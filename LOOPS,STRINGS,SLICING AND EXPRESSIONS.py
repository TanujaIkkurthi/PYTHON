#!/usr/bin/env python
# coding: utf-8

# LOOPS:
# FOR LOOP:
# A for loop is used to repeat a block of code a fixed number of times by going through each item in a sequence 
# (like a list, string, or range) one by one.
# It automatically stops when it reaches the last item — no need to manage a counter yourself.

# In[1]:


#program for sum of all numbers stored in a list
nums = [10, 20, 30, 40]
total = 0
for n in nums:
    total = total + n
print(total)


# Reverse a string:
# 
# Loop through each character of a string and prepend it to a new variable. Prepending means adding the new character at the
# front, which naturally flips the order.
# 
# 

# In[3]:


#Example

word = "Hello"
result = ""
for char in word:
    result = char + result
print(result)


#  while loop:
# 
# A while loop keeps repeating a block of code as long as a condition is true. Unlike a for loop, it does not count items — it just keeps checking the condition before every round. When the condition becomes false, the loop stops. You must always update something inside the loop, otherwise it runs forever.
# 
# while condition:
#     # code runs as long as condition is True
#     # update the variable to eventually make condition False

# In[6]:


i = 1
while i <= 5:
    print(i)
    i = i + 1


#  range:
# 
# range() generates a sequence of numbers for you to loop through. You tell it where to start, where to stop, 
# and how much to jump each time. The stop value is never included — it always stops just before it.
# 
# range(start, stop, step)
# #start = where to begin (default 0)
# #stop = where to end (NOT included)
# #step = how much to jump (default 1)
# 

# In[5]:


#Example

for i in range(1, 6):
    print(i)


# lower limit:
# 
# The lower limit is the starting number — the first value the loop begins from. In range(), this is the first argument.
# In a while loop, it is the value you assign to your counter variable before the loop starts.
# 
# in range(): first argument
# in while: starting variable value
# 

# In[10]:


#Example — lower limit is 3

for i in range(3, 8):
    print(i)


# upper limit:
# 
# The upper limit is the stopping number — the value where the loop ends. In range(), this is the second argument 
# and it is not included. In a while loop, it is the number in your condition that the counter must not exceed.
# 
# in range(): second argument (excluded)
# in while: condition boundary

# In[9]:


#Example — upper limit is 10

i = 1
while i <= 10:
    print(i)
    i += 1


# Break statement — exit the loop early
# 
# break immediately stops the loop and jumps out of it, even if there are items left. 
# Use it when you have found what you were looking for and do not need to keep going.
# 
# 

# In[11]:


#Example

for i in range(1, 10):
    if i == 5:
        break       # stop when i reaches 5
    print(i)


# Continue statement — skip one iteration
# 
# continue skips the rest of the code for the current loop step and jumps to the next one. 
# The loop does not stop — it just skips that one item and carries on.
# 
# 

# In[13]:


#Example

for i in range(1, 6):
    if i == 3:
        continue    # skip number 3
    print(i)


# STRINGS:
# 
# Printing a string:
# Use print() to display text on the screen. Put the text inside quotes and pass it to print().
# 

# In[14]:


print("Hello, World!")


# String indexing:
# 
# Every character in a string has a position number called an index. It starts at 0. Use square brackets [ ] to pick one character. 
# Negative index -1 gives the last character.
# 
# 

# In[15]:


s = "Python"
print(s[0])   # first letter
print(s[-1])  # last letter


# Slicing:
# 
# Slicing cuts out a part of a string using [start:stop]. The start is included, the stop is not.
# 
# 

# In[16]:


s = "Python"
print(s[0:3])  # letters at 0, 1, 2


# Step size:
# 
# Add a third number to slicing [start:stop:step] to skip characters. A step of 2 picks every 2nd character.
# A step of -1 reverses the string.
# 
# 

# In[17]:


s = "Python"
print(s[::2])   # every 2nd letter
print(s[::-1])  # reverse


# Grab everything:
# Use [:] with no start or stop to grab the entire string. This copies all characters from beginning to end.
# 
# 

# In[18]:


s = "Python"
print(s[:])  # grab everything


# String properties:
# Strings are immutable — you cannot change a single letter inside them. You can only create a new string. 
# Use len() to find how many characters a string has.
# 
# 

# In[19]:


s = "Python"
print(len(s))   # number of characters

s="Tanuja"
print(len(s))


# Concatenation:
# Concatenation means joining two strings together using the + operator. You can also repeat a string using *.
# 
# 

# In[21]:


a = "Hello"
b = " World"
print(a + b)  # join them
print(b * 2)  # repeat


# Reassignment:
# You cannot change a character inside a string, but you can give the whole variable a brand new string value.
# This is called reassignment.
# 
# 

# In[22]:


s = "Hello"
print(s)
s = "Goodbye"  # reassign
print(s)


# Built-in functions:
# Python has ready-made functions (methods) that work on strings. Call them using a dot .
# after the string variable. Common ones: upper(), lower(), strip(), replace().
# 
# 

# In[23]:


s = "  hello  "
print(s.upper())        # all caps
print(s.strip())        # remove spaces
print(s.replace("hello","hi"))


# Splitting:
# split() breaks a string into a list of smaller strings at a separator (like a comma or space). 
# Each piece becomes one item in the list.
# 
# 

# In[26]:


s = "apple,banana,cherry"
parts = s.split(",")
print(parts)
print(parts[2])


#  print formatting:
# 
# Print formatting is the way you control how text and variables appear when printed. Instead of just printing a plain variable,
# you mix it with words, set decimal places, or align columns — all inside one clean print() statement.

# In[31]:


price = 9.5678
print(f"Price: {price:.2f}")        # f-string
print("Price: {:.2f}".format(price)) # .format()
print("Price: %.2f" % price)         # %


# find(): location
# find() searches inside a string and returns the index (position number) of the first match it finds. If the word or letter is not found, it returns -1.
# 
# 

# In[28]:


#Example

s = "Hello World"
print(s.find("World"))  # where does "World" start?
print(s.find("xyz"))    # not found


# count(): counting
# count() counts how many times a letter or word appears inside a string. It returns a number.
# 
# 

# In[29]:


#Example

s = "banana"
print(s.count("a"))   # how many "a"s?
print(s.count("na"))  # how many "na"s?


# expandtabs(): spacing
# expandtabs() replaces the tab character \t in a string with spaces. You can set how many spaces each tab becomes 
# by passing a number. Default is 8 spaces.
# 
# 

# In[30]:


#Example

s = "Name\tAge\tCity"
print(s.expandtabs(10))


# we already discussed above fstring and.format

# is-check methods:
# 
# Is-check methods are built-in string methods that ask a yes/no question about a string. 
# They always return either True or False — nothing else. Every one of them starts with the word is.
# 
# True — yes, it matches
# False — no, it does not

# Method      Asks…            True example     False example 
# isalpha()  only letters?      "Hello"               "Hello2"
# isdigit()  only digits?        "123"                 "12a"
# isalnum()  letters or digits?  "Hi99"               "Hi 99"
# isspace()  only spaces?        "   "                "  a"
# isupper()    all uppercase?    "HELLO"              "Hello"
# islower()    all lowercase?    "hello"              "Hello"
# istitle()    title case?     "Hello World"        "hello world"

# Built-in regular expressions:
# 
# Regular expressions (regex) are patterns used to search, find, or replace text. 
# Python has a built-in module called re that gives you functions to work with these patterns. You must import it first 
# before using any regex function.
# 
# import re   # always write this at the top
# 
# Function                       What it does
# re.search()            finds the first match anywhere in the string
# re.match()             checks only the start of the string
# re.findall()           finds all matches and returns a list
# re.sub()               finds a pattern and replaces it
# re.split()             splits the string using a pattern
# re.fullmatch()          checks if the whole string matches

# In[42]:


#ASSIGNMENT FOR LOOP:
    #SAME ORDER
name = "TANUJA"
same_order = ""

for char in name:
    same_order = same_order + char

print("Patient Name :", same_order)



# In[41]:


#REVERSE ORDER
name = "TANUJA"
reverse_order = ""

for char in name:
    reverse_order = char + reverse_order

print("Reversed Name:", reverse_order)


# In[43]:


#COMBINATION OF SAME ORDER AND REVERSE ORDER

name = "TANUJA"

same_order    = ""
reverse_order = ""

for char in name:
    same_order    = same_order + char
    reverse_order = char + reverse_order

print("Same order   :", same_order)
print("Reverse order:", reverse_order)


# In[ ]:




