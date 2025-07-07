'''n = int(input("Enter a number: "))

if n==1:
    print('January')
elif n==2:
    print('February')
elif n==3:
    print('March')
elif n==4:
    print('April')
elif n==5:
    print('May')
elif n==6:
    print('June')
elif n==7:
    print('July')
elif n==8:
    print('August')
elif n==9:
    print('September')
elif n==10:
    print('October')
elif n==11:
    print('November')
elif n==12:
    print('December')
else:
    print('Invalid number')'''


months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

n = int(input("Enter a number: "))

if 1 <= n <= 12:
    print(months[n - 1])
else:
    print("Invalid number")

                                                    
