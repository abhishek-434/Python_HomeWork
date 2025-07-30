word = {
    'apple': 'Seb',
    'banana': 'Kela',
    'cat': 'Billi',
    'dog': 'Kutta'
}

w = input("Enter a word: ")

if w in word:
    print("The meaning of '" + w + "' is: " + word[w])
else:
    print("Sorry, the meaning of '" + w + "' is not in the dictionary.")
