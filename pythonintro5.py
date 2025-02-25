""" 
    Today we will cover two types of looping statements, 
    
    for loops and while loops. This will be the last thing we need before we begin doing labs in python
    
    OBJECTIVE TODAY: Write a program that does a shift cipher on a message in python
"""

""" 
    So last class I talked about lists and how to access data from them. One question that should immediately
    come to mind: what happens if our list is millions of indices long? how do we access all of the elements
    individually? 
    
    
"""

mylist = [1,2,3,4,5]

#print(mylist[0])
#print(mylist[1]) 
#... ^ we can do this for when the list is really really small. 

""" 
    Lists are not typically this small. So how do we repeat a process over and over again?
    
    I said that there were really three things you can do with a program
    
        - run a program line by line (sequentially)
        - do some sort of if-else logic (selection)
        - repetition (iteration)
        
    How is repeating something over and over again useful? Imagine you had like a website with a bunch
    of customer records, and you needed to apply a discount to certain accounts. 
    
    So let's say applying a 20% discount to an account takes 15 lines of code. Say we needed to do this
    to 200 accounts. 
    
    If we did this manually, it would be 15*200 lines of code we would have to write. So that sucks to write
    
    If we instead did a for-each loop, we could only write the first 15 lines of code, and let the computer
    do the rest
    
    syntax for for loops 
    
    for <temporary variable> in <name of list>: 
"""

mylist = [1,2,3,4,5,6,7,8,9,10]
#print(mylist[0])
#print(mylist[1])
#print(mylist[2])
#print(mylist[3])
#print(mylist[4])
#print(mylist[5])
#print(mylist[6])
#print(mylist[7])
#print(mylist[8])
#print(mylist[9])
#^ this is gonna take 10 lines of to write, but i can do it in 2 lines 

#for number in mylist: 
    #print(number)
    
"""
    What is going to happen when this runs? 
    
    For loops create a temporary variable gets assigned to each value in a list.
    
    1st run: number = 1 
    2nd run: number = 2
    
    and so on.
    
    Printing is not the only thing that we can do obviously
"""
"""
avg = 0
for number in mylist:
    avg = avg+number

print(avg)
print(avg/len(mylist))
 """
#in this example I took an average of all of the numbers in the list 
#So this could be useful in hypothesis testing where you need to do an average over hundreds of samples

"""
    For loops also do not care about the length of the list we are iterating over. 
"""

#mylist = [1,2]
#for num in mylist:
    #print(num)
    
    
#mylist = [1,2,3,54,6,6,4,2,525,2,62,72,3745,76,848,38]
#for num in mylist:
    #print(num)
    
"""
    There is no real limit other than by memory in how many times we can run a line in a for loop. 
    
    There is an exception to this ^ python will exit a program if it feels like it will forever.
    
    So how is this relevant to cryptography?  
    
    At this point we can do these things:
    
        1) manipulate numbers
        2) manipulate lists
        3) manipulate strings (plaintext)
        4) we can do a for-each loop
        
    If you recall from our previous assignments this semester, we did a bunch of basic cryptography by hand
    But we were highly limited in the length of the message that we were willing to encrypt. 
    
    Never really gave anything longer than 5 characters because anything more would be too long to do by hand.
    
"""

"""
    We've only really manipulated lists of numbers. However, strings are also lists. They're lists of characters
    
""" 


#print(message)

#for char in message: 
    #print(char)
    
"""
    I have told now at this point, that strings are also lists, we can manipulate lists with for loops,
    and now we can manipulate long strings of plaintext using python. So the question is now, how do we 
    convert our text into numbers? 
    
    A big part of cryptography was converting our text into numbers. In our basic case, we just did
    mod 26, all 26 letters of the alphabet in lowercase. In computer science, there is a international 
    standard called ascii which every computer should be able to display regardless of machine specifications 
    
    We can convert characters into their ascii value in python in literally one line
"""

char = "c"
value = ord(char)
#print(value)

"""
    ord(<character>) will convert a character into its ascii value. Additionally, we can take a number
    and convert into its ascii character.
    
    chr()
"""


#print(converted)

"""
    So now our message is a list of numbers. Remember our crpytography scheme
    
    1) take our plaintext
    2) convert into numbers
    3) do weird things to the numbers
    4) convert it back into text
"""

"""
    So lets do ceasar cipher on our mcmullen intro paragraph.
    
    I will choose the key to be +2
"""

#Ceasar Cipher Example
message = "Enrollment in the McMullen Scholars Program is limited. Candidates with a strong admissions portfolio (middle school grades, test scores, and recommendations) will be invited to interview with the Principal and the Program Director. Candidates must demonstrate high general intellectual ability as well as specific high-level ability in the verbal, mathematical, and language skills areas on the Archdiocesan High School Placement test and a standardized test taken within the last two years. Once invited to apply, those students who pursue a place in the Program will be interviewed by the Principal and the Program Director. Invitations to enter the McMullen Scholars Program are based on the above criteria and the interview."


converted = []
for character in message:
    convert = ord(character)
    converted.append(convert)
    

cipher = ""
for num in converted:
    num = num + 2
    char = chr(num)
    cipher = cipher + char

#print(message)    
print(cipher)

"""
    Now we have our ciphertext, how do convert it back? 
"""

converted = []
for char in cipher:
    num = ord(char)
    converted.append(num)
    
plaintext = "" 
for num in converted:
    num = num - 2
    char = chr(num)
    plaintext = plaintext+char
    
print(plaintext)

#Now we have done a full ceasar's cipher

""" 
    So we have 12 minutes: What I want you to do is a ceasar cipher of +3 to anything you find on the calvert
    hall website
"""