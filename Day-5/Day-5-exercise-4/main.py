#Write your code below this row 👇

numbers = range(1, 101, 1)

for number in numbers:
  if(number % 3 == 0 and number % 5 == 0):
    number = "FizzBuzz"
  elif(number % 3 == 0):
    number = "Fizz"
  elif(number % 5 == 0):
    number = "Buzz"

  print(number)

