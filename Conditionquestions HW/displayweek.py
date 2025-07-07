'''n = int(input("Enter a number: "))

if n==1:
    print('Sunday')
elif n==2:
    print('Monday')
elif n==3:
    print('Tuesday')
elif n==4:
    print('Wednesday')
elif n==5:
    print('Thrusday')
elif n==6:
    print('Friday')
elif n==7:
    print('Saturday')
else:
    print('Invalid number')                        

     '''

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

n = int(input("Enter a number: "))

if 1 <= n <= 7:
    print(days[n - 1])
else:
    print('Invalid number')
