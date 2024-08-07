## check pos and nev number

# num = int(input("Enter number: "))
# if(num > 0):
#     print("Num is positive")
# else:
#     print("num is negative")   

#prints all odd number    

# num1 = int(input("Enter 1st number: "))
# num2 = int(input("Enter 2nd number: "))

# for i in range(num1, num2):

#     if(i % 2 != 0):
#         print(i)


#check palidrome number

# num = int(input("Enter number: "))
# temp = num
# rev = 0

# while(num>0):

#     dig = num % 10
#     rev = rev * 10 + dig
#     num = num // 10

# if(temp == rev):
#     print("number is palindrome")
# else:
#     print("Number is not plindrome")   


#print number in reverse

# num = int(input("enter number: "))
# rev = 0

# while(num > 0):

#     digit = num % 10
#     rev = rev * 10 + digit
#     num = num //10

#print(rev)


#Print All Integers that Aren’t Divisible by Either 2 or 3

# num1 = int(input("Enter number: "))
# num2 = int(input("Enter number: "))

# for i in range(num1, num2):

#     if( i % 2  != 0  & i % 3 != 0 ):

#         print(i)


#sum of digits of number

# num = int(input("Enter number "))

# sum = 0
# while(num > 0):

#     dig = num % 10
#     sum = sum + dig
#     num = num // 10

# print(sum)    


#count number of digit in number

# num = int(input("Enter number: "))
# count = 0
# while(num>0):
#     count = count + 1
#     num = num // 10
# print(count)   


#print smallest divisor of integer

# num = int(input("Enter number: "))
# a = []

# for i in range(2, num+1):
#     if(num % i == 0):
#         a.append(i)
# a.sort
# print("smallest divisor is: ", a[0])


#Print prime number

# num = int(input("Enter number: "))
# k = 0

# for i in range(2, num//2+1):

#     if(num%i==0):
#         k = k+1

# if(k<=0):
#     print("prime")
# else:
#     print("not prime")   


#print armstrong number

# num = int(input("Enter number: "))
# sum = 0
# temp = num

# while(num>0):

#     dig = num % 10
#     sum = dig*dig*dig + sum
#     num = num//10
    
# if(sum==temp):
#     print("its armstrong")
# else:
#     print("its not armstrong")


#print sum of 1st N natural number

# num = int(input("Enter number: "))
# sum = 0

# while(num>0):
#     sum = sum + num
#     num = num-1

# print(sum)


a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
d=[]
d.append(a)
d.append(b)
d.append(c)
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            if(i!=j&j!=k&k!=i):
                print(d[i],d[j],d[k])


    