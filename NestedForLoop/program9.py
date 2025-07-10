for i in range(1, 7):
    for j in range(1, i + 1):
        num = i * j
        if num % i == 0:
            print(num, end=" ")
    print()