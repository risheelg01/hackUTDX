from fastapi import HTTPException, APIRouter
from fastapi.responses import JSONResponse
from fastapi_sqlalchemy import db
from sqlalchemy import select
from models.user import User as ModelUser
from serialization.user import User as PydanticUser
from serialization.person import Person as PydanticPerson

router = APIRouter()

class Person:
    def __init__(self, grossMonthlyIncome, creditCardPayments, carPayments, studentLoanPayments, appraisedValue, downPaymentOnHouse, loanAmount, monthlyMortgagePayment, creditScore):
        self.grossMonthlyIncome = grossMonthlyIncome
        self.creditCardPayments = creditCardPayments
        self.carPayments = carPayments
        self.studentLoanPayments = studentLoanPayments
        self.appraisedValue = appraisedValue
        self.downPaymentOnHouse = downPaymentOnHouse
        self.loanAmount = loanAmount
        self.monthlyMortgagePayment = monthlyMortgagePayment
        self.creditScore = creditScore
    
    def ltv(self):
        if 1.0 * (self.loanAmount) / self.appraisedValue > .95:
            return False
        if 1.0 * (self.loanAmount) / self.appraisedValue > .8:
            self.monthlyMortgagePayment *= 1.01
        return True

    def dti(self):
        return (self.creditCardPayments + self.carPayments + self.monthlyMortgagePayment) / self.grossMonthlyIncome < .43
    
    def fedti(self):
        return 1.0 * self.monthlyMortgagePayment / self.grossMonthlyIncome <= .28
    
    def approval(self):
        approval = True
        messages = []
        if self.creditScore < 640:
            messages.append("Improve your credit score. To improve your credit score, pay your bills on time, keep credit card balances low (below 30% of your credit limit), and avoid closing old accounts. These three actions have the most significant impact on your credit score and can lead to noticeable improvements over time.")
            approval = False
        if not self.ltv():
            messages.append("Increase your down payment. A larger down payment is better because it results in lower monthly payments, reduces interest costs, and can lead to better loan terms. It also demonstrates financial stability to lenders, increasing your chances of loan approval. Additionally, a substantial down payment builds equity from the start and offers financial security in case of unexpected events")
            approval = False
        if not self.dti():
            messages.append("Continue renting while saving more for a down payment. Renting before buying a home can be a wise choice because it allows you to save for a down payment while avoiding the financial commitments and responsibilities of homeownership. It gives you the flexibility to assess your housing needs and preferences before making a long-term commitment. Renting can also provide time to improve your credit score and financial stability, making it easier to secure a favorable mortgage when you're ready to purchase a home.")
            approval = False
        if not self.fedti():
            messages.append("Look for a less expensive home. Based on analysis, it appears that this home might be stretching your finances more than anticipated. To maintain financial security and peace of mind, it might be a good idea to consider more affordable housing options that better match your current budget and future financial plans")
            approval = False

        if approval:
            messages.append("You can buy this house!")
        
        return messages

@router.post("/api/user")
def check_approval(person_input: PydanticPerson):
    person = Person(
        grossMonthlyIncome = person_input.grossMonthlyIncome,
        creditCardPayments = person_input.creditCardPayments,
        carPayments = person_input.carPayments,
        studentLoanPayments = person_input.studentLoanPayments,
        appraisedValue = person_input.appraisedValue,
        downPaymentOnHouse = person_input.downPaymentOnHouse,
        loanAmount = person_input.loanAmount,
        monthlyMortgagePayment = person_input.monthlyMortgagePayment,
        creditScore = person_input.creditScore
    )
    messages = person.approval()
    return JSONResponse(
            status_code=201, 
            content={"message": messages}
        )

@router.post("/user/")
async def create_user(user: PydanticUser):
    try:
        user = ModelUser(
            name=user.name,
            email=user.email,
            areas_of_interest=user.areas_of_interest,
            bio=user.bio,
            accessToken=user.accessToken
        )
        db.session.add(user)
        db.session.commit()
        return JSONResponse(
            status_code=201, 
            content={"message": "User created successfully"}
        )
    except BaseException as exception:
        raise HTTPException(status_code=400, detail=exception)

@router.get("/user/uid/{id}", response_model=bool)
async def user_uid_exists(id: str):
    user = db.session.query(ModelUser).filter_by(accessToken=id).first()
    if not user:
        return False
    return True

@router.get("/user/{id}", response_model=PydanticUser)
async def get_user(id: str):
    modelUser = db.session.execute(select(ModelUser).filter_by(accessToken=id)).first()[0]
    user = PydanticUser(
        name=modelUser.name,
        email=modelUser.email,
        areas_of_interest=modelUser.areas_of_interest,
        bio=modelUser.bio,
        accessToken=modelUser.accessToken
    )
    return user