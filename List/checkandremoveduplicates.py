l1 = ['pizza','burger','momos','fries','shake','pizza','momos']

l2 = []
for item in l1:
    if item not in l2:
        l2.append(item)

print(l2)
