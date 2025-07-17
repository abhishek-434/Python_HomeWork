email = input("Enter your email address: ")

if "@" in email:
    username, domain = email.split("@")
    print("Username:", username)
    print("Domain:", domain)
else:
        print("Invalid email address")
