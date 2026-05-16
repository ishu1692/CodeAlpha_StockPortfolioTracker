import csv

# ===============================
# Stock Portfolio Tracker
# ===============================

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 320,
    "AMZN": 150
}

portfolio = {}
total_investment = 0

print("=" * 45)
print("📈 STOCK PORTFOLIO TRACKER 📈")
print("=" * 45)

# Display available stocks
print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock} : ${price}")

# Number of stocks user wants to add
num_stocks = int(input("\nHow many stocks do you want to add? "))

# User input loop
for i in range(num_stocks):

    print(f"\nStock #{i + 1}")

    stock_name = input("Enter stock symbol: ").upper()

    # Check valid stock
    if stock_name not in stock_prices:
        print("❌ Stock not available.")
        continue

    quantity = int(input("Enter quantity: "))

    # Calculate investment
    investment = stock_prices[stock_name] * quantity

    # Store data
    portfolio[stock_name] = {
        "quantity": quantity,
        "price": stock_prices[stock_name],
        "investment": investment
    }

    total_investment += investment

# Display portfolio summary
print("\n" + "=" * 45)
print("📊 PORTFOLIO SUMMARY")
print("=" * 45)

for stock, details in portfolio.items():
    print(
        f"{stock} | Quantity: {details['quantity']} | "
        f"Price: ${details['price']} | "
        f"Investment: ${details['investment']}"
    )

print("\n💰 Total Investment Value: $", total_investment)

# Save to CSV file
save_file = input("\nDo you want to save the portfolio to CSV? (yes/no): ").lower()

if save_file == "yes":

    with open("portfolio.csv", "w", newline="") as file:
        writer = csv.writer(file)

        # Header
        writer.writerow(["Stock", "Quantity", "Price", "Investment"])

        # Data rows
        for stock, details in portfolio.items():
            writer.writerow([
                stock,
                details["quantity"],
                details["price"],
                details["investment"]
            ])

    print("✅ Portfolio saved as 'portfolio.csv'")

print("\n🎯 Thank you for using Stock Portfolio Tracker!")