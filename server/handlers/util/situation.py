situations = [
    {
        
        "title": "Changing Careers",
        "description": "You've received an opportunity to switch careers, moving from a field you've been in for years to a more lucrative but unfamiliar industry.",
        "prompt": "Write a 2-3 sentence paragraph for a situation in which the user must decide whether to embark on a new career path, knowing it offers a substantial income increase but carries the risk of starting from scratch. The user should not know they are in a game.",
        "options": [
            {
                "title": "Accept the offer",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "grossMonthlyIncome",
                        "amount": 3000
                    },
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 10
                    }
                ]
            },
            {
                "title": "Decline the offer",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 10
                    }
                ]
            }
        ]
    },
    {
        "title": "Investment Opportunity",
        "description": "A friend offers you a chance to invest in a promising startup, potentially yielding substantial profits, but it requires a significant initial investment.",
        "prompt": "Write a 2-3 sentence paragraph for a situation where the user must decide whether to invest in a startup, acknowledging the potential for substantial financial gains but considering the risk of losing the investment. The user should not know they are in a game.",
        "options": [
            {
                "title": "Invest in the startup",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "grossMonthlyIncome",
                        "amount": 3000
                    },
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 20
                    }
                ]
            },
            {
                "title": "Decline the offer",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 10
                    }
                ]
            }
        ]
    },
    {
        "title": "Advanced Education",
        "description": "You have the option to pursue advanced education, such as a master's degree or certification, which could lead to higher-paying job opportunities.",
        "prompt": "Write a 2-3 sentence paragraph for a situation where the user must decide whether to invest time and resources in advanced education, recognizing the potential for better-paying positions but considering the costs and time commitment. The user should not know they are in a game.",
        "options": [
            {
                "title": "Pursue advanced education",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "grossMonthlyIncome",
                        "amount": 2000
                    },
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 15
                    }
                ]
            },
            {
                "title": "Avoid further education",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 10
                    }
                ]
            }
        ]
    },
    {
        "title": "Freelancing Opportunity",
        "description": "A client offers you a lucrative freelance project, but it would require a significant time commitment and possibly affect your work-life balance.",
        "prompt": "Write a 2-3 sentence paragraph for a situation where the user must decide whether to take on the freelance project, knowing it offers higher income potential but considering the impact on work-life balance. The user should not know they are in a game.",
        "options": [
            {
                "title": "Accept the freelance project",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "grossMonthlyIncome",
                        "amount": 2000
                    },
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 10
                    }
                ]
            },
            {
                "title": "Decline the project",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 5
                    }
                ]
            }
        ]
    },
    {
        "title": "Relocation for Promotion",
        "description": "You've been offered a promotion within your current company, but it involves relocating to a more expensive city where the cost of living is higher.",
        "prompt": "Write a 2-3 sentence paragraph for a situation where the user must decide whether to accept the promotion and relocation, considering the higher income but also the increased living costs. The user should not know they are in a game.",
        "options": [
            {
                "title": "Accept the promotion and relocate",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "grossMonthlyIncome",
                        "amount": 3000
                    },
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 10
                    }
                ]
            },
            {
                "title": "Decline the promotion",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 5
                    }
                ]
           
            }
        ]
    },
    {
        "title": "Moving to a new city",
        "description": "You've been offered a higher paying job but it requires you to relocate to a more expensive city.",
        "prompt": "write a 2-3 sentence paragraph for a situation in a  where the user has to decide whether or not to move to a higher cost of living city for a higher paying job. The user should not know they are in a game.",
        "options": [
            {
                "title": "Accept the job",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "grossMonthlyIncome",
                        "amount": 5000
                    },
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 10
                    }
                ]
            },
            {
                "title": "Decline the job",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 10
                    }

                ]
            }
        ]
    },

    {
        "title": "Overtime Oppportunites",
        "description": " Your employer is offering overtime opportunities, but it will require you to work longer hours",
        "prompt": "write a 2-3 sentence paragraph for a situation where the user has to decide between taking overtime to increase income or prioritize work-life balance. The user should not know they are in a game.",
        "options": [
            {
                "title": "Take the overtime",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "grossMonthlyIncome",
                        "amount": 200
                    },
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 5
                    }
                ]
            },
            {
                "title": "Decline the overtime",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 5
                    }

                ]
            }
        ]
    },


    {
        "title": "Side Business",
        "description": " You have the chance to start a side business, but it may take time to become profitable",
        "prompt": "write a 2-3 sentence paragraph for a situation where the user has to decide between launching the business to potentially boost income or stick to current job for stability. The user should not know they are in a game.",
        "options": [
            {
                "title": "Launch the Business",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "grossMonthlyIncome",
                        "amount": 1000
                    },
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 10
                    }
                ]
            },
            {
                "title": "Stick to Current Job",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 10
                    }

                ]
            }
        ]
    },

    {
        "title": "Part-Time Job",
        "description": "You're considering a part-time job to supplement your income",
        "prompt": "write a 2-3 sentence paragraph for a situation where the user has to decide between taking a part-time job for additional income or focusing on current job and personal life. The user should not know they are in a game.",
        "options": [
            {
                "title": "Take the job",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "grossMonthlyIncome",
                        "amount": 3000
                    },
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 15
                    }
                ]
            },
            {
                "title": "Stick to Current Job",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 15
                    }

                ]
            }
        ]
    },


    {
        "title": "Unexpected Bonus",
        "description": "You've received an unexpected bonus at work",
        "prompt": "write a 2-3 sentence paragraph for a situation where the user has to decide between using the bonus to keep their car maintained or save the bonus for future expense. The user should not know they are in a game.",
        "options": [
            {
                "title": "Use bonus on car",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "carPayments",
                        "amount": 1000
                    }
                ]
            },
            {
                "title": "Save bonus",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 15
                    },
                    {
                        "is_positive": True,
                        "attribute": "grossMonthlyIncome",
                        "amount": 800
                    }

                ]
            }
        ]
    },

    {
        "title": "Spouse Job Opportunity",
        "description": "Your spouse is offered a job opportunity, but it would require a change in household income.",
        "prompt": "write a 2-3 sentence paragraph for a situation where the user's spouse has to decide to take the job for additional income or maintain current stability. The user should not know they are in a game.",
        "options": [
            {
                "title": "Take the job",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "grossMonthlyIncome",
                        "amount": 3000
                    }
                ]
            },
            {
                "title": "Save bonus",
                "effect_on_player": [
                ]
            }
        ]
    },

    {
        "title": "Longer Commute",
        "description": "You are offered a pay increase at your current job but with a longer commute.",
        "prompt": "write a 2-3 sentence paragraph for a situation where the user has to decide whether to accept pay raise for longer commute or decline the raise to save time and commute costs. The user should not know they are in a game.",
        "options": [
            {
                "title": "Increase Pay",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "grossMonthlyIncome",
                        "amount": 1000
                    },
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 7
                    },
                    {
                        "is_positive": True,
                        "attribute": "carPayments",
                        "amount": 200
                    }
                ]
            },
            {
                "title": "Decline and save",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 7
                    }
                ]
            }
        ]
    },


    {
        "title": "Job Security",
        "description": "You're considering a job that has less earning potential but with more job security.",
        "prompt": "write a 2-3 sentence paragraph for a situation where the user has to decide whether to pursue the lower-paying job for more security or stick with current job for consistency. The user should not know they are in a game.",
        "options": [
            {
                "title": "Take Job",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "grossMonthlyIncome",
                        "amount": 1000
                    },
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 10
                    },
                    
                ]
            },
            {
                "title": "Keep Current Job",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 2
                    }
                ]
            }
        ]
    },

    {
        "title": "Job Security",
        "description": "You're considering a job that has less earning potential but with more job security.",
        "prompt": "write a 2-3 sentence paragraph for a situation where the user has to decide whether to pursue the lower-paying job for more security or stick with current job for consistency. The user should not know they are in a game.",
        "options": [
            {
                "title": "Take Job",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "grossMonthlyIncome",
                        "amount": 1000
                    },
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 10
                    },
                    
                ]
            },
            {
                "title": "Keep Current Job",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 2
                    }
                ]
            }
        ]
    },

    {
        "title": "Freelance",
        "description": "You have an opportunity to freelance on the side, increasing your income.",
        "prompt": "write a 2-3 sentence paragraph for a situation where the user has to decide whether to take on freelance work for extra income or focus solely on full time job. The user should not know they are in a game.",
        "options": [
            {
                "title": "Freelance",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "grossMonthlyIncome",
                        "amount": 1000
                    },
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 8
                    },
                    
                ]
            },
            {
                "title": "Focus on Job",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 5
                    }
                ]
            }
        ]
    },

    {
        "title": "Invest in Business Venture",
        "description": "You are presented with the option to invest in a risky but potentially lucrative business venture.",
        "prompt": "write a 2-3 sentence paragraph for a situation where the user has to decide whether to invest in venture for financial gain or avoid the risk and focus on current income. The user should not know they are in a game.",
        "options": [
            {
                "title": "Invest",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "grossMonthlyIncome",
                        "amount": 2000
                    },
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 12
                    },
                    
                ]
            },
            {
                "title": "Focus on Job",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 10
                    }
                ]
            }
        ]
    },

    {
        "title": "Car Payment straining Budget",
        "description": "Your current car payment is straining your budget, and you've been offered a chance to refinance your auto loan.",
        "prompt": "write a 2-3 sentence paragraph for a situation where the user has to decide whether to refinance the auto loan to reduce the monthly car payment or stick with current car loan. The user should not know they are in a game.",
        "options": [
            {
                "title": "Invest",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "carPayments",
                        "amount": 1000
                    },
                    {
                        "is_positive": False,
                        "attribute": "creditCardPayments",
                        "amount": 500
                    },
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 10
                    }
                    
                ]
            },
            {
                "title": "Focus on Job",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 10
                    },
                    {
                        "is_positive": False,
                        "attribute": "creditScore",
                        "amount": 30
                    }
                ]
            }
        ]
    },


    {
        "title": "Old Car Repair",
        "description": "Your car is getting older and requires more frequent repairs. You have the option to trade it in for a more affordable and reliable model",
        "prompt": "write a 2-3 sentence paragraph for a situation where the user has to decide whether to trade in your car for a more reliable model with a higher monthly car payment or continue to invest in repairs. The user should not know they are in a game.",
        "options": [
            {
                "title": "Trade in Car",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "carPayments",
                        "amount": 7500
                    },
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 10
                    }
                ]
            },
            {
                "title": "Continue repairs",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "carPayments",
                        "amount": 5000
                    },
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 10
                    }
                ]
            }

        ]
    },

    {
        "title": "Car Engine Repair",
        "description": "You're at a crossroads with your car, as it needs a costly engine repair. You can decide whether to invest in the repair or consider replacing it.",
        "prompt": "write a 2-3 sentence paragraph for a situation where the user has to decide whether to invest in car engine repair or buy a more reliable and affordable car. The user should not know they are in a game.",
        "options": [
            {
                "title": "Invest in Engine Repair",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "carPayments",
                        "amount": 10000
                    },
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 5
                    }
                ]
            },
            {
                "title": "Replace Car",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "carPayments",
                        "amount": 15000
                    },
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 5
                    }
                ]
            }

        ]
    },

    {
        "title": "Lease Car",
        "description": "You've received an offer to lease a new car with lower monthly payments than your current car loan.",
        "prompt": "write a 2-3 sentence paragraph for a situation where the user has to decide whether to lease new car with lower monthly payments or continue with current car loan. The user should not know they are in a game.",
        "options": [
            {
                "title": "Lease new car",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "carPayments",
                        "amount": 5000
                    },
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 3
                    }
                ]
            },
            {
                "title": "Continue with car loan",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 5
                    }
                ]
            }

        ]
    },


    {
        "title": "Personal Car Loan",
        "description": "You're exploring the option of taking out a personal loan to pay off your existing car loan, potentially lowering your monthly expenses.",
        "prompt": "write a 2-3 sentence paragraph for a situation where the user has to decide whether to take a personal loan to lower monthly car payment or maintain current car loan. The user should not know they are in a game.",
        "options": [
            {
                "title": "Take out loan",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "carPayments",
                        "amount": 5000
                    },
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 10
                    },
                    {
                        "is_positive": False,
                        "attribute": "grossMonthlyIncome",
                        "amount": 5000
                    }
                ]
            },
            {
                "title": "Keep current car loan",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 5
                    }
                ]
            }

        ]
    },

    {
        "title": "Costly Car",
        "description": "Your current car is costly to maintain, and you're considering selling it to rely on public transportation or ridesharing services.",
        "prompt": "write a 2-3 sentence paragraph for a situation where the user has to decide whether to sell car to use public transport/rideshare or keep car. The user should not know they are in a game.",
        "options": [
            {
                "title": "Sell Car",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "carPayments",
                        "amount": 6000
                    },
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 10
                    }
                ]
            },
            {
                "title": "Keep Car",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 5
                    }
                ]
            }

        ]
    },

    {
        "title": "Fuel-inefficient Car",
        "description": "Your current car is fuel-inefficient, and you're thinking about trading it in for a more eco-friendly vehicle",
        "prompt": "write a 2-3 sentence paragraph for a situation where the user has to decide whether to trade in car for eco-friendly car or keep car. The user should not know they are in a game.",
        "options": [
            {
                "title": "Trade in Car",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "carPayments",
                        "amount": 1000
                    },
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 3
                    }
                ]
            },
            {
                "title": "Keep Car",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 3
                    }
                ]
            }

        ]
    },

    {
        "title": "Car Warranty Extension",
        "description": "You've been offered an extended warranty for your car, which would come with a monthly payment increase.",
        "prompt": "write a 2-3 sentence paragraph for a situation where the user has to decide whether to purchase extended car warranty for future repairs or decline the extra warranty and keep current payment. The user should not know they are in a game.",
        "options": [
            {
                "title": "Buy Warranty",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "carPayments",
                        "amount": 1000
                    },
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 5
                    },
                    {
                        "is_positive": False,
                        "attribute": "grossMonthlyIncome",
                        "amount": 500
                    }
                ]
            },
            {
                "title": "Decline Warranty",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 5
                    }
                ]
            }

        ]
    },


    {
        "title": "Car Insurance Premiums",
        "description": "Your car insurance premiums have increased, and you're considering shopping around for a more affordable insurance plan.",
        "prompt": "write a 2-3 sentence paragraph for a situation where the user has to decide whether to switch to affordable car insurance plan or keep current plan. The user should not know they are in a game.",
        "options": [
            {
                "title": "Switch insurance plans",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "carPayments",
                        "amount": 2000
                    },
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 5
                    }
                    
                ]
            },
            {
                "title": "Keep plan",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 5
                    }
                ]
            }

        ]
    },

    {
        "title": "Economic for Luxury Car",
        "description": "You've been driving a luxury car with high monthly payments but are considering trading it for a more economical model with a lower payment.",
        "prompt": "write a 2-3 sentence paragraph for a situation where the user has to decide whether to trade luxury car for economical car with lower monthly payments or continue enjoying luxury car. The user should not know they are in a game.",
        "options": [
            {
                "title": "Switch Car",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "carPayments",
                        "amount": 3000
                    },
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 3
                    }
                    
                ]
            },
            {
                "title": "Keep Car",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 3
                    }
                ]
            }

        ]
    },

    {
        "title": "Offer for Longer Car loan",
        "description": "You've received an offer for a new car with a longer loan term that would reduce your monthly payments but extend the overall repayment period.",
        "prompt": "write a 2-3 sentence paragraph for a situation where the user has to decide whether to choose car with extended loan term for lower monthly car payments but extend the overall repayment period or stick with current car loan terms. The user should not know they are in a game.",
        "options": [
            {
                "title": "Switch Car loan",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "carPayments",
                        "amount": 1000
                    }
                    
                ]
            },
            {
                "title": "Stick to Current Loan",
                "effect_on_player": [
                   
                ]
            }

        ]
    },

    {
        "title": "Keep, Sell, Or Trade Car",
        "description": " Your current car is almost paid off, but you're contemplating whether to keep it, sell it, or trade it for a newer model.",
        "prompt": "write a 2-3 sentence paragraph for a situation where the user has to decide whether to keep current car and eliminate monthly payment or sell/trade car for newer model with higher monthly payments. The user should not know they are in a game.",
        "options": [
            {
                "title": "Keep Car",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "carPayments",
                        "amount": 1200
                    },
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 3
                    }
                    
                ]
            },
            {
                "title": "Sell/Trade Car",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 3
                    }
                   
                ]
            }

        ]
    },

    {
        "title": "Credit Card Burden",
        "description": "Your monthly credit card payments are becoming a financial burden, and you've been offered a balance transfer with a lower interest rate.",
        "prompt": "write a 2-3 sentence paragraph for a situation where the user has to decide whether to accept the balance transfer to ease monthly credit card payments or continue making same card payments. The user should not know they are in a game.",
        "options": [
            {
                "title": "Accept Balance Transfer Offer",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "creditCardPayments",
                        "amount": 500
                    },
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 3
                    }
                    
                ]
            },
            {
                "title": "Make Card Payment",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 3
                    },
                    {
                        "is_positive": False,
                        "attribute": "creditScore",
                        "amount": 20
                    }
                   
                ]
            }

        ]
    },

    {
        "title": "Credit Card Burden",
        "description": "Your monthly credit card payments are becoming a financial burden, and you've been offered a balance transfer with a lower interest rate.",
        "prompt": "write a 2-3 sentence paragraph for a situation where the user has to decide whether to accept the balance transfer to ease monthly credit card payments or continue making same card payments. The user should not know they are in a game.",
        "options": [
            {
                "title": "Accept Balance Transfer Offer",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "creditCardPayments",
                        "amount": 500
                    },
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 3
                    }
                    
                ]
            },
            {
                "title": "Make Card Payment",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 3
                    },
                    {
                        "is_positive": False,
                        "attribute": "creditScore",
                        "amount": 20
                    }
                   
                ]
            }

        ]
    },

    {
        "title": "Consolidate Credit Card Debt",
        "description": "You have an opportunity to consolidate your credit card debt with a personal loan to potentially lower your monthly credit card payments.",
        "prompt": "write a 2-3 sentence paragraph for a situation where the user has to decide whether to use personal loan to reduce monthly credit card payments or keep credit card debt separate. The user should not know they are in a game.",
        "options": [
            {
                "title": "Consolidate Credit Card Debt",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "creditCardPayments",
                        "amount": 1000
                    },
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 3
                    }
                    
                ]
            },
            {
                "title": "Keep Card Debt Separate",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 3
                    }
                   
                ]
            }

        ]
    },

    {
        "title": "Close Credit Card",
        "description": "You're contemplating closing one of your credit cards with a high annual fee.",
        "prompt": "write a 2-3 sentence paragraph for a situation where the user has to decide whether to close the credit to avoid annual fee but affect credit score or keep credit card and pay annual fee. The user should not know they are in a game.",
        "options": [
            {
                "title": "Close Credit Card",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "creditCardPayments",
                        "amount": 100
                    },
                    {
                        "is_positive": False,
                        "attribute": "creditScore",
                        "amount": 40
                    },
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 10
                    }
                    
                ]
            },
            {
                "title": "Keep Card Open",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "creditCardPayments",
                        "amount": 100
                    },
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 10
                    }
                   
                ]
            }

        ]
    },

    {
        "title": "Credit Limit Increase",
        "description": "You've received a credit limit increase on your credit card, allowing you to manage your credit utilization ratio more effectively.",
        "prompt": "write a 2-3 sentence paragraph for a situation where the user has to decide whether to accept the credit limit increase or decline the increase. The user should not know they are in a game.",
        "options": [
            {
                "title": "Accept Increase",
                "effect_on_player": [
                   
                    {
                        "is_positive": True,
                        "attribute": "creditScore",
                        "amount": 40
                    },
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 10
                    }
                    
                ]
            },
            {
                "title": "Decline Increase",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 10
                    }
                   
                ]
            }

        ]
    },

    {
        "title": "Recently Graduated",
        "description": "You've recently graduated and are deciding whether to defer your student loan payments for a year.",
        "prompt": "write a 2-3 sentence paragraph for a situation in a  where the user has to decide whether or not they should defer their student loan payments. The user should not know they are in a game.",
        "options": [
            {
                "title": "Defer Payments",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "studentLoanPayments",
                        "amount": 500
                    },
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 5
                    }
                ]
            },
            {
                "title": "Make loan payments",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 5
                    }

                ]
            }
        ]
    },

    {
        "title": "Refinancing Student Loans",
        "description": "You're considering refinancing your student loans to lower your monthly payments.",
        "prompt": "write a 2-3 sentence paragraph for a situation in which  the user has to decide whether or not they should refinance their student loans to lower monthly payments. The user should not know they are in a game.",
        "options": [
            {
                "title": "Refinance Student Loans",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "studentLoanPayments",
                        "amount": 500
                    },
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 5
                    }
                ]
            },
            {
                "title": "Maintain Current Loan",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 5
                    }

                ]
            }
        ]

    },


{
"title": "Increased Income",
        "description": "Your income has increased, and you have the option to make extra payments on your student loans to pay them off faster.",
        "prompt": "write a 2-3 sentence paragraph for a situation in which  the user has to decide whether or not they should make extra payments on their student loans to pay them off faster. The user should not know they are in a game.",
        "options": [
            {
                "title": "Increase Payments",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "studentLoanPayments",
                        "amount": 500
                    },
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 5
                    }
                ]
            },
            {
                "title": "Continue Regular Payments",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 5
                    }

                ]
            }
        ]
},
{

"title": "Recently Graduated",
        "description": "You've recently graduated and are deciding whether to defer your student loan payments for a year.",
        "prompt": "write a 2-3 sentence paragraph for a situation in a  where the user has to decide whether or not they should defer their student loan payments. The user should not know they are in a game.",
        "options": [
            {
                "title": "Defer Payments",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "studentLoanPayments",
                        "amount": 500
                    },
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 5
                    }
                ]
            },
            {
                "title": "Make loan payments",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 5
                    }

                ]
            }
        ]
},

{
"title": "Refinancing Student Loans",
        "description": "You're considering refinancing your student loans to lower your monthly payments.",
        "prompt": "write a 2-3 sentence paragraph for a situation in which  the user has to decide whether or not they should refinance their student loans to lower monthly payments. The user should not know they are in a game.",
        "options": [
            {
                "title": "Refinance Student Loans",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "studentLoanPayments",
                        "amount": 500
                    },
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 5
                    }
                ]
            },
            {
                "title": "Maintain Current Loan",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 5
                    }

                ]
            }
        ]
},
{

"title": "Increased Income",
        "description": "Your income has increased, and you have the option to make extra payments on your student loans to pay them off faster.",
        "prompt": "write a 2-3 sentence paragraph for a situation in which  the user has to decide whether or not they should make extra payments on their student loans to pay them off faster. The user should not know they are in a game.",
        "options": [
            {
                "title": "Increase Payments",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "studentLoanPayments",
                        "amount": 500
                    },
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 5
                    }
                ]
            },
            {
                "title": "Continue Regular Payments",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 5
                    }

                ]
            }
        ]
},
{
"title": "Loan Forgiveness",
        "description": "You've been offered the opportunity to participate in a loan forgiveness program for your profession.",
        "prompt": "write a 2-3 sentence paragraph for a situation in which  the user has to decide whether or not they should participate in a loan forgiveness program for their profession. The user should not know they are in a game.",
        "options": [
            {
                "title": "Enroll in Loan Forgiveness",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "studentLoanPayments",
                        "amount": 500
                    },
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 5
                    }
                ]
            },
            {
                "title": "Forego the program",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 5
                    }

                ]
            }
        ]

},
{

"title": "Extending Loan term",
        "description": "You're considering extending the loan term to lower your monthly student loan payments.",
        "prompt": "write a 2-3 sentence paragraph for a situation in which  the user has to decide whether or not they should extend the loan term to lower their monthly student loan payments. The user should not know they are in a game.",
        "options": [
            {
                "title": "Extend Loan term",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "studentLoanPayments",
                        "amount": 500
                    },
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 5
                    }
                ]
            },
            {
                "title": "Keep original loan term",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 5
                    }

                ]
            }
        ]

},
{

"title": "Significant Payment Towards Student Loans",
        "description": "You've received a lump sum of money, and you're deciding whether to make a significant payment toward your student loans.",
        "prompt": "write a 2-3 sentence paragraph for a situation in which  the user has to decide whether or not they should use this lump sum of money to make a significant payment towards their student loans. The user should not know they are in a game.",
        "options": [
            {
                "title": "Make a large payment",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "studentLoanPayments",
                        "amount": 500
                    },
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 5
                    }
                ]
            },
            {
                "title": "Continue regular payments",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 5
                    }

                ]
            }
        ]
},
{

"title": "Income-Driven Repayment Plan",
        "description": "You have the option to apply for an income-driven repayment plan, which adjusts your monthly payments based on your income.",
        "prompt": "write a 2-3 sentence paragraph for a situation in which  the user has to decide whether or not they should apply for this income-driven repayment plan that adjusts monthly payments based on income. The user should not know they are in a game.",
        "options": [
            {
                "title": "Apply for repayment plan",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "studentLoanPayments",
                        "amount": 500
                    },
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 5
                    }
                ]
            },
            {
                "title": "Stick current payment plan",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 5
                    }

                ]
            }
        ]

},
{

"title": "Tax Refund",
        "description": "You're considering using your tax refund to make an extra payment toward your student loans.",
        "prompt": "write a 2-3 sentence paragraph for a situation in which  the user has to decide whether or not they should consider using their tax refund to make an extra payment towards their student loans. The user should not know they are in a game.",
        "options": [
            {
                "title": "Use your tax refund",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "studentLoanPayments",
                        "amount": 500
                    },
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 5
                    }
                ]
            },
            {
                "title": "Allocate your tax refund",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 5
                    }

                ]
            }
        ]
},
{

"title": "Loan Consolidation Option",
        "description": "You're offered a loan consolidation option that combines multiple student loans into a single monthly payment.",
        "prompt": "write a 2-3 sentence paragraph for a situation in which the user has to decide whether or not they should use the loan consolidation option to combine multiple student loans into a single monthly payment. The user should not know they are in a game.",
        "options": [
            {
                "title": "Opt for the Loan Consolidation",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "studentLoanPayments",
                        "amount": 500
                    },
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 5
                    }
                ]
            },
            {
                "title": "Keep Loans seperate",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 5
                    }

                ]
            }
        ]
},

{
"title": "Part-Time Job",
        "description": "You're thinking about working a part-time job to increase your income and pay off your student loans faster.",
        "prompt": "write a 2-3 sentence paragraph for a situation in which  the user has to decide whether or not they should work a part-time job to increase income and pay off student loans faster. The user should not know they are in a game.",
        "options": [
            {
                "title": "Take on the part-time job",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "studentLoanPayments",
                        "amount": 500
                    },
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 5
                    }
                ]
            },
            {
                "title": "Focus on full time job",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 5
                    }

                ]
            }
        ]
},

{
"title": "Negotiate for Lower Interest Rate",
        "description": "You have the opportunity to negotiate with your lender for a lower interest rate on your student loans.",
        "prompt": "write a 2-3 sentence paragraph for a situation in which  the user has to decide whether or not they want to negotiate with the lender for a lower interest rate on their student loans. The user should not know they are in a game.",
        "options": [
            {
                "title": "Negotiate lower interest rate",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "studentLoanPayments",
                        "amount": 500
                    },
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 5
                    }
                ]
            },
            {
                "title": "Maintain current interest rate",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 5
                    }

                ]
            }
        ]
},
{

"title": "Pay Student Loans Off Quickly",
        "description": "You're debating whether to pay more than the minimum monthly payment on your student loans to pay them off more quickly.",
        "prompt": "write a 2-3 sentence paragraph for a situation in which  the user has to decide whether or not they would like to pay more than the minimum monthly payment on student loans to pay them off faster. The user should not know they are in a game.",
        "options": [
            {
                "title": "Pay Extra on Student Loans",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "studentLoanPayments",
                        "amount": 500
                    },
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 5
                    }
                ]
            },
            {
                "title": "Continue with minimum payments",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 5
                    }

                ]
            }
        ]
},
{

"title": "Consolidate Your Debts",
        "description": "You have the option to consolidate your debts, which could improve your credit score.",
        "prompt": "write a 2-3 sentence paragraph for a situation in which  the user has to decide whether or not they should consolidate their debts which could improve their credit score. The user should not know they are in a game.",
        "options": [
            {
                "title": "Consolidate debts to boost credit score",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "creditScore",
                        "amount": 50
                    },
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 5
                    }
                ]
            },
            {
                "title": "Keep debts as they are",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 5
                    }

                ]
            }
        ]
},
{
"title": "Credit Counseling Offer",
        "description": "You've been late on credit card payments, but you receive a credit counseling offer.",
        "prompt": "write a 2-3 sentence paragraph for a situation in which  the user has to decide whether or not they should accept the credit counseling offer as they are late on credit card payments. The user should not know they are in a game.",
        "options": [
            {
                "title": "Accept credit counseling",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "creditScore",
                        "amount": 50
                    },
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 5
                    }
                ]
            },
            {
                "title": "Decline and manage finance",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 5
                    }

                ]
            }
        ]
},
{

"title": "Co-Signing a Loan",
        "description": "You're considering co-signing a loan for a friend who is in financial trouble.",
        "prompt": "write a 2-3 sentence paragraph for a situation in which  the user has to decide whether or not they should co-sign a loan for a friend in financial trouble. The user should not know they are in a game.",
        "options": [
            {
                "title": "Co-sign the loan",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "creditScore",
                        "amount": 50
                    },
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 5
                    }
                ]
            },
            {
                "title": "Politely decline to co-sign",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 5
                    }

                ]
            }
        ]
},
{
"title": "Credit Card with High Credit Limit",
        "description": "You've been pre-approved for a credit card with a high credit limit.",
        "prompt": "write a 2-3 sentence paragraph for a situation in which  the user has to decide whether or not they should accept a pre-approved credit card with a high credit limit. The user should not know they are in a game.",
        "options": [
            {
                "title": "Accept the Credit Card",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "creditScore",
                        "amount": 50
                    },
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 5
                    }
                ]
            },
            {
                "title": "Decline the Credit Card",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 5
                    }

                ]
            }
        ]
},
{
"title": "Closing Credit Card Account",
        "description": " You're thinking of closing an old credit card account.",
        "prompt": "write a 2-3 sentence paragraph for a situation in which  the user has to decide whether or not they should close their old credit card account. The user should not know they are in a game.",
        "options": [
            {
                "title": "Close the account",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "creditScore",
                        "amount": 50
                    },
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 5
                    }
                ]
            },
            {
                "title": "Keep the account open",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "creditScore",
                        "amount": 5
                    }

                ]
            }
        ]

},
{
"title": "Credit Limit Increase",
        "description": "You've been offered a credit limit increase on your credit card.",
        "prompt": "write a 2-3 sentence paragraph for a situation in which  the user has to decide whether or not they should accept the credit limit increase on their credit card. The user should not know they are in a game.",
        "options": [
            {
                "title": "Accept the Increased Limit",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "creditScore",
                        "amount": 50
                    },
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 5
                    }
                ]
            },
            {
                "title": "Decline the credit limit",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 5
                    }

                ]
            }
        ]
},
{
"title": "Credit Repair Service",
        "description": "You're considering a credit repair service to boost your credit score.",
        "prompt": "write a 2-3 sentence paragraph for a situation in which  the user has to decide whether or not they should consult a credit repair service to boost their credit score. The user should not know they are in a game.",
        "options": [
            {
                "title": "Use the repair service",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "creditScore",
                        "amount": 50
                    },
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 5
                    }
                ]
            },
            {
                "title": "Improve credit independently",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 5
                    }

                ]
            }
        ]
},
{
"title": "Authorized User on Friend's Card",
        "description": "You have the opportunity to add yourself as an authorized user on a friend's credit card.",
        "prompt": "write a 2-3 sentence paragraph for a situation in which  the user has to decide whether or not they should accept the offer to add themselves as an authorized user on their friend's card. The user should not know they are in a game.",
        "options": [
            {
                "title": "Add yourself as user",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "creditScore",
                        "amount": 50
                    },
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 5
                    }
                ]
            },
            {
                "title": "Decline the opportunity",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 5
                    }

                ]
            }
        ]
},
{
"title": "Offered a Retail Store Credit Card",
        "description": "You're offered a retail store credit card with attractive discounts.",
        "prompt": "write a 2-3 sentence paragraph for a situation in which  the user has to decide whether or not they should accept this retail store credit card. The user should not know they are in a game.",
        "options": [
            {
                "title": "Accept the credit card",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "creditScore",
                        "amount": 50
                    },
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 5
                    }
                ]
            },
            {
                "title": "Decline the credit card",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 5
                    }

                ]
            }

        ]
},
{
"title": "Taking Out a Personal Loan",
        "description": "You're considering taking out a personal loan to consolidate debts and improve your credit score.",
        "prompt": "write a 2-3 sentence paragraph for a situation in which  the user has to decide whether or not they should take out a personal loan. The user should not know they are in a game.",
        "options": [
            {
                "title": "Take out the loan",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "creditScore",
                        "amount": 50
                    },
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 5
                    }
                ]
            },
            {
                "title": "Avoid additional debt",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 5
                    }

                ]
            }
        ]

},
{

"title": "Credit Report Error",
        "description": "You've been notified of an error on your credit report.",
        "prompt": "write a 2-3 sentence paragraph for a situation in which  the user has to decide whether or not they should correct this error. The user should not know they are in a game.",
        "options": [
            {
                "title": "Correct the error",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "creditScore",
                        "amount": 50
                    },
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 5
                    }
                ]
            },
            {
                "title": "Ignore the error",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 5
                    }

                ]
            }
        ]
},
{


"title": "Secured Credit Card",
        "description": "You're offered a secured credit card, which can help you rebuild your credit.",
        "prompt": "write a 2-3 sentence paragraph for a situation in which the user has to decide whether or not they will accept the secured credit card. The user should not know they are in a game.",
        "options": [
            {
                "title": "Accept the secured card",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "creditScore",
                        "amount": 50
                    },
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 5
                    }
                ]
            },
            {
                "title": "Decline the Secured Card",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 5
                    }

                ]
            }
        ]
},
{

"title": "Big-Ticket Purchase",
        "description": "You're deciding whether to use a credit card for a big-ticket purchase or opt for alternative financing with a personal loan..",
        "prompt": "write a 2-3 sentence paragraph for a situation in which the user has to decide whether or not they should use their credit card for a big-ticket purchase. The user should not know they are in a game.",
        "options": [
            {
                "title": "Use the credit card",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "creditCardPayments",
                        "amount": 500
                    },
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 5
                    }
                ]
            },
            {
                "title": "Alternative financing option",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 5
                    }

                ]
            }
        ]
},
{

"title": "Reached Credit Card Limit",
        "description": "You've reached your credit card limit and are considering requesting a credit limit increase to manage your monthly expenses better.",
        "prompt": "write a 2-3 sentence paragraph for a situation in which the user has to decide whether or not they should request an increased credit limit. The user should not know they are in a game.",
        "options": [
            {
                "title": "Request credit limit increase",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "creditCardPayments",
                        "amount": 500
                    },
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 5
                    }
                ]
            },
            {
                "title": "Maintain current credit limit",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 5
                    }

                ]
            }
        ]
},
{

"title": "Retail Store Credit Card",
        "description": "You've received an offer for a retail store credit card with enticing discounts for using it.",
        "prompt": "write a 2-3 sentence paragraph for a situation in which the user has to decide whether or not they should accept the retail store credit card. The user should not know they are in a game.",
        "options": [
            {
                "title": "Accept retail credit card",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "creditCardPayments",
                        "amount": 500
                    },
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 5
                    }
                ]
            },
            {
                "title": "Decline retail credit card",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 5
                    }

                ]
            }
        ]

},
{

"title": "Credit Report Statement Error",
        "description": "You've been notified of an error on your credit card statement that could lead to overpayment.",
        "prompt": "write a 2-3 sentence paragraph for a situation in which the user has to decide if they want to correct this error that could cause them to overpay. The user should not know they are in a game.",
        "options": [
            {
                "title": "Address this error",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "creditCardPayments",
                        "amount": 500
                    },
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 5
                    }
                ]
            },
            {
                "title": "Disregard the error",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 5
                    }

                ]
            }
        ]
},
{


"title": "Credit Card Rewards Program",
        "description": "Your credit card has a rewards program with an annual fee. You're debating whether to keep or cancel the card.",
        "prompt": "write a 2-3 sentence paragraph for a situation in which the user has to decide whether they want to keep the rewards program. The user should not know they are in a game.",
        "options": [
            {
                "title": "Keep the rewards program",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "creditCardPayments",
                        "amount": 500
                    },
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 5
                    }
                ]
            },
            {
                "title": "Cancel the card",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 5
                    }

                ]
            }
        ]
},
{


"title": "High Interest Credit Card Debt",
        "description": "You're at a crossroads with a high-interest credit card debt. You've received an offer for a lower-interest balance transfer.",
        "prompt": "write a 2-3 sentence paragraph for a situation in which the user has to decide whether or not they should choose a lower-interest balance transfer. The user should not know they are in a game.",
        "options": [
            {
                "title": "Choose lower-interest balance",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "creditCardPayments",
                        "amount": 500
                    },
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 5
                    }
                ]
            },
            {
                "title": "Continue high-interest card",
                "effect_on_player": [
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 5
                    }

                ]
            }
        ]
},
{
"title": "Credit Report Error",
        "description": "You've been notified of an error on your credit report.",
        "prompt": "write a 2-3 sentence paragraph for a situation in which  the user has to decide whether or not they should correct this error. The user should not know they are in a game.",
        "options": [
            {
                "title": "Correct the error",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "creditScore",
                        "amount": 50
                    },
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 5
                    }
                ]
            },
            {
                "title": "Ignore the error",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 5
                    }

                ]
            }
        ]
},
{

"title": "Credit Counseling Program",
        "description": "You're considering a credit counseling program that may help you manage your credit card debt and reduce monthly payments.",
        "prompt": "write a 2-3 sentence paragraph for a situation in which  the user has to decide whether or not they should partake in the credit counseling program. The user should not know they are in a game.",
        "options": [
            {
                "title": "Enroll in Credit Counseling",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "creditCardPayments", 
                        "amount": 500
                    },
                    {
                        "is_positive": False,
                        "attribute": "risk",
                        "amount": 5
                    },
                    {
                        "is_positive": True,
                        "attribute": "creditScore",
                        "amount": 5
                    }
                ]
            },
            {
                "title": "Manage Debt Independently",
                "effect_on_player": [
                    {
                        "is_positive": True,
                        "attribute": "risk",
                        "amount": 5
                    }

                ]
            }
        ]
},

    

    
]