#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
bill = int(input("What is the total bill? "))
numPeople = int(input("How many people are splitting the bill? "))
tipPercent = int(input("Please enter desired percentage for tip (typical values are 12, 15, 18, 20). "))
splitBill = (bill / numPeople) * (1 + (int(tipPercent) / 100))
formattedSplitBill = str(("%.2f"%splitBill))
print("The bill split evenly between " + str(numPeople) + " people is $" + formattedSplitBill)
