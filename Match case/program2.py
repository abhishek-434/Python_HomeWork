month = int(input("Enter month number: "))
match month:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print("Number of days is 31")

    case 2:
        print("Number of days is 28") 
        a = int(input("Enter Year"))
        if a%4==0:
            print("Leap year") 
        else:
            print("Not a leap year")
    case _:
        print("Number of days is 30")