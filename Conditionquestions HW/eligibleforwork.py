name = (input("Enter your name: "))
gender = (input("Enter your gender: "))

if gender == 'Female':
    age = int(input("Enter your age: "))
    if age >=21 and age <=25:
        print("You are eligible")
    else:
        print("Not eligible")
elif gender == 'Male':
    print("Male not allowed")
