num = int(input("Enter number: "))
temp = num
rev = 0

while(num>0):
    
    dig = num % 10
    rev = rev*10 + dig
    num = num // 10

if(temp == rev):
    print("Palindrom")
else:
    print("Not palindrome")    
