import { useState } from 'react';
import { Box, Button, Typography } from '@mui/material';
import TextField from '@mui/material/TextField';

const Form = () => {
    const [name, setName] = useState('');
    const [grossMonthlyIncome, setGrossMonthlyIncome] = useState('');
    const [creditCardPayments, setCreditCardPayments] = useState('');
    const [carPayments, setCarPayments] = useState('');
    const [studentLoanPayments, setStudentLoanPayments] = useState('');
    const [appraisedHouseValue, setAppraisedHouseValue] = useState('');
    const [downPaymentOnHouse, setDownPaymentOnHouse] = useState('');
    const [loanAmount, setLoanAmount] = useState('');
    const [monthlyMortgagePayment, setMonthlyMortgagePayment] = useState('');
    const [creditScore, setCreditScore] = useState('');


    const SubmitDetails = () => { 
        const data = {
            name: name,
            grossMonthlyIncome: grossMonthlyIncome,
            creditCardPayments: creditCardPayments,
            carPayments: carPayments,
            studentLoanPayments: studentLoanPayments,
            appraisedHouseValue: appraisedHouseValue,
            downPaymentOnHouse: downPaymentOnHouse,
            loanAmount: loanAmount,
            monthlyMortgagePayment: monthlyMortgagePayment,
            creditScore: creditScore
        };

        const options = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data),
        };

        //eslint-disable-next-line
        console.log(data);

        fetch('http://localhost:8000/api/user', options)
            .then(response => response.json())
            .then(data => {
                console.log(data);
            })
            .catch(error => {
                console.log(error);
            });
    };

    return (
        <div>
            <Typography variant="h4" component="h4" gutterBottom sx={{marginTop: '5vh'}}>
                User Form
            </Typography>
            <Box 
                sx={{ 
                    display: 'flex', 
                    flexDirection: 'column', 
                    justifyContent: 'space-between', 
                    textAlign: 'center',
                    width: '50%',
                    marginLeft: '25%',
                    marginRight: '25%',
                    height: '80vh'
                }}
            >
                <TextField id="outlined-basic" label="Name" variant="outlined" onChange={(e) => setName(e.target.value)} />
                <TextField id="outlined-basic" label="Gross Monthly Income" variant="outlined" onChange={(e) => setGrossMonthlyIncome(e.target.value)} type="number"/>
                <TextField id="outlined-basic" label="Credit Card Payments" variant="outlined" onChange={(e) => setCreditCardPayments(e.target.value)} type="number"/>
                <TextField id="outlined-basic" label="Car Payments" variant="outlined" onChange={(e) => setCarPayments(e.target.value)} type="number"/>
                <TextField id="outlined-basic" label="Student Loan Payments" variant="outlined" onChange={(e) => setStudentLoanPayments(e.target.value)} type="number"/>
                <TextField id="outlined-basic" label="Appraised House Value" variant="outlined" onChange={(e) => setAppraisedHouseValue(e.target.value)} type="number"/>
                <TextField id="outlined-basic" label="Down Payment on House" variant="outlined" onChange={(e) => setDownPaymentOnHouse(e.target.value)} type="number"/>
                <TextField id="outlined-basic" label="Loan Amount" variant="outlined" onChange={(e) => setLoanAmount(e.target.value)} type="number"/>
                <TextField id="outlined-basic" label="Monthly Mortgage Payment" variant="outlined" onChange={(e) => setMonthlyMortgagePayment(e.target.value)} type="number"/>
                <TextField id="outlined-basic" label="Credit Score" variant="outlined" onChange={(e) => setCreditScore(e.target.value)} type="number"/>
                <Button variant="contained" onClick={() => SubmitDetails()}>Submit</Button>
            </Box>
        </div>
    )
}

export default Form;