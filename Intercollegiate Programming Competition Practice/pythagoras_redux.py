# Daniel Wernz
# Problem 2: Pythagoras Redux
# Sample from 2011

user_entered_maximum = int(input("Enter the maximum: "))

result = []

a = 2
b = 2
c = 2

while (c >= 2 and c <= user_entered_maximum):
    if (a ** 2) + (b ** 2) == c ** 2:
        result.append([a, b, c])

    c += 1
    a = 2
    b = 2

    while (b >= 2 and b <= user_entered_maximum):
        if (a ** 2) + (b ** 2) == c ** 2:
            result.append([a, b, c])

        b += 1
        a = 2

        while (a >= 2 and a <= user_entered_maximum):   
            if (a ** 2) + (b ** 2) == c ** 2:
                result.append([a, b, c])

            a += 1
            

result = set(tuple(sorted(x)) for x in result)

sorted_result = sorted(result)

print("a\tb\tc")
for group in sorted_result:
    table = (str(group[0]) + "\t" + str(group[1]) + "\t" + str(group[2]))

    print(table)




# print(sorted_table)

# and (b >= 2 and b <= user_entered_maximum) and (c >= 2 and c <= user_entered_maximum):