# print("Hello")
# Literal assignment
f = "Sam"
l = "Raimi"

# print(type(f))
# print(type(f) == str)
# print(isinstance(f,str))

# Constructor function
# pizza = str("Pineapple")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza,str))

# Concatenation
full = f + " " + l
print(full)

# Casting a number to a string
decade = str(1980)
print(type(decade))
print(decade)
 
statement = "I like music from the "+ decade + "s."
print(statement)

# Multiple lines
multiline = '''
Hey, how are you ?

I was just checking in. 
                                All good?

'''

print(multiline)

#Escaping special characters
sentence = 'I\'m back at work!\t Hey!\n\nWhere\'s this at \\located?'
print(sentence)

# String Methods

print(f)
print(f.lower())
print(f.upper())

print(multiline.title())
print(multiline.replace("good","ok"))
print(multiline)

print(len(multiline))
multiline += "           "
multiline = "             " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print("")

#Build a menu
title = "menu".upper()
print(title.center(20,"="))
print ("coffee".ljust(16,".") + "$1".rjust(4))
print ("Muffin".ljust(16,".") + "$2".rjust(4))
print ("Cheesecake".ljust(16,".") + "$4".rjust(4))

print("")

# string index values
print(f[1])
print(f[-1])
print(f[1:-1])
print(f[1:])

# Some method returns boolean data
print(f.startswith("S"))
print(f.endswith("Z"))

# Boolean Data type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue,bool))

#Numeric data type
price = 1000
best_price = int(80)
print(type(price))
print(isinstance(best_price,int))

#float
gpa = 3.28
y = float(1.14)
print(type(gpa))

#complex
com_value = 5+3j
print(type(com_value))
print(com_value.real)
print(com_value.imag)




