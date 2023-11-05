import random
from fastapi import HTTPException, APIRouter
from fastapi.responses import JSONResponse
from serialization.situation import Situation as PydanticSituation
from serialization.person import Person as PydanticPerson
from handlers.util.situation import situations
from handlers.user import Person as PersonClass

router = APIRouter()

def generate_random_person():
    average_gross_monthly_income = 5979.11
    average_credit_card_payments = 350.89
    average_car_payments = 424.23
    average_student_loan_payments = 326.01
    average_credit_score = 700
    return (
        average_gross_monthly_income + random.randint(-1000, 1000),
        average_credit_card_payments + random.randint(-75, 75),
        average_car_payments + random.randint(-75, 75),
        average_student_loan_payments + random.randint(-50, 50),
        average_credit_score + random.randint(-100, 100)
    )

def generate_random_house():
    average_appraised_value = 365522.89
    average_down_payment_on_house = 62293.55
    random_down_payment_on_house = average_down_payment_on_house + random.randint(-10000, 10000)
    random_loan_amount = average_appraised_value - random_down_payment_on_house
    average_monthly_mortgage_payment = 1806.84
    return (
        average_appraised_value + random.randint(-50000, 50000),
        random_down_payment_on_house,
        random_loan_amount,
        average_monthly_mortgage_payment + random.randint(-100, 100)
    )

@router.post("/api/situation/", response_model=PydanticSituation)
async def getSituation(person_input: PydanticPerson):
    person = PersonClass(
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
    print(person.approval())
    if "You can buy a house!" in person.approval():
        return PydanticSituation(
            title = "Congratulations!",
            description = "You can buy your house!",
            options = []
        )
    else:
        random_index = random.randint(0, len(situations) - 1)
        random_situation = situations[random_index]
        random_situation = PydanticSituation(
            title = random_situation["title"],
            description = random_situation["description"],
            options = random_situation["options"]
        )
        return random_situation

@router.get("/api/rand_person/", response_model=PydanticPerson)
async def getRandPerson():
    grossMonthlyIncome, creditCardPayments, carPayments, studentLoanPayments, creditScore = generate_random_person()
    print(grossMonthlyIncome, creditCardPayments, carPayments, studentLoanPayments, creditScore)
    appraisedValue, downPaymentonHouse, loanAmount, monthlyMortgagePayment = generate_random_house()
    print(appraisedValue, downPaymentonHouse, loanAmount, monthlyMortgagePayment)
    return PydanticPerson(
        name='',
        grossMonthlyIncome = grossMonthlyIncome,
        creditCardPayments = creditCardPayments,
        carPayments = carPayments,
        studentLoanPayments = studentLoanPayments,
        appraisedValue = appraisedValue,
        downPaymentOnHouse = downPaymentonHouse,
        loanAmount = loanAmount,
        monthlyMortgagePayment = monthlyMortgagePayment,
        creditScore = creditScore
    )