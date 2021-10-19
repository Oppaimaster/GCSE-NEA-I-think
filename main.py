#import string will allow me to use ascii characters and make it easier to code
#imports random
import string
from random import *

symbols = ["!","$","%","^","&","*","(",")","-","_","=","+"]


#Function for if the user want to check how strong their password is
def checker():
  points = 0
  checpas = input("Enter the password that you want to check:")
  completed = []

#This checks if the password contains any upper or lower case letters and will only give points if 
#the password contains both upper or lower case letter
#If the user enter a password all in lower case no points will be give as well as if the password
#contains only upperc case
  if checpas.lower() != checpas and checpas.upper() != checpas:
    points = points + 10
    completed.append("upperlower")
  print(points)
    
#check if the password contains any numbers
  contains_digit = any(map(str.isdigit, checpas))
  if contains_digit == True:
    points = points + 5
    completed.append("numbers")
  print(points)

#check if the password contains any allowed symbols
  if (checpas in symbols):
    points = points + 5
    completed.append("symbols")
  print(points)

  if (len(completed) == 1):
    points -= 5

#check if its in keyboard order
  keyboardOrder = ["qwertyuiop","asdfghjkl","zxcvbnm"]
  for i in range(len(checpas) - 2):
    nextchars = (checpas[i:i+3])
    for x in keyboardOrder:
      if (nextchars in x):
        points = points - 5
        print(points)


#Converts your points into see the strength of your password 
  if points < 0:
    print("Your passowrd is weak")
  elif points > 20:
    print("Your password is strong ")
  else:
    print("Your password is median")
  
  return(points)

#Function for if the user wants to generate a password
#It will generate a number between 8 and 12 and this will be the length of the password
def gen():
  characters = string.ascii_letters + "!$%^&*()-_=+"  + string.digits
  password =  "".join(choice(characters) for x in range(randint(8, 12)))     
  print("Your password is:",password)



#This is the menu
print("1.Check password \n2.Generate password")
Option = int(input("Enter your option:"))
if Option == 1:
  checker()
elif Option == 2:
  gen()
