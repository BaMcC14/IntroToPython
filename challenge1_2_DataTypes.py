#Type function
#print(type("Hello World"))

#myValue = 2
#print(myValue)

#myValue += 2
#print(myValue)

#myValue *= 2
#print(myValue)

#myValue -= 3
#print(myValue)

#myValue /=2
#print(myValue)

#Exponent feature in Python
#base = 10
#exponent = 2
#result = base ** exponent 
#print(result)

#Modulo  
#remainder = 7 % 3 
#print(remainder)

#remainder = 99 % 3
#print(remainder)
#extract the right-most digit
#remainder = 6849 % 10
#print(remainder)
#extract the two right-most digits
#remainder = 6849 % 100
#print(remainder)


#pizzaSlices = 20
#remainingSlices = (pizzaSlices - 2) / 2
#print(remainingSlices)

#investment = 300 
#money = ((investment * 2 / 3) - 50) * 5 
#print(money)

#investment = 300
#profit = ((investment * 2/3) - 50) * 5
#print(profit)


#print("line1\nline2\nline3")

#myVar1 = "Learning"
#myVar2 = "Python"
#result = myVar1 + " " + myVar2
#print(result)

#myString = 'Python is great\n'
#result = myString * 5
#print(result)

#in feature in Python
#stringToFind = 'some'
#sentence = 'Python is quite a fun language to learn. There can be some great string functions to use.'
#result = stringToFind in sentence
#print(result)

#spanning a string over multiple lines
#outputString = """This is my first line
#and now my second line
#and lastly my last line."""
#print(outputString)

#We are importing a module that we need to be able to generate #random numbers
import random

#We are creating a random even number between 2 and 10 by
#first randomizing an integer between 1 and 5. This will be our
#final number. The number to add will take this final number and #multiply  it by 2.
randomFinalNumber = random.randrange(1,5)
numberToAdd = randomFinalNumber * 2 

#Asking the user to enter in thier name
name = input("Hello! What is your name?")

#Script to walk through each of the steps
print("Welcome " + name + ", we'll perform some mind reading on you.")
print("First, think of a number between 1 and 10.")
enteredNumber = int(input("Enter in a number between 1 and 10: ")) 
print("Multiply the result by 2.")
userNumber = enteredNumber * 2
print(">> userNumber at this step = " + str(userNumber))
answer = input("Ready for the next step?")
print("Now, add...let's see...")
print(numberToAdd)
userNumber = userNumber + numberToAdd 
print(">> userNumber at this step = " + str(userNumber))
answer = input("Ready for the next step?")
print("Now, divide the number you have by 2.")
userNumber = userNumber / 2
print(">> userNumber at this step = " + str(userNumber))
print("Now, subtract the original number that you thought about.")
answer = input("Ready for the last step?")

#Guessing the number
print("Well " + name + ", let me read your mind... The number that you have right now is a....")
print(randomFinalNumber)

userNumber = userNumber - enteredNumber
print(">> userNumber at this step = " + str(userNumber))