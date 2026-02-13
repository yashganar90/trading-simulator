# Trading Simulator Lite

A simple command line stock market simulator built in Python.

This project simulates basic trading mechanics using virtual money, dynamic stock prices, and portfolio tracking.

---

## Features

- Virtual starting capital of ₹10,000
- Random stock price fluctuations each round
- Buy and sell functionality
- Portfolio tracking with live valuation
- Cash balance tracking
- Total asset calculation
- ROI percentage calculation
- 10 round game limit

---

## How It Works

Each round:

1. Stock prices update randomly within a ±5% range
2. Current market prices are displayed
3. User chooses to buy, sell, or end the game
4. Portfolio and cash are updated accordingly

At the end of 10 rounds, the simulator calculates:

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

```
python trade.py
```

---

## Concepts Used

- Dictionaries for market and portfolio storage
- Functions for modular transaction handling
- Random module for market simulation
- Conditional logic for validation
- Loop control for round management

---

## Future Improvements

- Save trade history to a file
- Add multiple stocks dynamically
- Implement volatility levels
- Convert to class-based architecture
- Add graphical interface

---

## Author

Yash Ganar
