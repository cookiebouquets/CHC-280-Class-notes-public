""" 
    Last class we made a five function calculator 
    
    That's pretty cool but what if we wanted to only do one operation when the program runs

    we need to introduce something called conditional logic  
    
    if-then-else style of thinking
    
    1) is run code line by line sequentially
    2) if-then-else logic
    3) looping statements
"""

"""
    The premise of if-then-else is we want to only run certain lines of code if certain conditions are met
    
    
    if x = 5 
        do something
        
    if message = "hello" 
        do something 
        
    make a new file and call it conditional.py 
    
    we are introducing a branching structure to our programs.
    
    Syntax for this is 
    
    if <conditional>: 
        <code block>
    <keep going>
    
        
    <conditional> is a statement that is either evaluated to true or false (boolean)
    <code blocks> are the lines of code that gets executed when the conditional evaluates to true
"""
#x = int(input("Enter a number "))

"""
    So i only want to print out
    
    "Go hall" if x = 5
    
    Coding is very particular in how you write things. We already have one = reserved for variable assignment
    So checking for equality means we have to use a different or multiple symbols for this
    
    so what is common for conditionals is to use two equals signs to check for equality


    == <= i'm going to call this double equals from now on
    
    python cares a lot about whitespace (or tabs). You'll see in other coding languages {} but in python
    tabbing over is the same thing as curly braces
"""


"""
    That is a basic if statement that will if x == 5 is satisfied 
    
    if <conditional>:
        <code block>
    else: 
        <code block 2>
        
    if <conditional> is not satisfied, python will jump down to else: and run codeblock 2. 
    
    There is a second third keyword I have not shown yet. 
    
    We have the scenario 
    
        print(go hall) when x = 5
        print(i love chc) for all other numbers 
        
    say we wanted to print

        print(go cardinals) for x = 8
    
    In other programming languages what you would do is something like this
    
    if x =5:
        do thing
    else if x = 8:
        do thing
    else: 
        do thing
        
        
"""

    
"""
    So now we have 
    
    if <conditional>:
        code block
    elif <conditional>:
        code block
    else: 
        code block
        
    The question that gets asked often is why do we even need elif or elses if we can do a bunch of if 
    statements to get the same output
"""

#if x%5== 0:
 #   print("Go hall")
    
#elif x%2 == 0:
 #   print("Go cardinals")
    
"""
    So conditionals are not only based on equality. We can do the same thing for other mathematical
    expressions
    
    I only wanted go hall OR go cardinals to print when i typed in x = 10
    
    That means there is something interesting about elif.
    
    IF has precedence over elif ALWAYS  so in our example, divisibility by 5 is a stronger condition
    than divisibilty by 2


    So now we want to do for our 5 function calculator is this routine
    
        1) print the menu of options
        2) accept input for option
        3) navigate if-elif-else chain for printing out the result of the individual operations
"""



print("welcome to the calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Divison")
print("5. Mod")
option = int(input("Select which operation you want: "))
if option == 1:
    num1 = int(input("Enter num 1"))
    num2 = int(input("Enter num 2"))
    sum = num1+num2
    print(sum)
#TODO fill in elif statements for subtraction-mod 
    
    
#your next task is to do an if-elif-else chain that checks whether option equals 1-5 and then print out
#the corresponding math operation when that option is selected