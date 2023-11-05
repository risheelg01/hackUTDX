from pydantic import BaseModel

class Person(BaseModel):
    name: str
    grossMonthlyIncome: float
    creditCardPayments: float
    carPayments: float
    studentLoanPayments: float
    downPaymentOnHouse: float
    loanAmount: float
    monthlyMortgagePayment: float
    creditScore: int

    class config:
        orm_mode = True