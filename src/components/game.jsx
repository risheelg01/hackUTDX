import { Box, Typography, AppBar, Button } from "@mui/material";
import GameCard from "../components/gamecard";

const Game = () => {
    return (
        <>
            <AppBar position="static" sx={{display: "flex", flexDirection: "row"}}>
                <Button
                    onClick={() => window.location.href = '/'}
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
            <div style={{width:"50%", marginLeft: "25%"}}>
                <Typography variant="h4" component="h4" gutterBottom sx={{marginTop: '5vh'}}>
                    Can you buy a house?
                </Typography>
                <Typography variant="h6" component="h6" gutterBottom sx={{marginTop: '1vh'}}>
                    An interactive game to where you are given a random person's financial information
                    and you must make life decisions towards buying their dream house.
                </Typography>
                    <GameCard />
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
                </Box>
            </div>
        </>
    )
};

export default Game;