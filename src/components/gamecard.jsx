import { useEffect, useState } from "react";
import { Box, Button, Card, Dialog, DialogContent, DialogTitle, Grid, Typography } from "@mui/material"

const GameCard = () => {
    const [grossMonthlyIncome, setGrossMonthlyIncome] = useState(null);
    const [creditCardPayments, setCreditCardPayments] = useState(null);
    const [carPayments, setCarPayments] = useState(null);
    const [studentLoanPayments, setStudentLoanPayments] = useState(null);
    const [appraisedValue, setAppraisedValue] = useState(null);
    const [downPaymentOnHouse, setDownPaymentOnHouse] = useState(null);
    const [loanAmount, setLoanAmount] = useState(null);
    const [monthlyMortgagePayment, setMonthlyMortgagePayment] = useState(null);
    const [creditScore, setCreditScore] = useState(null);
    const [risk, setRisk] = useState(50);
    const [turns, setTurns] = useState(0);
    const [gameOver, setGameOver] = useState(false);
    const [congratulations, setCongratulations] = useState(false);
    const [title, setTitle] = useState("Welcome to the game!");
    const [description, setDescription] = useState("Let's see if you can buy a house!");
    const [leftButtonText, setLeftButtonText] = useState("Start Game");
    const [rightButtonText, setRightButtonText] = useState("Back to Home");
    const [leftButtonActions, setLeftButtonActions] = useState([]);
    const [rightButtonActions, setRightButtonActions] = useState([]);

    useEffect(() => {
        if (!grossMonthlyIncome) {
            fetch('http://localhost:8000/api/rand_person', {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json'
                }
            })
                .then(response => response.json())
                .then(data => {
                    console.log(data);
                    setGrossMonthlyIncome(data.grossMonthlyIncome);
                    setCreditCardPayments(data.creditCardPayments);
                    setCarPayments(data.carPayments);
                    setStudentLoanPayments(data.studentLoanPayments);
                    setAppraisedValue(data.appraisedValue);
                    setDownPaymentOnHouse(data.downPaymentOnHouse);
                    setLoanAmount(data.loanAmount);
                    setMonthlyMortgagePayment(data.monthlyMortgagePayment);
                    setCreditScore(data.creditScore);
                })
                .catch(error => {
                    console.log(error);
                });
        }
    }, []);

    const isGameOver = () => {
        if (turns == 15) {
            setGameOver(true);
        }
    }

    const LeftButtonClick = () => {
        isGameOver();
        const data = {
            name: '',
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
        
        fetch('http://localhost:8000/api/situation', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        }).then(response => response.json()).then(data => {
            console.log(data);
            setTitle(data.title);
            setDescription(data.description);
            if (data.options.length > 0) {
                setLeftButtonText(data.options[0].title);
                setRightButtonText(data.options[1].title);
                setLeftButtonActions(data.options[0].effect_on_player);
                setRightButtonActions(data.options[1].effect_on_player);
            }
            if (data.title == "Congratulations!") {
                setCongratulations(true);
            }
        })

        for (let i = 0; i < leftButtonActions.length; i++) {
            if (leftButtonActions[i].is_positive == true) {
                if (leftButtonActions[i].attribute == "grossMonthlyIncome") {
                    setGrossMonthlyIncome(grossMonthlyIncome + leftButtonActions[i].amount);
                } else if (leftButtonActions[i].attribute == "creditCardPayments") {
                    setCreditCardPayments(creditCardPayments + leftButtonActions[i].amount);
                } else if (leftButtonActions[i].attribute == "carPayments") {
                    setCarPayments(carPayments + leftButtonActions[i].amount);
                } else if (leftButtonActions[i].attribute == "studentLoanPayments") {
                    setStudentLoanPayments(studentLoanPayments + leftButtonActions[i].amount);
                } else if (leftButtonActions[i].attribute == "appraisedValue") {
                    setAppraisedValue(appraisedValue + leftButtonActions[i].amount);
                } else if (leftButtonActions[i].attribute == "downPaymentOnHouse") {
                    setDownPaymentOnHouse(downPaymentOnHouse + leftButtonActions[i].amount);
                } else if (leftButtonActions[i].attribute == "loanAmount") {
                    setLoanAmount(loanAmount + leftButtonActions[i].amount);
                } else if (leftButtonActions[i].attribute == "monthlyMortgagePayment") {
                    setMonthlyMortgagePayment(monthlyMortgagePayment + leftButtonActions[i].amount);
                } else if (leftButtonActions[i].attribute == "creditScore") {
                    setCreditScore(Math.min(creditScore + leftButtonActions[i].amount, 850));
                } else if (leftButtonActions[i].attribute == "risk") {
                    if (risk + leftButtonActions[i].amount > 100) {
                        setRisk(100);
                        setGameOver(true);
                    } else {
                        setRisk(risk + leftButtonActions[i].amount);
                    }
                }
            } else {
                if (leftButtonActions[i].attribute == "grossMonthlyIncome") {
                    setGrossMonthlyIncome(Math.max(grossMonthlyIncome - leftButtonActions[i].amount));
                } else if (leftButtonActions[i].attribute == "creditCardPayments") {
                    setCreditCardPayments(Math.max(creditCardPayments - leftButtonActions[i].amount, 0));
                } else if (leftButtonActions[i].attribute == "carPayments") {
                    setCarPayments(Math.max(carPayments - leftButtonActions[i].amount, 0));
                } else if (leftButtonActions[i].attribute == "studentLoanPayments") {
                    setStudentLoanPayments(Math.max(studentLoanPayments - leftButtonActions[i].amount, 0));
                } else if (leftButtonActions[i].attribute == "appraisedValue") {
                    setAppraisedValue(appraisedValue - leftButtonActions[i].amount);
                } else if (leftButtonActions[i].attribute == "downPaymentOnHouse") {
                    setDownPaymentOnHouse(downPaymentOnHouse - leftButtonActions[i].amount);
                } else if (leftButtonActions[i].attribute == "loanAmount") {
                    setLoanAmount(loanAmount - leftButtonActions[i].amount);
                } else if (leftButtonActions[i].attribute == "monthlyMortgagePayment") {
                    setMonthlyMortgagePayment(monthlyMortgagePayment - leftButtonActions[i].amount);
                } else if (leftButtonActions[i].attribute == "creditScore") {
                    setCreditScore(Math.min(creditScore - leftButtonActions[i].amount, 300));
                } else if (leftButtonActions[i].attribute == "risk") {
                    setRisk(Math.max(risk - leftButtonActions[i].amount, 0));
                }
            }
        }
        setTurns((turns) => turns + 1);  
    }

    const RightButtonClick = () => {
        if (rightButtonText == "Back to Home") {
            window.location.href = '/';
        }
        isGameOver();
        const data = {
            name: '',
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
        
        fetch('http://localhost:8000/api/situation', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        }).then(response => response.json()).then(data => {
            console.log(data);
            setTitle(data.title);
            setDescription(data.description);
            setLeftButtonText(data.options[0].title);
            setRightButtonText(data.options[1].title);
            setLeftButtonActions(data.options[0].effect_on_player);
            setRightButtonActions(data.options[1].effect_on_player);
        })
        for (let i = 0; i < rightButtonActions.length; i++) {
            if (rightButtonActions[i].is_positive == true) {
                if (rightButtonActions[i].attribute == "grossMonthlyIncome") {
                    setGrossMonthlyIncome(grossMonthlyIncome + rightButtonActions[i].amount);
                } else if (rightButtonActions[i].attribute == "creditCardPayments") {
                    setCreditCardPayments(creditCardPayments + rightButtonActions[i].amount);
                } else if (rightButtonActions[i].attribute == "carPayments") {
                    setCarPayments(carPayments + rightButtonActions[i].amount);
                } else if (rightButtonActions[i].attribute == "studentLoanPayments") {
                    setStudentLoanPayments(studentLoanPayments + rightButtonActions[i].amount);
                } else if (rightButtonActions[i].attribute == "appraisedValue") {
                    setAppraisedValue(appraisedValue + rightButtonActions[i].amount);
                } else if (rightButtonActions[i].attribute == "downPaymentOnHouse") {
                    setDownPaymentOnHouse(downPaymentOnHouse + rightButtonActions[i].amount);
                } else if (rightButtonActions[i].attribute == "loanAmount") {
                    setLoanAmount(loanAmount + rightButtonActions[i].amount);
                } else if (rightButtonActions[i].attribute == "monthlyMortgagePayment") {
                    setMonthlyMortgagePayment(monthlyMortgagePayment + rightButtonActions[i].amount);
                } else if (rightButtonActions[i].attribute == "creditScore") {
                    setCreditScore(Math.min(creditScore + rightButtonActions[i].amount, 850));
                } else if (rightButtonActions[i].attribute == "risk") {
                    setRisk(Math.min(risk - rightButtonActions[i].amount, 0));
                }
            } else {
                if (rightButtonActions[i].attribute == "grossMonthlyIncome") {
                    setGrossMonthlyIncome(Math.max(grossMonthlyIncome - rightButtonActions[i].amount, 0));
                } else if (rightButtonActions[i].attribute == "creditCardPayments") {
                    setCreditCardPayments(Math.max(creditCardPayments - rightButtonActions[i].amount, 0));
                } else if (rightButtonActions[i].attribute == "carPayments") {
                    setCarPayments(Math.max(carPayments - rightButtonActions[i].amount, 0));
                } else if (rightButtonActions[i].attribute == "studentLoanPayments") {
                    setStudentLoanPayments(Math.max(studentLoanPayments - rightButtonActions[i].amount, 0));
                } else if (rightButtonActions[i].attribute == "appraisedValue") {
                    setAppraisedValue(appraisedValue - rightButtonActions[i].amount);
                } else if (rightButtonActions[i].attribute == "downPaymentOnHouse") {
                    setDownPaymentOnHouse(downPaymentOnHouse - rightButtonActions[i].amount);
                } else if (rightButtonActions[i].attribute == "loanAmount") {
                    setLoanAmount(loanAmount - rightButtonActions[i].amount);
                } else if (rightButtonActions[i].attribute == "monthlyMortgagePayment") {
                    setMonthlyMortgagePayment(monthlyMortgagePayment - rightButtonActions[i].amount);
                } else if (rightButtonActions[i].attribute == "creditScore") {
                    setCreditScore(Math.max(creditScore - rightButtonActions[i].amount, 300));
                } else if (rightButtonActions[i].attribute == "risk") {
                    if (risk + rightButtonActions[i].amount > 100) {
                        setRisk(100);
                        setGameOver(true);
                    } else {
                        setRisk(risk + rightButtonActions[i].amount);
                    }
                }
            }
        }
        setTurns((turns) => turns + 1);
    };

    return (
        <>
            <Card sx={{marginTop: "3vh"}} raised>
                <Box sx={{display: "flex", flexDirection: "row", justifyContent: "space-between", marginBottom: "1vh", marginTop: "1vh", textAlign: "start"}}>
                    <Box sx={{display: "flex", flexDirection: "column", marginRight: "5%", marginLeft: "5%"}}> 
                        <Typography variant="caption">Gross Monthly Income: <b>${grossMonthlyIncome}</b></Typography>
                        <Typography variant="caption">Credit Card Payments: <b>${creditCardPayments}</b></Typography>
                        <Typography variant="caption">Car Payments: <b>${carPayments}</b></Typography>
                    </Box>
                    <Box sx={{display: "flex", flexDirection: "column", marginRight: "5%", marginLeft: "5%"}}>
                        <Typography variant="caption">Student Loan Payments: <b>${studentLoanPayments}</b></Typography>
                        <Typography variant="caption">Appraised Value: <b>${appraisedValue}</b></Typography>
                        <Typography variant="caption">Down Payment on House: <b>${downPaymentOnHouse}</b></Typography>
                    </Box>
                    <Box sx={{display: "flex", flexDirection: "column", marginRight: "5%", marginLeft: "5%"}}>
                        <Typography variant="caption">Loan Amount: <b>${loanAmount}</b></Typography>
                        <Typography variant="caption">Monthly Mortgage Payment: <b>${monthlyMortgagePayment}</b></Typography>
                        <Typography variant="caption">Credit Score: <b>{creditScore}</b></Typography>
                    </Box>
                    <Box sx={{display: "flex", flexDirection: "column", marginRight: "5%", marginLeft: "5%"}}>
                        <Typography variant="caption">Risk: <b>{risk}%</b></Typography>
                    </Box>
                </Box>
            </Card>
            <Card sx={{width: "100%", height: "50vh", marginTop: "4vh"}} raised>
                <Typography variant="h4" sx={{marginTop: "3vh", marginRight: "4vw", marginLeft: "4vw"}}>{title}</Typography>
                <Typography variant="h6"sx={{marginTop: "2vh", marginRight: "4vw", marginLeft: "4vw"}}>{description}</Typography>
                <Box sx={{display: "flex", flexDirection: "row", justifyContent: "center", marginTop: "2vh", marginRight: "4vw", marginLeft: "4vw"}}>
                    <Button variant="contained" sx={{width: "30%", height: "5vh", marginRight:"1vw"}} onClick={() => LeftButtonClick()}>{leftButtonText}</Button>
                    <Button variant="contained" sx={{width: "30%", height: "5vh", marginLeft:"1vw"}} onClick={() => RightButtonClick()}>{rightButtonText}</Button>
                </Box>
                <Dialog 
                    sx={{
                        width: "50vw", 
                        marginLeft: "25vw", 
                        height: "50vh", 
                        marginTop: "25vh"
                    }}
                    open={gameOver || congratulations}
                >
                    <DialogTitle>
                        { gameOver 
                        ? <Typography variant="h4" sx={{marginTop: "3vh"}}>Game Over</Typography> 
                        : <Typography variant="h4" sx={{marginTop: "3vh"}}>Congradulations!</Typography>}
                    </DialogTitle>
                    <DialogContent>
                        { gameOver 
                        ? <Typography variant="h6"sx={{marginTop: "2vh"}}>You have reached the end of the game! Better luck next time</Typography> 
                        : <Typography variant="h6"sx={{marginTop: "2vh"}}>You can successfully buy the house of your dreams!</Typography>}
                        <Box sx={{display: "flex", flexDirection: "row", justifyContent: "center", marginTop: "2vh"}}>
                            <Button variant="contained" sx={{width: "30%", height: "5vh", marginLeft:"1vw"}} onClick={() => window.location.reload()}>Play Again</Button>
                            <Button variant="contained" sx={{width: "30%", height: "5vh", marginLeft:"1vw"}} onClick={() => window.location.href = '/'}>Go back to home</Button>
                        </Box>
                    </DialogContent> 
                </Dialog>
            </Card>
        </>
    )
}

export default GameCard;