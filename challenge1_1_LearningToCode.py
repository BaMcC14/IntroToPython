#Author: Sophia
#Created Date: March 28, 2023
#Description: This program has two functions to find the maximum
#value of three numbers
#Exampe of usage: print(max_of_three(20, 30, -10))
#Result: function returns 30
#Function: max_of_two
#Purpose: This function accepts two numbers, compares them,
#and returns the value that is larger. 
def max_of_two(firstNumber, secondNumber):
  if firstNumber > secondNumber:
    return firstNumber
  return secondNumber

#Function: max_of_three
#Purpose: This function accepts three numbers and sends the second and third
#number to max_of_two. It then takes the result of that comparison to 
#send the first number and the result to get the larger value 
#of all three. 
def max_of_three( firstNumber, secondNumber, thirdNumber):
  return max_of_two( firstNumber, max_of_two( secondNumber, thirdNumber) )
#Testing the function max_of_three
print(max_of_three(-20, 3, 10))

#This function takes an integer input from the user and tells them if they passed or not. 
#Note no validation has been done to this code. 
score = int(input("What is your exam score (0-100):"))
if score >= 90 and score <= 100:
  print("You got an A! Congrats!")
elif score >= 80 and score < 90:
  print("You got a B! Well done!")
elif score >= 70 and score < 80:
  print("You got a C.")
else:
  print("You did not pass the exam.")