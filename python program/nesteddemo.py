num= int(input("Enter number"))

if(num<0):
    print("Number is negative")
elif(num>0):
    if(num<10):
        print("no is between 1-10")
    elif(num>10 & num<20):
        print("no is between 11-20")
    else:
        print("no is greater than 20")
else: 
    print("no is 0")               
