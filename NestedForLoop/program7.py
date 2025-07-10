1
23
456
7891
23456

num = 1

for i in range(1, 6):
    for j in range(i):
        if num > 9:
            num = 1
        print(num, end="")
        num += 1
    print()