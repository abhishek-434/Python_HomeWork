# a = int(input("Enter the decimal value: "))

# print(bin(a),"in binary")


num = float(input("Enter a decimal number: "))
binary = ""

if num == 0:
    binary = "0"
else:
    while num > 0:
        remainder = num % 2
        binary = str(remainder) + binary
        num = num // 2
print("Binary number:", binary)