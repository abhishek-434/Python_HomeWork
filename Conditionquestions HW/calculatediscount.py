amount = int(input("Enter Sale Price: "))

if(amount>0):
    if amount<=1000:
        dis = amount*0.1
    elif amount<=5000:
        dis = amount*0.2
    elif amount<=10000:
        dis = 0.3 * amount
    else:
        dis=  0.5 * amount

    print("discount: ",dis)
    print("Net Pay: ",amount-dis)
else:
    print("Invalid Amount")



