month = int(input("Enter month number: "))

match month:
    case 2:
        print("Number of days is 28 or 29")
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print("Number of days is 31")
    case 4 | 6 | 9 | 11:
        print("Number of days is 30")
    case _:
        print("Invalid month number")
