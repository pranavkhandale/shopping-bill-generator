print("<-------SHOPPING BILL------->")
names = []
prices = []

n = int(input("How many items?: "))

total_bill = 0

for i in range(n):
    name = input("Enter the item name you have buy: ")
    price = float(input("Enter the price of the item you have buy: "))

    names.append(name)
    prices.append(price)
    total_bill += prices[i]
    print()


maximum_price = prices[0]
maximum_price_item_name = ""

minimum_price = prices[0]
minimum_price_item_name = ""

for i in range(n):
    if prices[i] > maximum_price:
        maximum_price_item_name = names[i]
        maximum_price = prices[i]

    elif prices[i] < minimum_price:
        minimum_price_item_name = names[i]
        minimum_price = prices[i]

print(f"The total bill of items you have buy is {total_bill}")
print(f"The maximum price item you have buy is {maximum_price_item_name}and which is about {maximum_price}.rs")
print(f"The minimum price item you have buy is {minimum_price_item_name} and which is about {minimum_price}.rs")

