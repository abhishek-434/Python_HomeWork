marks = int(input("Enter the Marks(0-100): "))

if 0<= marks <=100:
    if marks >= 90:
        subject = 'English'
    elif marks >= 80:
        subject = 'Hindi'
    elif marks >=70:
        subject = 'Maths'
    elif marks >= 60:
        subject = 'Science'
    else:
        subject = '50'
    print("subject: ",subject)
else:
    print("Invalid marks")


