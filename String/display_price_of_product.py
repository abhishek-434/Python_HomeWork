product = input("Enter product name: ")
price = input("Enter price: ")

total_length = 25
dots = total_length - (len(product) + len(price))

result = product + '.' * dots + price
print(result)
