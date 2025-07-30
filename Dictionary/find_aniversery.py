# Create a dictionary with names and their anniversaries
ann = {
    'rahul': '23/11/2023',
    'sumit': '15/08/2022',
    'rakesh': '01/01/2021'
}


name = input("Enter the name: ")


if name in ann:
    print(name + "'s anniversary is on " + ann[name])
else:
    print("No anniversary found for " + name)
