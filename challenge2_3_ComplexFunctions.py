#----while Loop----
#while<expression>:
# <statement(s)>

#myNum = 5
#while myNum > 0:
#  myNum -= 1
#  print(myNum)
#print("Our loop is done")

#----for Loop----
#for <variable> in <iterable>:
  #<statement(s)>

#productList = ("card", "paper", "glue", "pencil")
#for product in productList:
#  print(product)

#for counter in range(-2,3):
#  print("Counter is set to: ", counter)

#for counter in range(10, 1, -2):
#  print("Counter is set to: ", counter)

#for char in "Python":
#  print(char)

#myNumb = 6
#while myNumb > 0:
#  myNumb -= 1
#  print(myNumb)
#print("Blastoff!")

#textEntered = ""
#stringBuilder = ""
#while textEntered != "quit":
#  textEntered = input("Enter in a string, enter quit to exit the loop: ")
#  if textEntered != "quit":
#    stringBuilder += textEntered + " "
#print(stringBuilder)

#myNumber = 6
#while myNumber > 0:
#  myNumber = myNumber - 1
#  if myNumber == 2:
#    break
#  print(myNumber)

#myNumber = 6
#while myNumber > 0:
#  myNumber = myNumber - 1
#  if myNumber == 2:
#    continue
#  print(myNumber)

#myNumber = -4
#while myNumber < 0:
#  myNumber += 1
#  if myNumber == 0:
#    print(0)
#    continue
#  print('T'+ str(myNumber))
#print("Blastoff!")

#----while Loop with else statement----
#while<expression>:
#  <statement(s)>
#else:
#  <additional statements>

#myNumber = 6
#while myNumber > 0:
#  myNumber = myNumber - 1
#  print(myNumber)
#else:  
#  print('Blastoff!')

#friendsList = ['Joseph', 'Glenn', 'Sally']
#for friends in friendsList:
#  print('Happy New Year: ', friends)
#print('Done!')

#countItems = 0
#for iterval in [3, 41, 12, 9, 74, 15]:
#  countItems = countItems + 1
#print('Count: ', countItems)

#totalItems = 0
#for itervar in [3, 41, 12, 9, 74, 15]:
#  totalItems = totalItems + itervar
#print('Total: ', totalItems)

#smallestValue = None
#print('Before', smallestValue)
#for itervar in [100, 3, 41, 12, 9, 74, 15]:
#  if(smallestValue is None or itervar < smallestValue):
#    smallestValue = itervar
#  print('Loop:', itervar, smallestValue)
#print('Smallest:', smallestValue)

#numberToFind = 52
#for itervar in [3, 41, 12, 9, 74, 15]:
#  if itervar == numberToFind:
#    print('Number Found')
#    break
#else:
#  print('Number not found')

#----Nested while Loop----
#while<expression>:
#  while<expression>:
#    <statement>
#  <statement>

#----Nested for Loop----
#for<variable> in <iterable>:
#  for<variable> in <iterable>:
#    <statement(s)>
#  <statement(s)>

#multiplesList = [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15], #[4, 8, 12, 16, 20]]
#print(multiplesList)

#multiples = []
#for outer in range(1,5):
#  multiples.append([])
#  for inner in range(1,6):
   #print("Outer: ", outer, ", Inner: ", inner, "Outer x inner: ", inner * outer)
#    multiples[outer - 1].append(outer * inner)
#print(multiples)

#for outerList in multiples: 
#  for innerValue in outerList:
#    print(innerValue, " ", end = '')
#  print()

#while True:
#  line = input('Enter input(# tag will not print). Type done when finished')
#  if line[0] == '#':
#    continue
#  if line == 'done':
#    break
#  print(line)
#print("Done!")
  
#for count in range(1,5):
#  print("Count is set to:", count)

#def print_stuff():
#  print("########################")
#  print("Using for comment block")
#  print("########################")

#print_stuff()

#def print_comment(comment):
#  print("#################")
#  print(comment)
#  print("#################")

#print_comment("This comment is important")


#The Return Statement 
#def return_one_hundred():
#  return 100
#    ^return statement 
#          ^return value

#something = return_one_hundred()
#print(something)
#print(type(something))

#def print_stuff():
#  print("########################")
#  print("Using for comment block")
#  print("########################")

#something = print_stuff();
#print(something)
#print(type(something))

#Function to calculate average. 
#this function takes in one agrument numbers and returns the average of those numbers. 
#def calculate_average(numbers):
#  return sum(numbers)/len(numbers)

#or can use a variable to return the number

#def calcualte_average(numbers):
#  my_avg = sum(numbers)/len(numbers)
#  return my_avg
#print(calculate_average([10, 20, 30, 40]))

#returning multiple return values 
#def calculate_multiple(numbers):
#  return sum(numbers), len(numbers), sum(numbers)/len(numbers)
  
#print(calculate_multiple([10, 20, 30, 40]))


#divmod example 
#print(divmod(21, 5))
#print(divmod(15, 5))

#return with conditions 
#def calculate_absolute(number):
#  if number > 0:
#    return number
#  elif number < 0:
#    return -number #turns a negative number into a positve number
#  else:
#    return 0

#print(calculate_absolute(-5))
#print(calculate_absolute(5))
#print(calculate_absolute(0))

#more simplified version of return with conditions 
#def calculate_absolute(number):
#  if number >= 0:
#    return number
#  else:
#    return -number

#print(calculate_absolute(-5))
#print(calculate_absolute(5))
#print(calculate_absolute(0))


#even more simplified version of return with conditions 
#def calculate_absolute(number):
#  if number >= 0:
#    return number
#  return -number

#print(calculate_absolute(-5))
#print(calculate_absolute(5))
#print(calculate_absolute(0))

#import math
#def dB(V1, V2):
#  return 20 * math.log10(V1/V2), V1, V2 
#calc_dB = dB(10,5)
#print(calc_dB)

#Sample Nested Function
#indentations are important to tell Python which function is which 
#def outer_func():
#  def inner_func():
#    print("Outputting from the inner function")
#  inner_func() #call to the inner function
#outer_func() #call to the outter funciton 

#Nested Function
#def outer_func(what):
#  def inner_func():
#    print("I like", what)
#  inner_func()
#outer_func("Python")

#recursion example
#def countdown(n):
#  print(n)
#  if n == 0: #base case when n is equal to 0
#    return
#  else: 
#    countdown(n - 1)

#countdown(10.2)

#Factorial Example of Recursion 
#n! = n * (n-1)!

#def factorial(number):
#  if not isinstance(number, int):
#    raise TypeError("Sorry. number must be an integer.")
#  if number < 0:
#    raise ValueError("Sorry. number must be zero or positive.")
#  def inner_factorial(number): #nested function for calculation factorial
#    if number <= 1:
#      return 1
#    return number * inner_factorial(number - 1)
#  return inner_factorial(number)

#print(factorial(4))

#Challenge:
#def outer_math(x):
#  def inner_math():
#    z = x + y
#    return z
#  return inner_math()
#z = outer_math(2)
#print("z = ", z)

#Complex functions with multiple arguments 
#def priceInformation(qty, item, price):
#  print(f'{qty} {item} cost ${price:.2f}')

#priceInformation(12, 'strawberries', 5.99)
#priceInformation(12, 5.99, 'strawberries') #valueError
#priceInformation(5.99, 'strawberries', 12) #logical error
#priceInformation(price=5.99, item='strawberries', qty=12) #using the arguments 
#priceInformation(item='strawberries', price=5.99,  qty=12) #can be moved around


#total = 0; #global variable 

#def sum(arg1, arg2):
# total = arg1 + arg2;
#  print("Local total: ", total)
#  return total;

#sum(10,20)
#print("Global total: ", total)

#What variables are within the scope of the inner2 function?
#q = 1
#def outer1(i):
#  j = i + 1
#  def outer2():
#    k = j + 1
#    def inner1():
#      m = k + 1
#      def inner2():
#        n = q + m + 1
#        return n
#      m = inner2()
#      return m
#    k = inner1()
#    return k
#  j = outer2()
#  return j
  
#print ("", outer1(1),"", outer1(1))
#Answer - n,m,k,j,i,q
