# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 22:57:11 2021
@author: D99003734
"""

#Name: Michelle Buchholz
#Class: CEIS150 - Sep 2024 Session
#Date: 

from datetime import datetime
from venv import create
from stock_class import Stock, DailyData
from account_class import  Traditional, Robo
import matplotlib.pyplot as plt
import csv

# Adding Stock to Stock List
def add_stock(stock_list):
      option = ""
      while option != "0":
          print("\n=== Add Stocks ===")

          symbol = input("Enter the Stock Symbol: ").upper()
          name = input("Enter the Company Name: ")
          shares = float(input("Enter the Number of Shares: "))

          new_stock = Stock(symbol, name, shares)
          stock_list.append(new_stock)

          option = input("Press 'Enter' to add another stock or '0' to Stop: ")
print()


# Remove stock and all daily data
def delete_stock(stock_list):
    print("\n=== Delete Stock ===")

    if not stock_list:
        print("There are No Stocks Available to Delete.")
    else: # Will display the stock symbols in list format
        print("Stock List: [", end="")
        for stock in stock_list:
            print(stock.symbol, end=" ")
        print("]")

        symbol = input("Enter the stock symbol you wish to delte: ").upper()
        found = False
        i = 0

        #loop through the stocks to find the symbol
        for stock in stock_list:
            if stock.symbol == symbol:
                found = True
                stock_list.pop(i)
                break
            i += 1

        if found:
            print(f"Deleted {symbol}")
        else:
            print(f"Error: Stock Symbol {symbol} was not found.")

    input("\nPress 'Enter' to Continue...")
    
    
# List stocks being tracked
def list_stocks(stock_list):
    print("\n=== Stock List ===")
    print(f"{'Symbol' :<10} {'Company Name' :<25} {'Shares' :<10}")
    print("="*45)

    if not stock_list:
        print("You have not entered any stocks yet.")
    else:
        for stock in stock_list:
            print(f"{stock.symbol:<10} {stock.name:<25} {stock.shares:<10.2f}")

    input("\nPress 'Enter' to Continue...")
    
    # Add Daily Stock Data
def add_stock_data(stock_list):
   print("\n=== Add Daily Stock Data ===")

   if not stock_list:
       print("No Stocks Currently Available.")
       return
   
   #Display the stocks in a list format
   print("Stock List: [", end="")
   for stock in stock_list:
       print(stock.symbol, end=" ")
   print("]")

   symbol = input("Enter the Stock Symbol to Add Daily Data for: ").upper()
   stock_found = None

   #Look for Stock by Symbol
   for stock in stock_list:
       if stock.symbol == symbol:
           stock_found = stock
           break
       
   if stock_found:
       print(f"Adding Daily Data for {stock_found.symbol} ({stock_found.name})")
       while True:
           data = input("Enter Date(MM/DD/YY), Closing Price, and Volume (or press 'Enter' to Stop): ")

           if not data: # Stopping on blank input
               break
           
           try:
               date, price, volume = data.split(",")
               daily_data = DailyData(datetime.strptime(date.strip(), "%m/%d/%y"),
                                      float(price.strip()), float(volume.strip()))
               stock_found.add_data(daily_data)
               print(f"Added: {daily_data.date.strftime('%m/%d/%y')} - Price: {daily_data.close}, Volume: {daily_data.volume}")
           except ValueError:
               print("Invalid Input. Please ensure the format is MM/DD/YY, Price, and Volume")
   else:
       print(f"Error: Stock Symbol {symbol} was not found.")

   input("\nPress 'Enter' to Continue...")
       
    
def investment_type(stock_list):
    print("Investment Account ---")
    balance = float(input("What is your initial balance: "))
    number = input("What is your account number: ")
    acct= input("Do you want a Traditional (t) or Robo (r) account: ")
    if acct.lower() == "r":
        years = float(input("How many years until retirement: "))
        robo_acct = Robo(balance, number, years)
        print("Your investment return is ",robo_acct.investment_return())
        print("\n\n")
    elif acct.lower() == "t":
        trad_acct = Traditional(balance, number)
        temp_list=[]
        print("Choose stocks from the list below: ")
        while True:
            print("Stock List: [",end="")
            for stock in stock_list:
                print(stock.symbol," ",end="")
            print("]")
            symbol = input("Which stock do you want to purchase, 0 to quit: ").upper()
            if symbol =="0":
                break
            shares = float(input("How many shares do you want to buy?: "))
            found = False
            for stock in stock_list:
              if stock.symbol == symbol:
                  found = True
                  current_stock = stock
            if found == True:
                current_stock.shares += shares 
                temp_list.append(current_stock)
                print("Bought ",shares,"of",symbol)
            else:
                print("Symbol Not Found ***")
        trad_acct.add_stock(temp_list)


# Function to create stock chart
def display_stock_chart(stock_list,symbol):

#Creates lists for date, price, volume
    date = []
    price = []
    volume = []
    company = ""

# Loops through the stock_list to find stock by symbol
    for stock in stock_list:
        if stock.symbol == symbol: 
            company = stock.name
# Loops through the daily data of the stock
            for dailyData in stock.DataList:
                date.append(dailyData.date)
                price.append(dailyData.close)
                volume.append(dailyData.volume)

#Plotting 
    plt.plot(date, price)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(company)
    plt.show()

# Display Chart
def display_chart(stock_list):
# Output the stock list
    print("Stock List: [", end="")
    for stock in stock_list:
        print(stock.symbol + " ", end="")
    print("]")
  
# Input symbol from user
    symbol = input("Enter Stock Symbol: ").upper()

#Initialize found as False
    found = False
    current_stock = None

#Search for stock by symbol
    for stock in stock_list:
        if stock.symbol == symbol:
            found = True
            current_stock = stock
            break

# If the stock is found, displays chart
    if found:
        display_stock_chart(stock_list, symbol)
    else: 
        print(f"Error: Stock Symbol '{symbol}' not Found.")

# Pause and Prompt User for Enter to Continue
    input("Press Enter to Continue....")

                
 # Get price and volume history from Yahoo! Finance using CSV import. - I used Google Finance & Sheets
def import_stock_csv(stock_list):
    print("\n=== Import Stock ===")
    
    # Display available stocks
    print("Stock List: [", end="")
    for stock in stock_list:
        print(stock.symbol, end=" ")
    print("]")

    # Input for symbol and filename
    symbol = input("Please Enter the stock symbol: ").upper()
    filename = input("Please Enter the Filename (including the .csv): ")

    # Attempt to find the stock in the stock list
    stock_found = None
    for stock in stock_list:
        if stock.symbol == symbol:
            stock_found = stock
            break
    
    if stock_found is None:
        print(f"Error: Stock Symbol '{symbol}' not found in stock list.")
        return

    # Try to open the file and read data
    try:
        print(f"Attempting to open file: {filename}")
        with open(filename, mode='r') as stockdata:
            datareader = csv.reader(stockdata, delimiter=',')
            next(datareader)  # Skip the header row
            
            for row in datareader:
                if len(row) < 7:  # Check if the row has enough columns
                    print("Warning: Row does not contain enough columns, skipping row.")
                    continue
                
                # Create DailyData object
                daily_data = DailyData(
                    datetime.strptime(row[0], "%Y/%m/%d"),
                    float(row[4]),
                    float(row[6])
                )
                stock_found.add_data(daily_data)
                print(f"Added data for {daily_data.date.strftime('%Y/%m/%d')} - Price: {daily_data.close}, Volume: {daily_data.volume}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error has occurred: {str(e)}")

    # Optionally call the display_report function to show the updated data
    display_report(stock_list)

    
   # Display Report 
def display_report(stock_list):
    print("\n=== Stock Report ===")
    
    # Loop through each stock in stock_list
    for stock in stock_list:
        print(f"Report for: {stock.symbol} - {stock.name}")
        print(f"Shares: {stock.shares}")
        
        # Initialize variables for summary
        count = 0
        price_total = 0
        volume_total = 0
        lowPrice = 999999.99
        highPrice = 0
        lowVolume = 999999999999
        highVolume = 0
        startPrice = 0
        endPrice = 0
        
        # Check if there is any historical data for the stock
        if not stock.DataList:
            print("No daily history available")
        else:
            # Loop through daily data
            for i, daily_data in enumerate(stock.DataList):
                count += 1
                price_total += daily_data.close
                volume_total += daily_data.volume
                
                # Set starting price (first day)
                if i == 0:
                    startPrice = daily_data.close
                
                # Set ending price (latest day)
                endPrice = daily_data.close
                
                # Compare and update low/high prices and volumes
                if daily_data.close < lowPrice:
                    lowPrice = daily_data.close
                if daily_data.close > highPrice:
                    highPrice = daily_data.close
                if daily_data.volume < lowVolume:
                    lowVolume = daily_data.volume
                if daily_data.volume > highVolume:
                    highVolume = daily_data.volume

            # Calculate price change and profit/loss
            priceChange = endPrice - startPrice
            profit_or_loss = priceChange * stock.shares
            
            # Output summary information
            print("Summary ---")
            print("Low Price:", "${:,.2f}".format(lowPrice))
            print("High Price:", "${:,.2f}".format(highPrice))
            print("Average Price:", "${:,.2f}".format(price_total / count))
            print("Low Volume:", "{:,}".format(lowVolume))
            print("High Volume:", "{:,}".format(highVolume))
            print("Average Volume:", "{:,}".format(volume_total // count))
            print("Change in Price:", "${:,.2f}".format(priceChange))
            print("Profit/Loss:", "${:,.2f}".format(profit_or_loss))
        
        # Print blank lines to separate reports for each stock
        print("\n" + "-" * 40 + "\n")
    
    print("Report Complete")
    input("Press Enter to continue...")


    
def main_menu(stock_list):
    option = ""
    while True:
        print("Stock Analyzer ---")
        print("1 - Add Stock")
        print("2 - Delete Stock")
        print("3 - List stocks")
        print("4 - Add Daily Stock Data (Date, Price, Volume)")
        print("5 - Show Chart")
        print("6 - Investor Type")
        print("7 - Load Data")
        print("0 - Exit Program")
        option = input("Enter Menu Option: ")
        if option =="0":
            print("Goodbye")
            break
        
        if option == "1":
            add_stock(stock_list)
        elif option == "2":
            delete_stock(stock_list)
        elif option == "3":
            list_stocks(stock_list)
        elif option == "4":
           add_stock_data(stock_list) 
        elif option == "5":
            display_chart(stock_list)
        elif option == "6":
            investment_type(stock_list)
        elif option == "7":
            import_stock_csv(stock_list)
        else:
            
            print("Goodbye")

# Begin program
def main():
    stock_list = []
    main_menu(stock_list)

# Program Starts Here
if __name__ == "__main__":
    # execute only if run as a stand-alone script
    main()