"""
    Last time we covered basic variables and inputs. We will continue with a review 
    of those concepts and work on manipulating strings. 

    Our goal by the end of class today is to write a basic 5 function calculator      
"""

""" 
    First thing: print statements
    
    always need parentheses after functions 
    
    What goes inside the print statement? It's either strings or variable names
"""

print("hello world")

""" 
    We can also print out variables by putting the variable name into the print
    statement
"""

x = 5
print(x)

""" 
    Variables have two pieces of information associated with them
    
    the name and their data
    
    left hand side of the equals sign is always going to be the name
    right hand side of the equals sign is always going to be the data
    
    the name acts as two things
    
        1) its a label 
        2) its also an address in memory 
        
    so think of variables as houses that store information and their names are 
    the addresses to the house
"""

""" 
    Python does line by line execution. what that means is if we want to use a variable
    we have to declare it before we even use it 
"""

""" 
    Variables also have a third piece of information associated with them:

        their datatype
        
    computer languages really only have three basic data types (primitive data types)
    
        -integers: whole numbers including negatives
        -floats: floating point decimal numbers
        -strings: Plaintext
        -booleans:True or False
"""


""" 
    So printing stuff out to the terminal is cool; but that doesn't mean we saved 
    the result anywhere 
    
    printing =/= variable assignment 
    
    Whenever the result of a mathematical operation ends up being important later on
    it's better practice to save that result into another variable and then 
    print out that variable instead
"""

x= 5 
y = 10
sum = x+y
print(sum)

"""
    So not only can you save numbers into variables, we can also save strings
"""

school = "CHC"
print(school)

"""
    So what other kinds of operations do we have for numbers?
    
    We know we can add
    We can subtract
    we can multiply
    we can divide
    we can also do modular arithmetic 
    
"""

difference = y - x
print(difference)
product = x*y
print(product)
quotient = y/x
print(quotient)
mod = y%x
print(mod)

""" 
    So overall, our five functions are 
    
    +: addition
    -: subtraction
    *: multiplication
    /: division
    %: modular arithmetic 
"""

""" 
    So the nature of computer programs is less so print out a bunch of thingsd
    and more involving input/outputs from the user of the program
    
    we want our programs to enforce/introduce an input/out or back and forth
    communcation between the user and the program 
    
    how do we allow for user input? input()
""" 




"""
    What input() does is it will pass control of the program to the user and wait
    for keyboard input into the terminal. So we need to put a prompt inside
    the parentheses indicating that the program is waiting for an input
"""


"""
    Whenever you do input() you're typing in a prompt in the parentheses as the 
    programmer, waiting for the input from the user. Do NOT type the actual data
    into input()
"""



"""
    What the hell we got 105 instead of 15 for our 10 and 5 example. 
    
    input() only returns strings. We want it to convert the data into an integer
    
    constructors change datatypes (or rather it will create an object of that 
    data type with the data you pass into it)
    
    int() float() bool() <-- these are constructors 
"""

x = input("enter your data for x ")
x = int(x)
y = input("enter your data for y ")
y = int(y)
sum = x + y 
print(sum)
""" 
    We can change datatypes in separate lines OR we can do it on the same line
    as the input
"""

x = int(input("enter your data for x "))
y = int(input("enter your data for y "))
sum = x+y
print(sum)

"""
    nested functions go inside to outside 
    
    Our objective for the last 10 minutes is to write our five function calculator
    which takes in 10 numbers and prints out the separate operations for them
"""