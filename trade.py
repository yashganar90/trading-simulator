import random


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

    def show_prices(self):
        print("\n--- Market Prices ---")
        for stock in self.stocks.values():
            print(f"{stock.name}: ₹{stock.price:.2f}")


# ------------------ PORTFOLIO CLASS ------------------

class Portfolio:
    def __init__(self, cash):
        self.cash = cash
        self.holdings = {}

    def buy(self, market):
        stock_name = input("Select the stock you want to buy: ").upper()

        if stock_name not in market.stocks:
            print("Stock does not exist")
            return

        try:
            quantity = int(input("Enter quantity: "))
        except ValueError:
            print("Invalid quantity")
            return

        if quantity <= 0:
            print("Quantity must be positive")
            return

        stock = market.stocks[stock_name]
        cost = stock.price * quantity

        if cost > self.cash:
            print("Insufficient funds")
            return

        self.cash -= cost
        self.holdings[stock_name] = self.holdings.get(stock_name, 0) + quantity

        print(f"Bought {quantity} shares of {stock_name}")

    def sell(self, market):
        stock_name = input("Select the stock you want to sell: ").upper()

        if stock_name not in self.holdings:
            print("You do not own this stock")
            return

        try:
            quantity = int(input("Enter quantity to sell: "))
        except ValueError:
            print("Invalid quantity")
            return

        if quantity <= 0:
            print("Quantity must be positive")
            return

        if quantity > self.holdings[stock_name]:
            print("Cannot sell more than you own")
            return

        stock = market.stocks[stock_name]
        sell_value = stock.price * quantity

        self.cash += sell_value
        self.holdings[stock_name] -= quantity

        if self.holdings[stock_name] == 0:
            del self.holdings[stock_name]

        print(f"Sold {quantity} shares of {stock_name}")

    def show_portfolio(self, market):
        print(f"\nCash Available: ₹{self.cash:.2f}")
        print("\n--- Portfolio ---")

        portfolio_value = 0

        if not self.holdings:
            print("No holdings")
        else:
            for stock_name, qty in self.holdings.items():
                current_price = market.stocks[stock_name].price
                total_value = qty * current_price
                portfolio_value += total_value

                print(f"{stock_name}: {qty} shares | ₹{current_price:.2f} each | Total: ₹{total_value:.2f}")

        total_assets = self.cash + portfolio_value

        print(f"\nPortfolio Value: ₹{portfolio_value:.2f}")
        print(f"Total Assets: ₹{total_assets:.2f}")

        return total_assets


# ------------------ MAIN PROGRAM ------------------

market = Market()
market.add_stock("HDFC", 2000)
market.add_stock("TATA", 4600)
market.add_stock("RELIANCE", 6000)

player = Portfolio(10000)

round_count = 0
game_over = False

while round_count < 10 and not game_over:
    print(f"\n======== ROUND {round_count + 1} ========")

    market.show_prices()
    player.show_portfolio(market)

    while True:
        try:
            choice = int(input("\n1 = Buy | 2 = Sell | 3 = End Round | 4 = Complete Game\nSelect: "))
        except ValueError:
            print("Invalid choice")
            continue

        if choice == 4:
            game_over = True
            break

        elif choice == 3:
            break

        elif choice == 1:
            player.buy(market)
            player.show_portfolio(market)

        elif choice == 2:
            player.sell(market)
            player.show_portfolio(market)

        else:
            print("Invalid option")

    if not game_over:
        market.update_market()
        round_count += 1


# ------------------ FINAL RESULTS ------------------

final_assets = player.show_portfolio(market)
roi = ((final_assets - 10000) / 10000) * 100

print("\n========= GAME OVER =========")
print(f"ROI: {roi:.2f}%")