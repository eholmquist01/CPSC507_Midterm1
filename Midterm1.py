# Emmalyn Holmquist
# CPSC 507
# Midterm 1
# 9/26/2024

## Problem 1

# Write a Python program that asks the user for their name and prints the following:
# Hello [name]!
# Welcome to the Python Programming midterm.
# Good luck!
# Replace [name] with the user’s input.

name = input("Please enter your name: ")
print("Hello "+name+ "!")
print("Welcome to the Python Programming midterm. \nGood luck!")
# ---------------------------------

# ## Problem 2

# Given a list nums = [2, 4, 6, 8, 10], write a for loop that prints out each number
# in the list multiplied by 2.

nums = [2, 4, 6, 8, 10]
for i in nums:
    num = i*2
    print(num)
# ---------------------------------

# ## Problem 3

# Write a Python program that prompts the user to enter numbers.
# The program should stop when the user enters “STOP”.
# Calculate and print the average of all the numbers entered (excluding the “STOP”).

num = 0 #initialize variables
sum_num = 0
count = 0
while (1): #infinite loop; will break when stop is entered
    num = input("Enter a num: ")
    if num == "STOP": #if STOP then break out of loop
        break
    else: # convert num to integer so that you can sum num for average
        num=int(num)
        sum_num= sum_num+num # calc sum
        count+= 1 #count nums for average calculation
avg= sum_num/count #calc avg
print(avg)
# ---------------------------------

## Problem 4

# Using the turtle module, write a Python program that draws a square with a side length of 100 units.
# Once the square is drawn, the turtle should move to the center of the square and draw a circle with a radius of 50 units.

import turtle
import math
t = turtle.Turtle()
for side in [0,0,0,0]: #repeats instructions 4 times for a square
    t.width(5)
    t.right(90)
    t.forward(100)

t.right(135)
t.forward((math.sqrt(100*100+100*100))/2) #this will give the exact center, as it is half the length of the diameter of the square
t.circle(50) # https://docs.python.org/3/library/turtle.html#turtle.circle
# used python documentation for circle function in turtle
# ---------------------------------

## Problem 5

# Write a Python program that asks the user for the radius of a circle and then calculates:
#   The area of the circle (using π from the math module).
#   The circumference of the circle.
# Print out both values with appropriate labels.

import math
radius = int(input("Please give the radius of a circle: ")) #convert to int for calculating
area = str(radius*radius*math.pi)
circumference = str(2*math.pi*radius) #convert to strings for printing
print("Area: "+area)
print("Circumference: "+circumference)
# ---------------------------------

## Problem 6

# Given a string s = "programmingIsFun", perform the following tasks:
# (a) Convert the entire string to uppercase.
# (b) Extract and print the substring from index 5 to index 10.
# (c) Count and print the number of times the letter ‘g’ appears in the string.

s = "programmingIsFun"
#a
s_upper = s.upper()
#print(s_upper) --- not sure if we are supposed to print this
#b
s_5_10 = s_upper[5:10]
print(s_5_10)
#c
count = 0 #initialize count
for letter in s:
    if letter == "g":
        count+=1
print(count)
# ---------------------------------

## Problem 7

# Write a Python function named is palindrome that:
# (a) Takes a single string argument.
# (b) Returns True if the string is a palindrome and False otherwise.
# The function should ignore spaces, punctuation, and should be case-insensitive.

def is_palindrome(word):
    backwards = '' #initialize string
    for i in word:  #marching through each letter/element in string
        if i.isalnum():  # https://docs.python.org/3/library/stdtypes.html#str.isalnum - check if it is alphanumeric
            backwards += i.lower() #if it is letters, than convert to lowercase (so that its not case sensitive)
    return backwards == backwards[::-1] #check if the word is equal to its backwards self


#check:
# print(is_palindrome("A man, a plan, a canal, Panama!"))
# print(is_palindrome("12343212"))
# print(is_palindrome("1234321"))
# print(is_palindrome("true"))
# ---------------------------------

## Problem 8

# Write a Python program that does the following:
#   Prompt the user for a sentence.
#   Count the number of words in the sentence.
#   Using a for loop, print each word on a new line in reverse order (e.g., ”I love Python” becomes ”Python”, ”love”, ”I”).

sentence = input("Enter a sentence: ")
list = []
temp_string = ""
count = 0
for i in sentence:
    temp_string = temp_string + i #temporarily make a new string so that we can put the words into a string and then into a list
    if i == " ":
        list.append(temp_string) #if the string is followed by a space, then add it to list
        temp_string = "" #reset the temporary string
        count +=1 #increase count of words by 1
list.append(temp_string) #when for loop exits, it will not have included last word. append it now
count = count + 1 #to count the last word (because it will not be followed by a space)
for item in list[::-1]: #start from end of list and increment backwards
    print(item)
# ---------------------------------

## Problem 9

# (a) Write a Python function named estimate pi that:
# (b) Takes a single argument n which represents the number of random points to generate.
# (c) Uses the random module to generate n points in the top right quadrant of the square.
# (d) Returns the estimated value of π using the above Monte Carlo method.

import random
def estimate_pi(n):
    count = 0 # intialize count of  points in the circle
    for i in range(n):
        x = random.uniform(0, 1) #https://docs.python.org/3/library/random.html#random.random
        y = random.uniform(0, 1)
        if x*x + y*y <= 1: #unit circle equation to test if points are within circle
            count += 1
    estimate = 4*(count/n)
    return estimate

#print(estimate_pi(200)) #--check
