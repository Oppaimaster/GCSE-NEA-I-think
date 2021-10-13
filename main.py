#import string will allow me to use ascii characters and make it easier to code
#imports random
import string
from random import *
 
points = 0

#Function for if the user want to check how strong their password is
def checker():
  points = 0
  checpas = input("Enter the password that you want to check: ")

  return any(char.isdigit() for char in checpas)
  
#checks if the password contains any lower or upper case if it contains atleast 1 upper case it will
#add 5 points and if it contains any lower case letters it will add 5 points
  if checpas.lower() != checpas and checpas.upper() != checpas:
    points = points + 5

  if checpas.upper() != checpas and checpas.lower() != checpas:
    points = points + 5
  print(points)




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


