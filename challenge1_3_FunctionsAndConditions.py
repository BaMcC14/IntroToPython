#Introduction to Functions
#Functions can be built in or user made.

#First user made. We define the finction definition by using the reserve keyword "def" to define it
#then set up the finction myFunction with three parameters firstName, middleInitial, and lastName
#to end a function, we place a colon at the end 

#def myFunction(firstName, middleInitial, lastName):

#finally we will print to screen so we can see it work
#  print(firstName, middleInitial, lastName)

#here is where we call myFunction and pass it the actual values as arguments 
#myFunction("John", "R", "Doe")

#Built in funcitons 
#len() function - lenght of string
#myString = "Python is fun!"
#print(len(myString))

#int() function - creates an integer number from an integer literal, a float literal, or string literal. 
#print(int(100))
#print(int(2.95))
#print(int("100"))

#float() function - creates a float number from an integer literal, float literal, or a string literal as long as the string repesents a float or an integer
#print(float(100))
#print(float(2.95))
#print(float("200"))

#str() function - creates a string from various data types, including stirngs, integer literals, and float literals
#print(str(100))
#print(str(2.95))
#print(str("200"))

#.index() Method - can find the location of a character or a stirng within another string 
#myString = 'Python is fun!'
#print(myString.index("n"))

#.capitalize() Method - can convert the first character of the string to an uppercase with all of the other characters to lowercase
#outputString = 'I AM YELLING!'
#print(outputString.capitalize())

#.lower() Method - converts all the characters of a string to lowercase
#.upper() Method - converts all the characters of a string to uppercase

#.swapcase() Method - swaps all the characters from uppercase to lower or lowercase to upper.
#outputString = 'ThIs Is My TeSt StRiNg!'
#print(outputString.swapcase())

#.title() Method - returns a copy of the string with the first letter of each word converted to uppcase and the other characters converted to lowercase. 
#outputString = 'ThIs Is My TeSt StRiNg!'
#print(outputString.title())

#Conditional Statements.

#this is assigning variable temperature the integer 82
#temperature = 82

#below is the if statement
#if temperature > 0 : #this is the header line that ends with a ":"
#  print('temperature is positive') #this is the indented block

#grade = 15
#if grade > 90:
#elif grade > 80:
#  print("You got a B")
#elif grade > 70:
#  print("You got a C")
#elif grade > 60:
#  print("You got a D")
#else:
#  print("You got a F")

#num = 1
#if not num == 0:
#  print('True')
#else :
#  print('False')

#carSpeed = int(input("Enter in the car's speed between 0 and 200:"))
#if carSpeed > 100:
#  print("The car's speed is fast!")
#else:
#  if carSpeed < 100:
#    print("The car's speed is slow")
#  else:
#    print("The car's speed is exactly 100.")
#
#hungry = input("Are you hungry? Enter y if you are and n of you are not: ")
#if hungry == "n":
#  print("You are not hungry.")
#else:
#  healthy = input("Did you want a healthy meal? Enter y if you do and n if you do not: ")
#  if healthy == "n":
#    print("Getting some junk food.")
#  else:
#    print("Getting a healthy meal")

#inp = input('Enter Fahrenheit Temperature: ')
#try:
 # fahr = float(inp)
  #cel = (fahr - 32.0) * 5 / 9.0
  #print(cel)
#except ValueError as error:
  #print(error)
  #print('Oops, you did not enter in a number. Please enter a number next time.')


#grade = 85
#if grade > 90:
#  print("You got an A")
#elif grade > 80:
#  print("You got a B")
#elif grade > 70: 
#  print("You got a C")
#elif grade > 60:
#  print("You got a D")
#elif grade <= 60:
#  print("You got a F")
#print("We are done!")

#hungry = input("Are you hungry? Enter y if you are and n if you are not: ")
#if hungry == "n":
#  print("You are not hungry.")
#else:
#  healthy = input("Did you want a healty meal Enter y if you do and n if you do not: ")
#  if healthy == "n":
#    print("Getting some junk food.")
#  else:
#    print("Getting a healthy meal.")
#print("All done!")

#variable for drink order 
#ask the user if they would like water coffee or tea
#if water
  #hot or col
      #drink is water hot
    #if cold 
      #ice or no ice 
        #drink is cold water with ice
        #drink is cold water with no ice
#elif coffee 
  #decaff or not
  #milk cream or none
  #sugar 
    #drink is coffee 
#elif tea 
  #green or black 
#drink is green tea
#drink is black tea


#Drink details program. This program will ask the user what they want to drink and contitions of the choices made. 
drinkDetails=""

drink = input('What type of drink would you like to order?\nWater\nCoffee\nTea\nEnter your choice: ')
if drink == "Water":
  drinkDetails = drink
  temperature = input("How would you like your water? Hot or Cold: ")
  if temperature == "Hot":
    drinkDetails += ", " + temperature
  elif temperature == "Cold":
    drinkDetails += ", " + temperature
    ice = input("Would you like ice? Yes or No: ")
    if ice == "Yes":
      drinkDetails += ", Ice"
  else:
    drinkDetails += ", unknown temperature entered."

elif drink == "Coffee":
  drinkDetails = drink
  decaf = input("Would you like decaf? Yes or No: ")
  if decaf == "Yes":
    drinkDetails += ", Decaf"
  milkCream = input("Would you like Milk, Cream or None: ")
  if milkCream == "Milk":
    drinkDetails += ", Milk"
  elif milkCream == "Cream":
    drinkDetails += ", Cream"
  sugar = input("Would you like sugar? Yes or No: " )
  if sugar == "Yes":
    drinkDetails += ", Sugar"
    

elif drink =="Tea":
  drinkDetails = drink
  teaChoice = input("Green or Black Tea: ")
  if teaChoice == "Green":
    drinkDetails += ", " + teaChoice
  elif teaChoice == "Black":
    drinkDetails += ", " + teaChoice

else:
  print("Sorry, we did not have that drink available for you.")
print("Your drink selection:  ", drinkDetails)


