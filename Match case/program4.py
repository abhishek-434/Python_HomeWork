age = int(input("Enter your age: "))

match age >= 18:
    case 1:
        print("You are eligible to vote.")
    case _:
        print("You are not eligible to vote.")