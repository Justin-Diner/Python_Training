import datetime
"""
To do:  
1. Strings and Array portions of App Academy Open
2. Two Pointers on Array method (some sort of indexing question) – What to do on last index. 
3. Search algos 

"""
# Strings  

# .index() is similar to indexOf in JavaScript. 
print("Spaghetti".index("h")) # 4

#.count() – 
print("Spaghetti".count("t")) # 2 

# Concatenation – Python uses the (+) operator to stitch strings together. 
# You can also use the (*) operator to repeat a given number of times. 

print("s" * 5) #sssss

# Formatting
# The format function will help a lot with debugging. You can put elements inside of a variable:
first_name = "Billy"
last_name = "Bob"
print('Your name is {0} {1}'.format(first_name, last_name)) # Your name is Billy Bob

# For simple uses, you can use the 'f' flag on a string. 
print(f'Your name is {first_name} {last_name}')
""" 
VALUE	METHOD	RESULT
s = "Hello"	s.upper()	"HELLO"
s = "Hello"	s.lower()	"hello"
s = "Hello"	s.islower()	False
s = "hello"	s.islower()	True
s = "Hello"	s.isupper()	False
s = "HELLO"	s.isupper()	True
s = "Hello"	s.startswith("He")	True
s = "Hello"	s.endswith("lo")	True
s = "Hello World"	s.split()	["Hello", "World"]
s = "i-am-a-dog"	s.split("-")	["i", "am", "a", "dog"]
"""

# Join 
# In JavaScript, the join method was on the Array object. In Python, the join method is on the String object. 
s = "--".join(["it", "is", "kind"])
print(s)

# Other helpful string methods 
"""
isalpha()	returns True if the string consists only of letters and is not blank.
isalnum()	returns True if the string consists only of letters and numbers and is not blank.
isdecimal()	returns True if the string consists only of numeric characters and is not blank.
isspace()	returns True if the string consists only of spaces, tabs, and newlines and is not blank.
istitle()	returns True if the string consists only of words that begin with an uppercase letter followed by only lowercase letters.
"""

#name = input("What is your name?\n")
#print(f'Hello {name}')
#print("Hi, {0}.".format(name))
## Also can use the percent sign. 
#print("Hi, %s." % name)

shopping_list = ['bread', 'milk', 'eggs']
print(', '.join(shopping_list))

# Comma as thousands separator
print('{:,}'.format(1234567890))

# Date and Time
d = datetime.datetime(2020, 7, 4, 12, 15, 58)
print('{:%Y-%m-%d %H:%M:%S}'.format(d))

# Percentage 
points = 190
total = 220
print('Correct answers: {:.2%}'.format(points/total))

a = "a"
b = "b"
an = "an"

print(b + an)
print(b + a*7)
print(b + an*2 + a)
print("$1" + ",000" * 3)

def concat_name(first_name, last_name):
    return f'{first_name}, {last_name}'

print(concat_name("First", "Last"))  #> "Last, First"
print(concat_name("John", "Doe"))    #> "Doe, John"
print(concat_name("Mary", "Jane"))   #> "Jane, Mary"

print(reversed("hello"))