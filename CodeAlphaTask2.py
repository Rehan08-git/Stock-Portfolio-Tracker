stocks = {"AAPL": 180, "TSLA": 250, "GOOG": 2700, "AMZN": 3300}

total_investment = 0


print("Stock Portfolio Tracker")


while True:

    stock_name = input("Enter stock name (or 'exit' to stop): ").upper()


    
    if stock_name == "EXIT":
        break
    
    if stock_name in stocks:
        quantity = int(input("Enter quantity: "))
        value = stocks[stock_name] * quantity
        total_investment += value
        print(f"Added {stock_name}: {value}")

    else:
        print("Stock not found!")


print("\nTotal Investment Value:", total_investment)


save = input("Do you want to save result to file? (y/n): ").lower()


if save == 'y':
    file = open("portfolio.txt", "w")
    file.write(f"Total Investment Value: {total_investment}")
    file.close()
    print("Data saved to portfolio.txt")
