n = int(input("Enter a number: "))
sum = 0

while n > 0:
    digit = n % 10
    if digit > sum:
        sum = digit
    n = n // 10
print("The maximum digit is:", sum)