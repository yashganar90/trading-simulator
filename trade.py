import tkinter as tk
import random
import csv


# ------------------ STOCK CLASS ------------------

class Stock:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def update_price(self):
        change_percent = random.uniform(-0.05, 0.05)
        self.price *= (1 + change_percent)
        if self.price < 1:
            self.price = 1


# ------------------ MARKET CLASS ------------------

class Market:
    def __init__(self):
        self.stocks = {}

    def add_stock(self, name, price):
        self.stocks[name] = Stock(name, price)

    def update_market(self):
        for stock in self.stocks.values():
            stock.update_price()


# ------------------ PORTFOLIO CLASS ------------------

class Portfolio:
    def __init__(self, cash):
        self.cash = cash
        self.holdings = {}
        self.trade_history = []

    def buy(self, stock_name, quantity, market, round_num):
        if stock_name not in market.stocks:
            return False, "Stock does not exist", 0

        if quantity <= 0:
            return False, "Quantity must be positive", 0

        stock = market.stocks[stock_name]
        cost = stock.price * quantity

        if cost > self.cash:
            return False, "Insufficient funds", 0

        self.cash -= cost
        self.holdings[stock_name] = self.holdings.get(stock_name, 0) + quantity

        self.trade_history.append({
            "type": "BUY",
            "stock": stock_name,
            "qty": quantity,
            "price": stock.price,
            "round": round_num
        })

        return True, f"Bought {quantity} {stock_name} for ₹{cost:.2f}", cost

    def sell(self, stock_name, quantity, market, round_num):
        if stock_name not in self.holdings:
            return False, "You do not own this stock", 0

        if quantity <= 0:
            return False, "Quantity must be positive", 0

        if quantity > self.holdings[stock_name]:
            return False, "Cannot sell more than you own", 0

        stock = market.stocks[stock_name]
        value = stock.price * quantity

        self.cash += value
        self.holdings[stock_name] -= quantity

        if self.holdings[stock_name] == 0:
            del self.holdings[stock_name]

        self.trade_history.append({
            "type": "SELL",
            "stock": stock_name,
            "qty": quantity,
            "price": stock.price,
            "round": round_num
        })

        return True, f"Sold {quantity} {stock_name} for ₹{value:.2f}", value

    def calculate_values(self, market):
        portfolio_value = 0
        for name, qty in self.holdings.items():
            portfolio_value += qty * market.stocks[name].price

        total_assets = self.cash + portfolio_value
        return portfolio_value, total_assets

    def save_history(self):
        with open("trade_history.csv", "w", newline="") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["type", "stock", "qty", "price", "round"]
            )
            writer.writeheader()
            writer.writerows(self.trade_history)


# ------------------ GUI APPLICATION ------------------

class TradingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Trading Simulator")

        self.market = Market()
        self.market.add_stock("HDFC", 2000)
        self.market.add_stock("TATA", 4600)
        self.market.add_stock("RELIANCE", 6000)

        self.portfolio = Portfolio(10000)
        self.round = 1

        self.create_widgets()
        self.update_display()

    def create_widgets(self):
        self.market_label = tk.Label(self.root, text="", justify="left")
        self.market_label.pack(pady=5)

        self.portfolio_label = tk.Label(self.root, text="", justify="left")
        self.portfolio_label.pack(pady=5)

        tk.Label(self.root, text="Stock Name").pack()
        self.stock_entry = tk.Entry(self.root)
        self.stock_entry.pack()

        tk.Label(self.root, text="Quantity").pack()
        self.qty_entry = tk.Entry(self.root)
        self.qty_entry.pack()

        tk.Button(self.root, text="Buy", command=self.buy_stock).pack(pady=2)
        tk.Button(self.root, text="Sell", command=self.sell_stock).pack(pady=2)
        tk.Button(self.root, text="End Round", command=self.end_round).pack(pady=2)
        tk.Button(self.root, text="Save Trade History", command=self.save_history).pack(pady=5)

        self.status_label = tk.Label(self.root, text="", fg="blue")
        self.status_label.pack(pady=5)

    def update_display(self):
        market_text = f"Round: {self.round}\n\n--- Market Prices ---\n"
        for stock in self.market.stocks.values():
            market_text += f"{stock.name}: ₹{stock.price:.2f}\n"

        portfolio_value, total_assets = self.portfolio.calculate_values(self.market)

        portfolio_text = (
            f"\n--- Portfolio ---\n"
            f"Cash: ₹{self.portfolio.cash:.2f}\n"
            f"Portfolio Value: ₹{portfolio_value:.2f}\n"
            f"Total Assets: ₹{total_assets:.2f}\n\n"
        )

        for name, qty in self.portfolio.holdings.items():
            portfolio_text += f"{name}: {qty} shares\n"

        self.market_label.config(text=market_text)
        self.portfolio_label.config(text=portfolio_text)

    def buy_stock(self):
        stock = self.stock_entry.get().upper()

        try:
            qty = int(self.qty_entry.get())
        except ValueError:
            self.status_label.config(text="Invalid quantity", fg="red")
            return

        success, msg, amount = self.portfolio.buy(stock, qty, self.market, self.round)

        if success:
            self.status_label.config(text=msg, fg="green")
        else:
            self.status_label.config(text=msg, fg="red")

        self.update_display()

    def sell_stock(self):
        stock = self.stock_entry.get().upper()

        try:
            qty = int(self.qty_entry.get())
        except ValueError:
            self.status_label.config(text="Invalid quantity", fg="red")
            return

        success, msg, amount = self.portfolio.sell(stock, qty, self.market, self.round)

        if success:
            self.status_label.config(text=msg, fg="green")
        else:
            self.status_label.config(text=msg, fg="red")

        self.update_display()

    def end_round(self):
        self.market.update_market()
        self.round += 1
        self.status_label.config(text="Round ended. Prices updated.", fg="blue")
        self.update_display()

    def save_history(self):
        self.portfolio.save_history()
        self.status_label.config(text="Trade history saved to trade_history.csv", fg="blue")


# ------------------ RUN APPLICATION ------------------

root = tk.Tk()
app = TradingApp(root)
root.mainloop()