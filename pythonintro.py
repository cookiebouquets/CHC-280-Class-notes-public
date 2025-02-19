""" 
    So today I'll teach some python, don't type things that 
    i type in orange 
    
    
    what is python?
    
    python is a scripting language that is interpreted
    
    what does interpreted mean? for python it uses
    the python interpreter to convert the code into machine code
    
    compiled languages use a compiler to convert code 
    into assembly byte code
    
    interpreted languages can be ran on much more general hardware
    but compiled languages will have weird artifacts from not
    being interpreted 


    C, C++, and Java are all verbose while python is pretty 
    open ended on how you can code 
"""


"""
    Question: What is coding actually useful for?
    
    answer: doing really hard math automatically 
    
    python is not strongly typed, but java is strongly typed 
    
    int x = 1
"""

x = 1

"""
    we have made our first variable.
    
    
    Anatomy of variables: 
        1. is the name (x)
        2. is the variable assignment operator (=)
        3. data (1)
    
    Call the name of our variable an address. When I click run there are two pieces of memory on RAM
        1. Stack - premade
        2. The Heap - which is dynamic
        
    000000000
    000000000
    000000000
    
    x = 1
    
    000001000
    000000000
    000000000
    
    The address tells me which part in memory 1 is stored at (in this case its named x)

"""
"""
x = 1
y = 5

print(x+y)
"""
"""
    print() is an example of a function, similar to one in math. Whenever you "call" a function, 
    you will need parentheses.
    
    Keep this in mind: printing something to the terminal is not the same as saving in memory. In our example
    we printed 6 to the terminal but it is inaccessible because it doesnt have a name.
    
    We have to assign the sum x + y to another variable
"""
"""
variable = x + y
print(variable)
"""
"""
    So variables have things associated with them on top of their name and data 
    
    their data type: 4 primitive data types in python
        1) integers (whole numbers including + and -)
        2) floating point numbers (decimal points)
        3) strings (text)
        4) boolean values (true and false)
"""

"""
z = 3.14 #floating point number (float)
sum = x + z #float 
check = True #boolean (bool)
#to make a string in python, we have to wrap our text in quotation marks ""
message = "hello world" 
#strings need quotation marks, that means my comments from before are strings too
print(message)
"""

"""
    Variable names are case sensitive.
    
    we've seen all of the primitive data types. Next thing we want to see is input and output 
    
    output = print() is an output, what about inputs?
    
    
"""



"""
    Nuances about strings in python. Strings care about whitespace 
"""

"""
    Simple program time: accept two numbers, save their sum, and then print it 
"""
num1 = int(input("enter num 1 "))
num2 = int(input("enter num 2 "))
sum = num1+num2
print(sum)

"""
    what the hell, we did not get 3? So what we need to do is something called typecasting 
    
    input() specifically asks for a string. We want a number. how do we do this?
    
    we typecast num1 into an integer. How do we do this? 
    
    int() <= integer constructor 
"""

""" 
    What other mathematical operations matter to us?
    
    adding, subtracting, multiplying, and dividng 
"""

