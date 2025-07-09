num = int(input("Enter a number: "))
fact = 1

if num<0:
    print("factorial of 0 is not exist")
if num==0:
    print("factorial of 0 is", 1) 
if num>0:
    for i in range (1,num+1):
        fact=fact*i
print("the factorial is", fact) 
              
