import { useState } from 'react';
import { Box, Typography, AppBar, Button, DialogActions, Dialog, DialogTitle, DialogContent } from '@mui/material';
import TextField from '@mui/material/TextField';

const Form = () => {
    const [name, setName] = useState('');
    const [grossMonthlyIncome, setGrossMonthlyIncome] = useState('');
    const [creditCardPayments, setCreditCardPayments] = useState('');
    const [carPayments, setCarPayments] = useState('');
    const [studentLoanPayments, setStudentLoanPayments] = useState('');
    const [appraisedValue, setAppraisedValue] = useState('');
    const [downPaymentOnHouse, setDownPaymentOnHouse] = useState('');
    const [loanAmount, setLoanAmount] = useState('');
    const [monthlyMortgagePayment, setMonthlyMortgagePayment] = useState('');
    const [creditScore, setCreditScore] = useState('');
    const [openDialog, setOpenDialog] = useState(false);
    const [messages, setMessages] = useState([]);


    const SubmitDetails = () => { 
        const data = {
            name: name,
            grossMonthlyIncome: grossMonthlyIncome,
            creditCardPayments: creditCardPayments,
            carPayments: carPayments,
            studentLoanPayments: studentLoanPayments,
            appraisedValue: appraisedValue,
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
                setMessages(data.message);
                setOpenDialog(true);
            })
            .catch(error => {
                console.log(error);
            });
    };

    return (
        <div>
            <AppBar position="static" sx={{display: "flex", flexDirection: "row"}}>
                <Button
                    onClick={() => window.location.href = "/"}
                    sx={{ my: 2, color: "white", display: "block" }}
                >
                    Home
                </Button>
                <Button
                    onClick={() => window.location.href = "/game"}
                    sx={{ my: 2, color: "white", display: "block" }}
                >
                    Game
                </Button>
                <Button
                    onClick={() => window.location.href = "/resources"}
                    sx={{ my: 2, color: "white", display: "block" }}
                >
                    Resources
                </Button>
            </AppBar>
            <Typography variant="h4" component="h4" gutterBottom sx={{marginTop: '2vh'}}>
                Can you buy your dream house?
            </Typography>
            <Typography variant="h6" component="h6" gutterBottom sx={{marginTop: '1vh'}}>
                Fill out the form below to see if you can buy your dream house!
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
                <TextField id="outlined-basic" label="Appraised House Value" variant="outlined" onChange={(e) => setAppraisedValue(e.target.value)} type="number"/>
                <TextField id="outlined-basic" label="Down Payment on House" variant="outlined" onChange={(e) => setDownPaymentOnHouse(e.target.value)} type="number"/>
                <TextField id="outlined-basic" label="Loan Amount" variant="outlined" onChange={(e) => setLoanAmount(e.target.value)} type="number"/>
                <TextField id="outlined-basic" label="Monthly Mortgage Payment" variant="outlined" onChange={(e) => setMonthlyMortgagePayment(e.target.value)} type="number"/>
                <TextField id="outlined-basic" label="Credit Score" variant="outlined" onChange={(e) => setCreditScore(e.target.value)} type="number"/>
                <Button variant="contained" onClick={() => SubmitDetails()}>Submit</Button>
            </Box>
            <Dialog 
                    sx={{
                        width: "50vw", 
                        marginLeft: "25vw", 
                        height: "50vh", 
                        marginTop: "25vh"
                    }}
                    open={openDialog}
                >
                    <DialogTitle>
                        { messages[0] === "You can buy a house!" 
                        ? <Typography variant="h4" sx={{marginTop: "3vh"}}>Congratulations!</Typography> 
                        : <Typography variant="h4" sx={{marginTop: "3vh"}}>Here are some things to improve:</Typography>}
                    </DialogTitle>
                    <DialogContent>
                        { messages[0] === "You can buy a house!"
                        ? <Typography variant="h6"sx={{marginTop: "2vh"}}>You meet the requirements for being able to purchase a house</Typography> 
                        : 
                            <Box sx={{display: "flex", flexDirection: "column"}}>
                                {
                                messages.map((message) => 
                                    <Typography variant="caption"sx={{marginTop: "1vh"}}>{message}</Typography>
                                )}
                            </Box>
                        }
                    </DialogContent> 
                    <DialogActions>
                        <Button onClick={() => setOpenDialog(false)}>Close</Button>
                    </DialogActions>
                </Dialog>
        </div>
    )
}

export default Form;