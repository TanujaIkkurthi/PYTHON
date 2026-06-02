#!/usr/bin/env python
# coding: utf-8

# 1. Lists:
# A list is a collection of items stored in a single variable, ordered and changeable.
# 

# In[1]:


#python
fruits = ["apple", "banana", "cherry"]
print(fruits)  # ['apple', 'banana', 'cherry']


# 2. Indexing and Slicing:
# 
# Indexing — access a single item by position (starts at 0).
# 
# Slicing — access a range of items [start:end] (end is excluded).
# 

# In[2]:


#python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])   # apple
print(fruits[-1])  # cherry  (negative = from end)

#python
print(fruits[0:2])  # ['apple', 'banana']
print(fruits[1:])   # ['banana', 'cherry']


# 3. Mutability:
# Mutable key concept
# Lists are mutable — you can change them after creation (add, remove, or modify items) without making a new list.
# 

# In[3]:


# Same list object, changed in place
my_list = [1, 2, 3]
my_list[0] = 99
print(my_list)  # [99, 2, 3]


# Basic List Methods:
#     
# 1.append(item):
# Adds a single item to the end of the list.
# 

# In[4]:


fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)  # ["apple", "banana", "cherry"]


# 2.pop() / .pop(index):
# Removes and returns an item. Without an index it removes the last item; with an index it removes that specific item.
# 

# In[5]:


nums = [10, 20, 30]
last = nums.pop()        # removes 30 → last = 30
second = nums.pop(0)    # removes 10 → second = 10
print(nums)             # [20]


# Using the popped value:
# Because .pop() returns the removed item, you can store and use it immediately.
# 

# In[6]:


stack = ["a", "b", "c"]
top = stack.pop()
print("Removed:", top)   # Removed: c
print("Stack:", stack)   # Stack: ["a", "b"]


# 3.sort()
# Sorts the list in place (ascending by default). Use reverse=True for descending. Does not return a new list.
# 

# In[7]:


nums = [3, 1, 4, 1, 5]
nums.sort()
print(nums)              # [1, 1, 3, 4, 5]
nums.sort(reverse=True)
print(nums)              # [5, 4, 3, 1, 1]


# 4.reverse()
# Reverses the list in place. Not the same as sorting — it just flips the current order.
# 

# In[8]:


letters = ["a", "b", "c"]
letters.reverse()
print(letters)  # ["c", "b", "a"]


# Nested Lists & Matrix:
# Nesting lists
# A list can hold other lists as items. A matrix is a common use case — a list of rows, each row being a list of values.
# 

# In[9]:


# 3×3 matrix
matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
print(matrix[1][2])  # 6  (row 1, col 2)


# List Comprehensions:
# List comprehension syntax
# A concise one-line way to create a new list from an existing iterable.
# 

# In[10]:


squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]


# All List Methods — One by One
# 1.append(x)
# Adds item x to the end of the list.
# 

# In[11]:


a = [1, 2]
a.append(3)
print(a)  # [1, 2, 3]


# 2.count(x)
# Returns how many times item x appears in the list.
# 

# In[12]:


a = [1, 2, 2, 3]
print(a.count(2))  # 2


# 3.extend(iterable):
# Adds all items from another list (or any iterable) to the end. Unlike append, it unpacks the items.
# 

# In[13]:


a = [1, 2]
a.extend([3, 4])
print(a)  # [1, 2, 3, 4]


# 4.index(x)
# Returns the index (position) of the first occurrence of item x.
# 

# In[14]:


a = ["a", "b", "c"]
print(a.index("b"))  # 1


# 5.insert(i, x):
# Inserts item x at position i, shifting existing items right.
# 

# In[15]:


a = [1, 3, 4]
a.insert(1, 2)
print(a)  # [1, 2, 3, 4]


# 6.pop(i)
# Removes and returns the item at index i. Defaults to the last item.
# 

# In[16]:


a = [10, 20, 30]
val = a.pop(1)
print(val)  # 20
print(a)    # [10, 30]


# 7.remove(x)
# Removes the first occurrence of item x by value (not by index).
# 

# In[17]:


a = [1, 2, 3, 2]
a.remove(2)
print(a)  # [1, 3, 2]


# 8.reverse()
# Reverses the list in place — flips the order of all items.
# 

# In[18]:


a = [1, 2, 3]
a.reverse()
print(a)  # [3, 2, 1]


# 9.sort()
# Sorts the list in place in ascending order. Pass reverse=True for descending.
# 

# In[19]:


a = [5, 2, 8, 1]
a.sort()
print(a)  # [1, 2, 5, 8]


# Tuples:
# Constructing a tuple ( ) or no brackets
# A tuple is an ordered collection created with parentheses (or just commas). Single-item tuples need a trailing comma.
# 

# In[20]:


t1 = (1, 2, 3)        # with parentheses
t2 = 1, 2, 3           # without parentheses
t3 = (42,)              # single-item — comma required!
print(t1[0])           # 1  (index access same as list)


# 1.count(x)
# Returns how many times value x appears in the tuple.
# 

# In[21]:


t = (1, 2, 2, 3)
print(t.count(2))  # 2


# 2.index(x)
# Returns the index of the first occurrence of value x.
# 

# In[22]:


t = ("a", "b", "c")
print(t.index("b"))  # 1


# Immutability key concept:
# Tuples cannot be changed after creation — no adding, removing, or editing items. Trying to do so raises a TypeError.
# 

# In[23]:


t = (1, 2, 3)
t[0] = 99  # TypeError: 'tuple' object does not support item assignment


# When to use tuples:
# Use a tuple when data should not change — coordinates, RGB colors, database records, function return values, or dictionary keys.
# 

# In[ ]:


point   = (10.5, 20.3)          # x, y coordinate
color   = (255, 128, 0)           # RGB value
# Tuples can be dict keys; lists cannot
grid = {(0, 0): "start", (3, 3): "end"}


# Sets:
# unordered, no duplicates
# A set stores unique items with no guaranteed order. Created with curly braces or set().
# Use set() for an empty set — {} creates a dict.
# 

# In[24]:


s = {1, 2, 3, 2, 1}
print(s)  # {1, 2, 3}  — duplicates removed automatically


# .remove(x)
# Removes item x. Raises a KeyError if the item does not exist.
# 

# In[25]:


s = {1, 2, 3}
s.remove(2)
print(s)  # {1, 3}
s.remove(99)  # KeyError!


# .discard(x)
# Removes item x if it exists. Does nothing (no error) if the item is not found — safer than remove.
# 

# In[26]:


s = {1, 2, 3}
s.discard(99)  # no error
s.discard(2)
print(s)  # {1, 3}


# .clear()
# Removes all items from the set, leaving an empty set.
# 

# In[27]:


s = {1, 2, 3}
s.clear()
print(s)  # set()


# .pop()
# Removes and returns an arbitrary item (sets are unordered, so you cannot predict which). Raises KeyError if empty.
# 

# In[28]:


s = {10, 20, 30}
val = s.pop()
print(val)  # some item, e.g. 10
print(s)    # remaining two items


# Dictionaries:
# Constructing a dictionary
# A dictionary stores key-value pairs inside curly braces. Keys must be unique and immutable (strings, numbers, tuples).
# Values can be anything.
# person = {
#   "name": "Alice",
#   "age": 30,
#   "city": "Dallas"
# 
# 

# Keys, values, and index:
# A key is the label; a value is the data it holds. You access values by key (like an index), not by position number.
# 

# In[33]:


person = {"name": "Alice", "age": 30}
print(person["name"])   # Alice   ← access by key
print(person["age"])    # 30


# .upper() on a value:
# .upper() is a string method — call it on a string value retrieved from the dict to convert it to uppercase.
# 

# In[34]:


person = {"name": "alice"}
print(person["name"].upper())  # ALICE


# Accessing objects from a dictionary:
# Use square brackets or .get(). The .get() method is safer — it returns None (or a default) instead of crashing on missing keys.
# 

# In[35]:


d = {"fruit": "mango", "count": 5}
print(d["fruit"])              # mango
print(d.get("color", "red"))  # red  ← default if missing


# Nesting dictionaries:
# A dictionary value can itself be a dictionary. Access nested values by chaining keys.
# 

# In[36]:


users = {
  "alice": {"age": 30, "city": "Dallas"},
  "bob":   {"age": 25, "city": "Austin"}
}
print(users["alice"]["city"])  # Dallas


# Basic Dictionary Methods
# 1.keys()
# Returns a view of all keys in the dictionary.
# 

# In[37]:


d = {"a": 1, "b": 2}
print(d.keys())    # dict_keys(["a", "b"])


# 2.values()
# Returns a view of all values in the dictionary.
# 

# In[38]:


d = {"a": 1, "b": 2}
print(d.values())  # dict_values([1, 2])


# 3.items()
# Returns all key-value pairs as tuples — perfect for looping.
# 

# In[39]:


d = {"a": 1, "b": 2}
for k, v in d.items():
    print(k, v)  # a 1 / b 2


# 4.get(key, default)
# Returns the value for a key, or a default value if the key doesn't exist (no crash).
# 

# In[40]:


d = {"name": "Bob"}
print(d.get("age", 0))  # 0  (key missing, returns default)


# 5.update(other_dict)
# Merges another dictionary in. Existing keys are overwritten; new keys are added.
# 

# In[41]:


d = {"a": 1}
d.update({"b": 2, "a": 99})
print(d)  # {"a": 99, "b": 2}


# 6.pop(key)
# Removes a key and returns its value. Raises KeyError if missing (pass a default to avoid this).
# 

# In[42]:


d = {"x": 10, "y": 20}
val = d.pop("x")
print(val)  # 10
print(d)    # {"y": 20}


# 7.clear()
# Removes all key-value pairs, leaving an empty dictionary.
# 

# In[43]:


d = {"a": 1, "b": 2}
d.clear()
print(d)  # {}


# Basic dict comprehension:
# A one-line way to build a dictionary from an iterable. Syntax: {key: value for item in iterable}.
# 

# In[44]:


squares = {x: x**2 for x in range(1, 6)}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# Dict comprehension with condition:
# Add an if filter to include only items that match a condition.
# 

# In[45]:


prices = {"apple": 1.2, "banana": 0.5, "cherry": 3.0}
cheap = {k: v for k, v in prices.items() if v < 2}
print(cheap)  # {"apple": 1.2, "banana": 0.5}


# In[ ]:




