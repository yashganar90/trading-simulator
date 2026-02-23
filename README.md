# Trading Simulator Lite

A GUI-based stock market simulator built in Python using object-oriented design and tkinter.

This project simulates basic trading mechanics using virtual money, dynamic stock prices, portfolio tracking, and trade history export.

---

## Features

- Virtual starting capital of ₹10,000
- Multiple stocks available for trading
- Random stock price fluctuations (±5%) per round
- Interactive tkinter graphical interface
- Buy and sell functionality with live updates
- Real-time cash balance display
- Live portfolio value calculation
- Total asset tracking
- Trade history tracking
- Export trade history to CSV file

---

## How It Works

- Market prices are displayed inside the GUI
- User enters stock name and quantity
- Buy and Sell buttons execute trades instantly
- Cash, portfolio value, and total assets update in real time
- End Round updates stock prices
- Save Trade History exports all transactions to `trade_history.csv`

The application uses event-driven programming instead of a command line loop.

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

The GUI window will open.

---

## Concepts Used

- Object-Oriented Programming (OOP)
- Classes and Objects (Stock, Market, Portfolio)
- Encapsulation and separation of concerns
- Event-driven programming with tkinter
- Dictionaries for holdings storage
- Random module for market simulation
- CSV file handling for data export

---

## Future Improvements

- Implement advanced volatility models
- Add graphical stock price charts
- Improve GUI layout and styling

---

## Author

Yash Ganar
