# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#initialize total cost to 0
total = 0

#Pricing for small pizza
if(size == "S"):
  total += 15

  if(add_pepperoni == "Y"):
    total += 2
  if(extra_cheese == "Y"):
    total += 1

#Pricing for medium pizza
elif(size == "M"):
  total += 20

  if(add_pepperoni == "Y"):
    total += 3
  if(extra_cheese == "Y"):
    total += 1

#Pricing for large pizza
elif(size == "L"):
  total += 25

  if(add_pepperoni == "Y"):
    total += 3
  if(extra_cheese == "Y"):
    total += 1

#If customer did not enter "S", "M", or "L" for size
else:
  print("Size error.")

#print out total
print("Your final bill is: $" + str(total))



