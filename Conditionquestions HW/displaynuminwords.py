'''n = int(input("Enter a number: "))

if n==1:
    print('One')
elif n==2:
    print('Two')
elif n==3:
    print('Three')
elif n==4:
    print('Four')
elif n==5:
    print('Five')
elif n==6:
    print('Six')
elif n==7:
    print('Seven')
elif n==8:
    print('Eight')
elif n==9:
    print('Nine')
elif n==10:
    print('Ten')
else:
    print('Invalid number')'''


numbers = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']

n = int(input("Enter a number: "))

if 1 <= n <= 10:
    print(numbers[n - 1])
else:
    print('Invalid number')

                                                    
