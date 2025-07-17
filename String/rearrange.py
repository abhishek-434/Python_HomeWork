text = input("Enter text: ")

lowercase = ''
uppercase = ''

for char in text:
    if char.islower():
        lowercase += char
    elif char.isupper():
        uppercase += char

result = lowercase + uppercase
print("Rearranged text:", result)