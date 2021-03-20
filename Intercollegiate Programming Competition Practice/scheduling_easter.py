# Daniel Wernz
# Problem 1: Scheduling Easter
# Sample from 2011

year = int(input("What is the year? "))

if (year >= 1583 and year <= 1699):
    M = 22
    N = 2
elif (year <= 1799):
    M = 23
    N = 3
elif (year <= 1899):
    M = 23
    N = 4
elif (year <= 2099):
    M = 24
    N = 5
elif (year <= 2199):
    M = 24
    N = 6
elif (year <= 2299):
    M = 25
    N = 0

a = year % 19
b = year % 4
c = year % 7
d = (19 * a + M) % 30
e = (2 * b + 4 * c + 6 * d + N) % 7

print(a, b, c, d, e, M, N)

if (d + e < 10):
    month = "March"
    day = d + e + 22
else:
    month = "April"
    day = d + e - 9

if (month == "April" and day == 26):
    day = 19

if (month == "April" and day == 25 and d == 28 and e == 6 and a > 10):
    day = 18

day = str(day)

if (day == "1" or day == "11" or day == "21" or day == "31"):
    day = day + "st"
elif (day == "2" or day == "12" or day == "22"):
    day = day + "nd"
elif (day == "3" or day == "13" or day == "23"):
    day = day + "rd"
else:
    day = day + "th"

print("In " + str(year) + ", Easter is on " + str(month) + " " + day)