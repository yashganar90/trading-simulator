# Trading Simulator Lite

A command line stock market simulator built in Python using object-oriented design.

This project simulates basic trading mechanics using virtual money, dynamic stock prices, and portfolio tracking.

---

## Features

- Virtual starting capital of ₹10,000
- Multiple stocks available for trading
- Random stock price fluctuations (±5%) per round
- Multiple buy and sell transactions per round
- Option to end a round manually
- Option to complete the game early
- Portfolio tracking with live valuation
- Cash balance tracking
- Total asset calculation
- ROI percentage calculation
- 10 round maximum game limit

---

## How It Works

Each round:

1. Current market prices are displayed
2. User can perform multiple buy/sell transactions
3. User can end the round manually
4. After the round ends, stock prices update randomly

The game can also be completed early using the "Complete Game" option.

At the end of the game, the simulator calculates:

- Final portfolio value
- Remaining cash
- Total assets
- ROI percentage

---

## Project Structure

```
trading-simulator/
│
├── trade.py
└── README.md
```

---

## How To Run

1. Make sure Python is installed.
2. Open terminal in the project directory.
3. Run:

python trade.py

---

## Concepts Used

- Object-Oriented Programming (OOP)
- Classes and Objects (Stock, Market, Portfolio)
- Encapsulation and separation of concerns
- Dictionaries for holdings storage
- Random module for market simulation
- Conditional validation logic
- Nested loops for round control

---

## Future Improvements

- Save trade history to a file
- Implement advanced volatility models
- Add graphical interface

---

## Author

Yash Ganar
