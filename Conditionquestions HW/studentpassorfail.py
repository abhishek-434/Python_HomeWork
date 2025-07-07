sub1 = int(input("Enter marks of 1st subject: "))
sub2 = int(input("Enter marks of 2nd subject: "))
sub3 = int(input("Enter marks of 3rd subject: "))

marks = (sub1+sub2+sub3)/3

if sub1>20 and sub2>20:
    print('Pass')
elif sub2>20 and sub3>20:
    print('Pass')
elif sub3>20 and sub1>20:
    print('Pass')
elif marks>20:
    print('Pass')
else:
    print('Fail')
                    