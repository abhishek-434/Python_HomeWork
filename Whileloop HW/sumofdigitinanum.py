# i = 345
# sum = 0

# while i>0:
#     sum=sum+i%10
#     i//=10
# print("Sum of digit: ",sum)   

i = int(input("Enter number: "))
sum = 0

while i>0:
    sum = sum + i % 10
    i //= 10
print("Sum of digit: ",sum)