#Name: Michelle Buchholz
#Date: 9/2/2024
#Class: CEIS150

# initialize the count variable to 0
# initialize the sum variable to 0
count = 0
sum = 0

# input full_name
name = input("What is your name: ")

# input the min_price and convert it to float
min_price = float(input("What is the minimum price: "))

# create a list of prices example: price_list = [69.0, 71.0, 84.5, 91.0, 67.4, 81.2, 84.6, 58.8,79.3, 101.2]
price_list = [69.0, 71.0, 84.5, 91.0, 67.4, 81.2, 84.6, 58.8, 79.3, 101.2]

# for price in price_list
# add current price to sum
# if price > min_price
# increment count by 1

for price in price_list:
    sum += price
    if price > min_price:
        count += 1


# output "Hello",name,"the minimum price is ",min_price
# output "There are ",count,"prices greater than the minimum price"
# output "The total price is ",sum

print("Hello",name, "the minimum prince is ",min_price)
print("there are ",count,"prices greater than the minimum price")
print("The total price is ",sum)