#!/usr/bin/env python
# coding: utf-8

# 1. Round 4.5667 to the nearest hundreth using a build-in function, round().

# In[1]:


round(4.5667)


# 2. Convert "657" to an integer data type

# In[4]:


print(int("657"))


# 3.
# Write a program to get two numbers from a user. Then, create a secret code where a code consists of 6 numbers and each number is randomly generated number between two numbers from a user. 

# In[9]:


import random as mylibrary
mylibrary.random()
import random as rand
rand.random()
rand.randint(1,12)
print(rand.randint(1,12))
print(rand.randint(1,12))
print(rand.randint(1,12))
print(rand.randint(1,12))
print(rand.randint(1,12))
print(rand.randint(1,12))


# 4.
# Write a program to center align below text where number of characters per line is 40:
# 
#     Hickory, dickory, dock,
#     The mouse ran up the clock.
#     The clock struck one,
#     The mouse ran down,
#     Hickory, dickory, dock
# 

# In[24]:


line1 = "Hickory, dickory, dock,"
line2 = "The mouse ran up the clock."
line3 = "The clock struck one,"
line4 = "The mouse ran down,"
line5 = "Hickory, dickory, dock"
line1 = line1.center(40)
line2 = line2.center(40)
line3 = line3.center(40)
line4 = line4.center(40) 
line5 = line5.center(40)
line1 = line1.strip(".")
line2 = line2.strip(".")
line3 = line3.strip(".")
line4 = line4.strip(".")
line5 = line5.strip(".")
print(line1)
print(line2)
print(line3)
print(line4)
print(line5)


# 5. Write a function to calculate the miles per gallon.
# Get a miles driven and gallons used from a user and call your function to calculate the miles per gallon. 

# In[1]:


#receive iput
miles_driven = 201.5
gallons_of_gas_used = 3.5
miles_driven = float(input('\nEnter number of miles driven: '))
gallons_of_gas_used = float(input('Enter gallons of gas used: '))
#Process (calculate stuff)
miles_per_gallon = miles_driven / gallons_of_gas_used

#output info
print=('Miles per gallon =')



# In[2]:


print=('Miles per gallon =')


# 6.
# Enhance compute() function to compute circle's area and circumference where :
#  - circle's area = 3.14 X (radius X radius)   
#  - circle's circumference = 3.14 X diameter
#     
# You must make sure the original functionality of compute() function still works.
# Get necessary information from a user and then call your function to show it works.

# In[ ]:


import math
radius = 36
radius = float(input('\nEnter the radius of a circle: '))
area = math.pi * (radius**2)
circumference = 2 * math.pi * radius 


# In[ ]:


radius = float(input('\nEnter the radius of a circle: '))
area = math.pi * (radius**2)
circumference = 2 * math.pi * radius 


# In[ ]:


print("*** The Area and Perimeter Program ***")  
print("Circle")


    


# 7.
# Write a function called multiply_two() that accepts two parameters. The function should print a message like '15 + 2 = 17'.  Randomly generate two numbers between 1 and 100, then call the function with the two random numbers.

# In[6]:


def sum_up(val1, val2):
    return val1 + val2

print(sum_up(17,30))


# 8. Create a function for a multiplication table.  Get a number from a user and then call you function which produces a multiplication table for that number.
# The output should look something like this:
# 
#         Enter a number: 3
#         3 X 1 = 3
#         3 X 2 = 6
#         3 X 3 = 9
#         3 X 4 = 12
#         3 X 5 = 15
#         3 X 6 = 18
#         3 X 7 = 21
#         3 X 8 = 24
#         3 X 9 = 27
#         

# In[2]:


n = int(input('3: '))
for i in range(1,27)
    print(n, "*", i, "=", n*i)


# 9.
# Write a function that accepts a string and returns a string that is 
#     - without any leading nor trailing blanks
#     - converts to all capital letters
#     - and replaces all blanks with a period(.) 
# 
# Write a program to accept a string from a user then call your function and display the original string and changed string.  
# 
# The output should look something like this:
# 
#         Enter a text: may your dreams come true
#         
#         Original Text: may your dreams come true
#         New Text: MAY.YOUR.DREAMS.COME.TRUE

# In[ ]:





# 10.
# Write a function to convert a test score to a grade where  
#  - 90 - 100: A
#  - 80 - 89:  B
#  - 70 - 79:  C
#  - 60 - 69:  D
#  - < 60   :  F
#  
# If a score is not between 0 and 100 then print out an error message. In the program, ask the user for a score and then call your function. 

# In[4]:


grade = int(input("enter your grade here: "))

if grade > 90:
    amount = "A"
    
elif grade > 80 and grade < 90:
    amount = "B"
    
elif grade > 70 and grade < 80:
    amount = "C"
    
elif grade > 60 and grade < 70:
    amount = "D"
    
elif grade < 50:
    amount = "F"
    
print('amount')


# In[ ]:




