card_number = input("Enter 16-digit card number: ")

if len(card_number) == 16 and card_number.isdigit():
    masked = "**** " * 3 + card_number[-4:]
    print("Masked Card Number:", masked)
else:
    print("Invalid card number. Please enter exactly 16 digits.")
