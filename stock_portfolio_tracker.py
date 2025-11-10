import csv

# Step 1: Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 130,
    "MSFT": 400
}

# Step 2: User input
portfolio = {}
num_stocks = int(input("How many stocks do you want to add? "))

for i in range(num_stocks):
    stock_name = input(f"Enter stock name (e.g., AAPL, TSLA): ").upper()
    quantity = int(input(f"Enter quantity of {stock_name}: "))
    portfolio[stock_name] = quantity

# Step 3: Calculate total value
total_value = 0

for stock, qty in portfolio.items():
    if stock in stock_prices:
        total_value += stock_prices[stock] * qty
    else:
        print(f"Stock {stock} not found in price list.")

# Step 4: Display
print("\nYour Portfolio Summary:")
for stock, qty in portfolio.items():
    if stock in stock_prices:
        print(f"{stock}: {qty} *${stock_prices[stock]} = ${stock_prices[stock] * qty}")

print(f"\n Total Investment Value: ${total_value}")

# Step 5: Save to file
with open("portfolio.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Stock", "Quantity", "Price", "Value"])
    for stock, qty in portfolio.items():
        if stock in stock_prices:
            writer.writerow([stock, qty, stock_prices[stock], stock_prices[stock] * qty])
    writer.writerow(["Total", "", "", total_value])

print("\n Portfolio saved to portfolio.csv")
