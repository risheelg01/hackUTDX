from fastapi import HTTPException, APIRouter
from fastapi.responses import JSONResponse
from fastapi_sqlalchemy import db
from sqlalchemy import select
from models.user import User as ModelUser
from serialization.user import User as PydanticUser
from serialization.person import Person as PydanticPerson

router = APIRouter()

class Person:
    def __init__(self, grossMonthlyIncome, creditCardPayments, carPayments, studentLoanPayments, downPaymentOnHouse, loanAmount, monthlyMortgagePayment, creditScore):
        self.grossMonthlyIncome = grossMonthlyIncome
        self.creditCardPayments = creditCardPayments
        self.carPayments = carPayments
        self.studentLoanPayments = studentLoanPayments
        self.downPaymentOnHouse = downPaymentOnHouse
        self.loanAmount = loanAmount
        self.monthlyMortgagePayment = monthlyMortgagePayment
        self.creditScore = creditScore
    
    def ltv(self):
        if 1.0 * (self.downPaymentOnHouse - self.monthlyMortgagePayment) / self.downPaymentOnHouse > .95:
            return False
        if 1.0 * (self.downPaymentOnHouse - self.monthlyMortgagePayment) / self.downPaymentOnHouse > .8:
            self.studentLoanPayments *= 1.1
        return True

    def dti(self):
        return (self.creditCardPayments + self.carPayments + self.loanAmount) / self.grossMonthlyIncome < .43
    
    def fedti(self):
        return 1.0 * self.loanAmount / self.grossMonthlyIncome <= .28
    
    def approval(self):
        approval = True
        messages = []
        if self.creditScore < 640:
            messages.append("Improve credit score")
            approval = False
        if not self.ltv():
            messages.append("Increase your down payment")
            approval = False
        if not self.dti():
            messages.append("Continue renting while saving more for a down payment")
            approval = False
        if not self.fedti():
            messages.append("Look for a less expensive home")
            approval = False

        if approval:
            messages.append("You can buy a house!")
        
        return messages

@router.post("/api/user")
def check_approval(person_input: PydanticPerson):
    person = Person(
        grossMonthlyIncome = person_input.grossMonthlyIncome,
        creditCardPayments = person_input.creditCardPayments,
        carPayments = person_input.carPayments,
        studentLoanPayments = person_input.studentLoanPayments,
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