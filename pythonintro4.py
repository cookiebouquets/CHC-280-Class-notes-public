#Feb 24, Day 6

"""
    Today: Lists and loops (maybe)
    
    So we know to manipulate variables with arithmetic which is fantastic 
    
    But the problem is, it kinda sucks to make variables for each individual 
    thing we want to store. What if we want to aggregate data into one address? 
    
    So we can do this with lists
    
    If you're familiar with other programming languages, lists are basically
    just arrays but somehow worse and better in every way 
"""

mylist = [] #This makes an empty list 

"""
    square bracket operator makes a list (empty) but you put stuff in it 
"""

grades = [81,88,92,98,96,95]

"""
    You can put stuff in the square brackets (comma dilineated)
    
    Question: How do we access individual grades from our list of grades?
"""

print(grades)

"""
    Answer: Square bracket operators (again)
"""

print(grades[0])


""" 
    So why did grades[0] print 81 when 81 is the first element in the list? 
    
    So lists and most things in python, computer science, etc. start from 0 <= mod
    
    you have a list of length n and if you divide by n, weird things happen, so we end
    just using the numbers
    
    0,...,n - 1
    
    what numbers can go inside the square brackets?
    
    0 up until n - 1 where n is the length of the list
    
""" 

grades = [81,88,92,98,96,95]

print(grades[5])

"""
    we call the numbers that go inside the square brackets the index of the element
    
    index singular
    indices plural
    
    vocab for lists 
    
    list = ordered list of numbers,objects,etc. 
    indices = the position of each element 
    
    syntax 
    
    mylist = [] <- to make a list
    mylist[] <- to get an element 
    
    So for people who are familiar with other languages, lists can do weird things
    in python
    
    
"""

print(grades)

grades = [88,65,"math"] #this is acceptable in python, but not in other languages
print(grades)

print(grades[0])
print(grades[2])

"""
    Because python allows mixed datatypes in lists, you have to be really careful with
    your data types. 
"""

a = [1,2,3,4,5]

print(a[0] + a[2])

"""
    I can do arithmetic on elements of a list just like if they were variable names.
    
    
"""

b = [1,2,3,"pi"]

#print(b[0]+b[3])

"""
    We got a type error, we tried to add a number and a string together which makes
    no sense!
    
"""

"""
    Other things we can do with lists:
    
    We can to the list with .append()
"""

c = [1,2,3]
print(c)
c.append(4)
print(c)

"""
    <listname>.append(<element>) allows you to add things to a list
"""

c.remove(4)

print(c)

"""
    <listname>.remove(<element>) allows you to remove things from a list
"""

""" 
    The big thing we care about in programming is the attributes or characteristics
    of these objects that we manipulate. we can get the length of a list using
    
    len()
"""

print(len(c))

""" 
    important detail: len() gives us the length of the list (1 - the last element)
    but the indices go from 0 - length minus 1
    
    so we're gonna do a math calculator again but this time what I want you to do
    
"""


#                              Five Function Calculator again with lists
nums = []
nums.append(int(input("    ")))
nums.append(int(input("    ")))
#bonus challenge, rather than printing the result, add the result to the list THEN print it out 
nums.append(nums[0] + nums[1])
print(nums[2])
nums.append("Whatever") 