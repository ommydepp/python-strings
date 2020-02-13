#strings indexing & slicing
pie="3.142"
print (pie)

a="hello world!"

print (a)
print (a[0]) #assigning indexing from 0
print (a[1])
print (a[2])
print (a[3])
print (a[4])
print (a[5])
print (a[6])
print (a[7])
print (a[8])
print (a[9])
print (a[10])
print (a[11])

print (a[40]) #index is out of range

print (a)
print (a[-2]) #ndexing 2 steps from the last
print (a[:])
print (a[2:5]) #ndexing from 2 to 5 without including index 5
print (a[2:7]) #ndexing from 2 to 7 without including index 7

#string operators
a="hello"
b="world"
print (a+b) #putting a and b together
print (a*4) #multiplying a 4 times
print (r"C:\Users\Student\Documents")
print ("hi {}".format (b)) #replaces hello with hi
print ("h"in a) #checking whether "h" is in a
print ("n"not in a) #checking whether "n" is in a
print ("m"in a) #checking whether "m" is in a
print ("n"in a) #checking whether "n" is in a
print ("l"not in a) #checking whether "l" is in a

#built-in string functions/methods
a="hello world"
b=a.capitalize() #capitalizing the first letter of sentence
print (b)
print (a.capitalize()) #capitalizing the first letter of sentence
print (a.upper()) #capitalizing all letters
print (a.lower()) #lower casing all letters

n="HELLO"
b=n.capitalize()
print (b)
print (n.capitalize())
print (n.upper())
print (n.lower())

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

a = "Hello, World!"
print(a.lower()) # lower cases "Hello, World!"

a = "Hello, World!"
print(a.upper()) # capitalizes "Hello, World!"

a = "Hello, World!"
print(a.replace("H", "J")) # replaces "H" with "J"

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']