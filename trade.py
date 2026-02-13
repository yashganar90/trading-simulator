import random

stock_list = {
    "HDFC": 2000,
    "TATA": 4600,
    "RELIANCE": 6000
}

def update_market():
    for stock in stock_list:
        change_percent = random.uniform(-0.05, 0.05)
        stock_list[stock] *= (1 + change_percent)

        if stock_list[stock] < 1:
            stock_list[stock] = 1


def show_market(cash, portfolio):
    print("\n--- Market Prices ---")
    for stock, price in stock_list.items():
        print(f"{stock}: ₹{price:.2f}")

    print(f"\nCash Available: ₹{cash:.2f}")

    print("\n--- Portfolio ---")
    portfolio_value = 0

    if not portfolio:
        print("No holdings")
    else:
        for stock, qty in portfolio.items():
            current_price = stock_list[stock]
            total_value = qty * current_price
            portfolio_value += total_value

            print(f"{stock}: {qty} shares | ₹{current_price:.2f} each | Total: ₹{total_value:.2f}")

    total_assets = cash + portfolio_value

    print(f"\nPortfolio Value: ₹{portfolio_value:.2f}")
    print(f"Total Assets: ₹{total_assets:.2f}")



def buy(cash, portfolio):
    stock = input("Select the stock you want to buy: ").upper()

    if stock not in stock_list:
        print("Stock does not exist")
        return cash, portfolio

    try:
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Invalid quantity")
        return cash, portfolio

    if quantity <= 0:
        print("Quantity must be positive")
        return cash, portfolio

    price = stock_list[stock]
    cost = price * quantity

    if cost > cash:
        print("Insufficient funds")
        return cash, portfolio

    cash -= cost

    if stock in portfolio:
        portfolio[stock] += quantity
    else:
        portfolio[stock] = quantity

    print(f"Bought {quantity} shares of {stock}")
    return cash, portfolio


def sell(cash, portfolio):
    stock = input("Select the stock you want to sell: ").upper()

    if stock not in portfolio:
        print("You do not own this stock")
        return cash, portfolio

    try:
        quantity = int(input("Enter quantity to sell: "))
    except ValueError:
        print("Invalid quantity")
        return cash, portfolio

    if quantity <= 0:
        print("Quantity must be positive")
        return cash, portfolio

    if quantity > portfolio[stock]:
        print("Cannot sell more than you own")
        return cash, portfolio

    price = stock_list[stock]
    sell_value = price * quantity

    cash += sell_value
    portfolio[stock] -= quantity

    if portfolio[stock] == 0:
        del portfolio[stock]

    print(f"Sold {quantity} shares of {stock}")
    return cash, portfolio


# ------------------ MAIN PROGRAM ------------------

portfolio = {}
cash = 10000
round_count = 0

while round_count < 10:
    print(f"\n======== ROUND {round_count + 1} ========")

    update_market()
    show_market(cash, portfolio)

    try:
        choice = int(input("\n1 = Buy | 2 = Sell | 3 = End Game\nSelect: "))
    except ValueError:
        print("Invalid choice")
        continue

    if choice == 3:
        break
    elif choice == 1:
        cash, portfolio = buy(cash, portfolio)
    elif choice == 2:
        cash, portfolio = sell(cash, portfolio)
    else:
        print("Invalid option")
        continue

    round_count += 1


# --------- FINAL CALCULATIONS ---------

portfolio_value = 0
for stock in portfolio:
    portfolio_value += portfolio[stock] * stock_list[stock]

total_assets = cash + portfolio_value
roi = ((total_assets - 10000) / 10000) * 100

print("\n========= GAME OVER =========")
print(f"Final Portfolio Value: ₹{portfolio_value:.2f}")
print(f"Final Cash: ₹{cash:.2f}")
print(f"Total Assets: ₹{total_assets:.2f}")
print(f"ROI: {roi:.2f}%")
