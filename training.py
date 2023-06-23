"""Module for Testing Python"""
friends = ["Allen", 2, "Brian", "Tyler", "Allison"]
friends[1] = "Creed"
friends.reverse()
# List functions
# append = push = friends.append("Justin")
# friends.pop() = Removes the last element. pop(0) will remove the first element.
# insert = insert. It will push all values to the right. = friends.insert(1, "Justin") (Unshift)
# remove = delete element = friends.remove("Allen")
# friends.clear() = empty list.
# friends.index("Brian") = 2. You get an error if not in the list.
# friends.count("Brian") = 1
# friends.sort() = sorts the list in ascending order. # Returns none. It sorts the ORIGINAL list.
# friends.reverse() = will reverse the list.
# friends.copy() = creates a new copied list.

# Tuples
# Type of data structure. Container where we can store different values.
# A tuple is similar to a list.
# A few key differences from lists.
coordinates = (4, 5, 12)
# Cannot change tuples. They are immutable. They are a data structure that is a constant.
print(coordinates)

#Functions

def say_hi(name, age):
    """Prints say Hi"""
    print("Hi " + name + ", you are " + str(age))

say_hi("Justin", 35)
say_hi("Steve", 21)

# Return function
def cube(num):
    """Return the cube of the number"""
    return num * num * num

RESULT = cube(5)

print(RESULT)

if RESULT == 64:
    print("Correct Answer")
else:
    print("Was not 64")

IS_TALL = False

if IS_TALL and RESULT == 125:
    print("You did this right")
elif not(IS_TALL) and RESULT == 125:
    print("Else if condition")
else:
    print("You are not tall")

# Comparison Operators
def max_num(num1, num2, num3):
    """Determines the largest number of 3"""
    if num1 != num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(3, 4, 5))

## Better Calculator
#num1 = float(input("Enter the first number: "))
#op = input("Enter the operator: ")
#num2 = float(input("Enter the second number: "))

#if op == "+":
#    print(num1 + num2)
#elif op == "-":
#    print(num1 - num2)
#elif op == "*":
#    print(num1 * num2)
#elif op == "/":
#    print(num1 / num2)
#else:
#    print ("Invalid Operator")

# Dictionaries
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(monthConversions.get("Sep", "Not Valid"))
# Dictionaries can also have numbers as the keys.