n = int(input("How many numbers do you want to sum? "))
total = 0
count = 0

while count < n:
    num = int(input(f"Enter number {count + 1}: "))
    total += num
    count += 1

print("Sum =", total)
