import yfinance as yf

# Define the ticker symbol for Apple stock
ticker_symbol = "AAPL"

# Get the data for the stock using the Yahoo Finance API
apple_stock = yf.Ticker(ticker_symbol)

# Define a function to get the current price of the stock
def get_price():
    data = apple_stock.history(period="1d")
    price = data["Close"].iloc[-1]
    return price

# Define a function to compare the price changes over a certain period of time
def compare_prices(num_minutes):
    initial_price = get_price()
    time.sleep(num_minutes * 60)
    final_price = get_price()
    price_difference = final_price - initial_price
    price_change_percentage = (price_difference / initial_price) * 100
    return price_change_percentage

# Test the function by comparing the price changes over the past 5 minutes
price_change_percentage = compare_prices(5)
print(f"The price change percentage over the past 5 minutes is {price_change_percentage:.2f}%")
