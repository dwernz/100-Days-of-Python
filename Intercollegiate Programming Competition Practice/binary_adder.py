# Daniel Wernz
# Problem 2: Binary Adder
# Sample from 2011

b = (input("Enter the binary number: "))

binary = {'0','1'}
t = set(b)

x = 0

while (x != -1):
    if binary == t or t == {'0'} or t == {'1'}:
        d = int(input("Enter the decimal number to add: "))
        
        d_in_bin = bin(d)

        sum = bin(int(b, 2) + int(d_in_bin, 2))

        print("Binary sum is " + str(sum[2:]))

        x = -1
    else:
        b = (input("Number not binary\nEnter the binary number: "))
        t = set(b)


