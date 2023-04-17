#Example of a Class
#class Dog:
  #def __init__(self,name,breed,age,color):
    #self.name = name
    #self.breed = breed
   # self.age = age
  #  self.color = color

 # def bark(self):
#    print("woof")

#  def fetch(self):
#    print(self.name," went to fetch.")

#Exampoe of an instance of the Dog Class

#my_dog = Dog("Fluffy","Beagle",2,"Brown")

#print(my_dog.name)
#print(my_dog.breed)
#print(my_dog.age)
#print(my_dog.color)


#my_string = "Sophia"
#print(my_string.upper())
#print(my_string.lower())



#Another example of a Class
#class PeopleCounter:
#   x = 0
  
#def anotherOne(self): 
#    self.x = self.x + 1
#    print("So far",self.x)

#people = PeopleCounter() #Creation of an instace of the class PeoplCounter
#people.anotherOne()
#people.anotherOne()
#people.anotherOne()
#people.anotherOne()

#Full Syntax to create the __init__ method 
#def __init__(self,<otherParameters>):

#Creating a new class for an application that creats users login information. 
#class User:
#  def __init__(self, uname, pword):
#    self.username = uname
#    self.password = pword

#account = User('sophia', 'mypass')
#account1 = User('Blake', 'Kelsey01')

#print(account.password)
#print(account.username)
#how to delete an instance. 
#del <instanceName>
#del account
#print(account.password) #Results in an error
#print(type(account)) #Results in an error

#import datetime #importing the datetime module 

#class User:
#  def __init__(self, uname, pword):
#    self.username = uname
#    self.password = pword

#    self.activeUser = True #new variable with True as default value
#    self.numOfLogins = 0 #new variable with 0 as the default value
#    self.dateJoined = datetime.date.today() #new variable using the datetime module
    

#account = User('sophia', 'mypass')

#print(account.username)
#print(account.password)
#account.password = 'python'
#print(account.username)
#print(account.password)
#print(account.activeUser)
#print(account.numOfLogins)
#print(account.dateJoined)
#account.activeUser = False
#print(account.activeUser)

#Syntax to change an attribute 
##<objectName>.<attributeName> = ValueError
#Setting Default Values 
##self.<attributeNameNum> = 0
##self.<attributeNameString> = ""

import datetime
class User:
  def __init__(self, uname, pword):
    self.username = uname
    self.password = pword

    self.activeUser = True 
    self.numOfLogins = 0 
    self.dateJoined = datetime.date.today() 

#Syntax for defining a method in a class
#def<method_name>(self, <parameter(s)>):

#new method to show number of logins
  def show_num_logins(self):
    return self.username + " logged in " + str(self.numOfLogins) + " times."

  def logged_in(self):
    self.numOfLogins = self.numOfLogins + 1

  def login(self, uname, pword):
    if(self.username == uname and self.password == pword):
      print("Login Successful")
      self.logged_in()
    else:
      print("Incorrect username and password")
    
account = User('sophia', 'mypass')
#print(account.show_num_logins())

#account.logged_in()
#account.logged_in()
#account.logged_in()
#print(account.show_num_logins())
account.login('sophia', 'wrongpassword')
account.login('sophia', 'mypass')
print(account.show_num_logins())
