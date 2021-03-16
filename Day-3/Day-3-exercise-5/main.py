# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1 = name1.lower()
name2 = name2.lower()

t = int(name1.count('t')) + int(name2.count('t'))
r = int(name1.count('r')) + int(name2.count('r'))
u = int(name1.count('u')) + int(name2.count('u'))
e = int(name1.count('e')) + int(name2.count('e'))

l = int(name1.count('l')) + int(name2.count('l'))
o = int(name1.count('o')) + int(name2.count('o'))
v = int(name1.count('v')) + int(name2.count('v'))

true = (t + r + u + e)
love = (l + o + v + e)

trueStr = str(t + r + u + e)
loveStr = str(l + o + v + e)

score = int(trueStr + loveStr)

scoreStr = trueStr + loveStr

if(score < 10 or score > 90):
  print("Your score is " + scoreStr + ", you go together like coke and mentos.")
elif(score > 40 and score < 50):
  print("Your score is " + scoreStr + ", you are alright together.")
else:
  print("Your score is " + scoreStr + ".")

