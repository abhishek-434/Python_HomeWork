coun = {
    'A': ['Australia', 'Austria', 'Argentina'],
    'B': ['Brazil', 'Belgium', 'Bangladesh'],
    'C': ['Canada', 'China', 'Colombia'],
    'D': ['Denmark', 'Dominican Republic']
}


letter = input("Enter the starting letter (A-Z): ").upper()

if letter in coun:
    print("Countries starting with", letter + ":")
    for country in coun[letter]:
        print("-", country)
else:
    print("No countries found starting with the letter", letter)
