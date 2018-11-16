"""
to choose random char you'll need import the random module
"""
import random
"""
now u will choose a random char from the list and store it in a variable called
password"""
chars= 'abcdefghijklmnopqrstuvwxyz@#$^&ABCDEFGHI1234567890'
# enter the size of password as urs requriment
length=input('Enter the size of password:')
#use int() to turn the user's input into a whole number
length=int(length)
# add this code to create 3 passwords
for p in range(3):
    password=''
    for c in range(length):
        password +=random.choice(chars)
    print(password)

