import { AppBar, Container, Typography, Button, Card, CardActions, CardContent, CardMedia, CssBaseline, Grid, Toolba, Box, Link, Divider } from "@mui/material";


const resources = [
    {
        "title": "Consumer Financial Protection Bureau: Understanding Loan Options",
        "link": "https://www.consumerfinance.gov/owning-a-home/loan-options/",
        "description": "This website provides information on the different types of loans available to consumers. This is a great resources for those who are looking to buy a home and need to know what type of loan they should get."
    },
    {
        "title": "Loans for First-Time Homebuyers: How to Finance",
        "link": "https://www.investopedia.com/articles/mortgages-real-estate/08/homebuyer-financing-option.asp",
        "description": "This resource provides critical information on the different types of loans available to first-time homebuyers. This is a great resource for those who are looking to buy a home and need to know what type of loan they should get."
    },
    {
        "title": "How to Buy a House: A 9-Step Guide for the First-Time Buyer",
        "link": "https://www.moneyunder30.com/how-to-buy-a-house",
        "description": "This resource provides a 9-step guide for first-time homebuyers. This is a great resource for those who are looking to buy a home and need to know the steps they should take."
    }
]


const Resources = () => {
    return <>
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
        <Typography variant="h3" sx={{marginTop: "3vh"}}>Resources</Typography>
        <Typography variant="h5" align="center" sx={{marginTop: "2vh"}}>
            The Resources are there to provide helpful information and allow you to gain more opportunities
        </Typography>
        <Divider sx={{width:"80%", marginTop: "3vh", marginLeft: "10%"}} />
        <Box sx={{width: "60vw", display: "flex", flexDirection: "column", justifyContent: "center", marginTop: "3vw"}}>
                {
                    resources.map((resource) => (
                        <div style={{marginLeft: "20vw", width: "100%", marginTop: "2vh"}}>
                            <Typography variant="h3" align="start" sx={{marginBottom: "1vh"}}>
                                <Link href={resource.link} underline="hover">
                                    {resource.title}
                                </Link>
                            </Typography>
                            <Typography variant="h6" align="start">
                                {resource.description}
                            </Typography>
                        </div>
                    ))
                }
        </Box>
    </>
};

export default Resources;