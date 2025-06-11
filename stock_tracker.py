# Stock Portfolio Tracker
# This program calculates the total investment based on user input and hardcoded stock prices.

# Hardcoded dictionary of stock prices (USD)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2800,
    "MSFT": 330,
    "AMZN": 3500
}

# Dictionary to store user portfolio
portfolio = {}

# Welcome message
print("📈 Welcome to the Stock Portfolio Tracker!\n")
print("Available stocks:", ', '.join(stock_prices.keys()))

# Input loop
while True:
    stock = input("\nEnter stock symbol (or 'done' to finish): ").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print("❌ Stock not found. Try again.")
        continue
    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("❌ Invalid quantity. Please enter a number.")

# Calculate total investment
print("\n📊 Your Portfolio Summary:")
total_value = 0
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = qty * price
    total_value += value
    print(f"{stock}: {qty} shares x ${price} = ${value}")

print(f"\n💰 Total Investment: ${total_value}")

# Optional: Save to file
save = input("\nDo you want to save this to a file? (yes/no): ").lower()
if save == 'yes':
    file_format = input("Choose file format - 'txt' or 'csv': ").lower()
    filename = f"portfolio.{file_format}"
    with open(filename, "w") as f:
        if file_format == 'txt':
            for stock, qty in portfolio.items():
                f.write(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${qty * stock_prices[stock]}\n")
            f.write(f"\nTotal Investment: ${total_value}")
        elif file_format == 'csv':
            f.write("Stock,Quantity,Price,Total\n")
            for stock, qty in portfolio.items():
                f.write(f"{stock},{qty},{stock_prices[stock]},{qty * stock_prices[stock]}\n")
            f.write(f"\n,,Total,{total_value}")
    print(f"✅ Portfolio saved to '{filename}'")

print("\n✅ Thank you for using Stock Portfolio Tracker!")