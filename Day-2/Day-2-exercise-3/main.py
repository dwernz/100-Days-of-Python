# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age = int(age)
timeLeft = 90 - age

daysLeft = timeLeft * 365
weeksLeft = timeLeft * 52
monthsLeft = timeLeft * 12

daysLeft = str(daysLeft)
weeksLeft = str(weeksLeft)
monthsLeft = str(monthsLeft)

print("You have " + daysLeft + " days, " + weeksLeft + " weeks, and " + monthsLeft + " months left.")