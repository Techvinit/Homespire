n1, n2 = 0, 1
count = 0

num = int(input("Enter number\n"))

while count<num:
    print(n1)
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    count = count + 1
    