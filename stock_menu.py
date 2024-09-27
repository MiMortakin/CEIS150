# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 22:57:11 2021
@author: D99003734
"""

#Name: Michelle Buchholz
#Class: CEIS150 - Sep 2024 Session
#Date: 

from datetime import datetime
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

          option = input("Press 'Enter' to add another stock or '0' to Stop")


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
    print("This method is under construction")

# Display Chart
def display_chart(stock_list):
    print("This method is under construction")
  


                
 # Get price and volume history from Yahoo! Finance using CSV import.
def import_stock_csv(stock_list):
    print("This method is under construction")
    
   # Display Report 
def display_report(stock_list):
    print("This method is under construction")
    
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