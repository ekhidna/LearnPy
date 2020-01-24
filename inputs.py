name = input("Enter your name: ")
quantity = int(input("How many items? "))
price = float(input("Cost per item? "))
total = quantity * price
print("You entered the name: ", name)
print("You entered ", quantity, " number of items")
print("You entered a price of ", price, "$ for each item")
print("The total cost of the items is ", total, "$")