#!/usr/bin/env python
# coding: utf-8

# # Functions, Scoping, Data Collections 1 & List Comprehensions

# ## Tasks Today:
# 
# <i>Monday Additions (or, and ... if statements)</i>
# 
# 1) String Manipulation <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) strip() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) title() <br>
# 2) Working With Lists <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) min() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) max() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) sum() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) sort() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) Copying a List <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; f) 'in' keyword <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; g) 'not in' keyword <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; i) Checking an Empty List <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; j) Removing Instances with a Loop <br>
# 3) List Comprehensions <br>
# 4) Tuples <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) sorted() <br>
# 5) Functions <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) User-Defined vs. Built-In Functions <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Accepting Parameters <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) Default Parameters <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) Making an Argument Optional <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) Keyword Arguments <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; f) Returning Values <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; g) *args <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; h) Docstring <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; i) Using a User Function in a Loop <br>
# 6) Scope

# ### String Manipulation

# ##### .lstrip()

# In[1]:


# string.lstrip()
name ="          John Smith"
print(name.lstrip(" "" " "J"))


# ##### .rstrip()

# In[2]:


# string.rstrip()
name.rstrip("h")


# ##### .strip()

# In[3]:


# string.strip()
name = "   John Strength"
print(name.strip())


# ##### .title()

# In[4]:


# string.title()
president = 'barack obama'
print(president.title())


# ### String Exercise <br>
# <p>Strip all white space and capitalize every name in the list given</p>

# In[22]:


names = ['    coNNor', 'max', 'EVan ', 'JORDAN']

# HINT: You will need to use a for loop for iteration
for name in names:
    if name == '    coNNor':
        print(name.strip())
        print(name.title())
        print(name)
    elif name == 'max':
        print(name.title())
        
    elif name == 'EVan ':
        print(name.rstrip(" "))
        
        
#Could figure out how to apply two function and output


# ### Working With Lists

# ##### min()

# In[15]:


# min(list)
number = [4,2,97,16]
print(min(number))


# ##### max()

# In[16]:


# max(list)

print(max(number))


# ##### sum()

# In[18]:


# sum(list)

print(sum(number))


# ##### sorted()

# In[19]:


# sorted(list)
sorted_number = sorted(number)
print(sorted_number)


# ##### .sort() <br>
# <p>Difference between sort and sorted, is that sorted doesn't change original list it returns a copy, while .sort changes the original list</p>

# In[27]:


# list.sort()
print(f'Before Sort: {number}')
print(number.sort())
print(number)


# use sorted when you don't want to alter original list, use .sort() when you want to alter original list


# ##### Copying a List

# In[ ]:


# [:] copies a list, doesn't alter original
#save to a new variable


# ##### 'in' keyword

# In[30]:


l_teachers = ['Joel', 'Derek', "Conner"]

#if 'Joel' in l_teachers:
    #else:
    #print('Not an insturctor')
    
for name in l_teachers:
    if 'C' in name:
        print('Found')
    else:
        print('Not Found')


# ##### 'not in' keyword

# In[31]:


if 'Zach' not in l_teachers:
    print('Not a instructor')


# ##### Checking an Empty List

# In[33]:


# if l_1: or if l_1 = []
list_2 =[]

if list_2 == []:
    print('Yo')


# ##### Removing Instances with a Loop

# In[34]:


# while, remove
names = ['Evan','John', 'Jordan', 'Nani' ]

#while 'Evan' in names:
    #names.remove('Evan')
#print(names)

for name in names:
    if name -- 'Evan':
    names.remove('Evan')
print(names)


# ### List Exercise <br>
# <p>Remove all duplicates<br><b>Extra: Create a program that will remove any duplicates from a given list</b></p>

# In[47]:


names = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 2, 2, 2, 3, 3, 4, 'bob', 'kevin']
new_name = []
# Hint 1: You will need an append
# Hint 2: Using an empty list will make life easier
no_dupes = set(names)
print(no_dupes)



# ### List Comprehensions <br>
# <p>Creating a quickly generated list to work with<br>*result*  = [*transform*    *iteration*         *filter*     ]</p>

# ##### In a list comprehension we have a few pieces:
# 1. The first is the counter/ variable - IN this the variable is x
# 2. then we have a transform for the variable
# 3. The finale part of a list comp is called the condition
# 
# ```python
#     [transform, variable, condition]
# ```

# In[50]:


# number comprehension

# With a regular for loop
nums = []
for i in range(100):
    if i % 2 == 0:
        nums.append(i)
print(nums)

print('\n')
nums_comp = [i for i in range(100) if i % 2 == 0]
print(nums_comp)




# There are a few benefits to using List comprehensions. The most obvious would be that we now have shorter code to work with instead of using 3+ lines of code in the for loop variant.
# 
# Another is an added benefit to memory usage. Since the list's memory is allocated first before adding elements to it, we don't have to resize the list once we add elements to it.
# 
# Lastly, list comprehensions are considered the "pythonic" way to write code by the PEP8 standards (Python Style Guide)

# In[52]:


# square number comprehension
squares = [x ** 2 for x in range(10)]
print(squares)

square_reg = []
for x in range(10):
    square_reg.append(x**2)
print(square_reg)


# In[57]:


# string comprehension
names = ['Conner', 'Max', 'Evan', 'Rob']

first_char_comp = [name[0] for name in names]
print(first_char_comp)

first_char = []

for name in names:
    first_char.append(name[0])
print(first_char)




# In[63]:


c_names = [first_name for first_name in names if first_name[0] == 'C']
print(c_names)

c_names_reg = []

for first_name in names:
    if first_name[0] == "C":
        c_names_reg.append(first_name)
        
print(c_names_reg)


# In[ ]:





# ### Tuples <br>
# <p><b>Defined as an immutable list</b></p><br>Seperated by commas using parenthesis

# In[67]:


tup_1 = 1, 2, 3 #first way of creating a tuple
tup_2 = (1,2,3) #other way

print(tup_1[0])

print(len(tup_1))

#Loop
for number in tup_1:
    print(number)

    
for number in range(len(tup_1)):
    
    print(popped_num)
    


# ##### sorted()

# In[73]:


tup_3 = (20, 5, 1, 3, 9, 45)

sorted_tup =sorted(tup_3)
print(sorted_tup)

random_list = [3, 3, 66, 72, 33]
combine_list = sorted_tup + random_list

new_tup = tuple(combine_list)
print(new_tup)

print(type(sorted_tup))
print(tup_3)


# ##### Adding values to a Tuple

# In[75]:


print(tup_1)

tup_1 = tup_1 + (5,)
print(tup_1)


# ## Functions

# ##### User-Defined vs. Built-In Functions

# In[77]:


#User Defined-
def sayHello():
    return 'Hello World'

sayHello()


# ##### Accepting Parameters

# In[80]:


#Arguments or Parameter
#order Matter
# a variable can be any type of object

def printFullName(first_name, last_name):
    return f'Hello, {first_name} {last_name}'

a_name = 'Kevin'

printFullName('JJ', 'John')
printFullName(a_name, 'Apol')


# ##### Default Parameters

# In[81]:


#Default parameters need to be declared after non-default parameters

def printAgentName(first_name, last_name = 'Bond'):
    return f'The name is {last_name}.... {first_name}{last_name}'

print(printAgentName('James'))
#DOnt do this
def printAgentAgain(last_name = 'ever', first_name):
    return f' Last name {last name}, first name {first_name}'



# ##### Making an Argument Optional

# In[82]:


def printHorseName(first, middle = '', last = 'Ed'):
    return f'Hello {first} {middle} {last}'


printHorseName('Mr')


# ##### Keyword Arguments

# In[83]:


# last_name='Max', first_name='Smith' in the function call
def printSuperHero(name, power = 'flying'):
    return f' The heros name is {name} and superpower is {power}'

printSuperHero(power = 'Spidey Sense', name = 'Spiderman')
# see above


# # Creating a start, stop, step function

# In[85]:


def my_range(stop, start = 0, step = 1):
    for i in range(start,stop,step):
        print(i)
        
my_range(20)


# ##### Returning Values

# In[86]:


def addNums(num1, num2):
    return num1 + num2

addNums(1,2)


# ##### *args

# In[87]:


#arge == arguments, takes any number of argumets as parameters
#must be last if mutiple parameters are present

def printArgs(num1, *args, **kwargs):
    print(num1)
    print(args)
    
printArgs(16, 'Dragonlord', 'vanilla', 2,3, testing = 'joel')


# ##### Docstring

# In[88]:


def printNames(list_1):
    '''
     Function only accepts list
    '''
    for name in list_1:
        print(name)
printNames(['George', 'Justin', 'John'])


# ##### Using a User Function in a Loop

# In[89]:


def printInput(answer):
    print(answer)
response = input('Are you ready to Quit?')

while True:
    ask = input('What do you want to do?')
    printInput(ask)
    
    response = input('Ready Yet? ')
    if response.lower() == 'quit':
        break


# ## Function Exercise <br>
# <p>Write a function that loops through a list of first_names and a list of last_names, combines the two and return a list of full_names</p>

# In[94]:


first_name = ['John', 'Evan', 'Jordan', 'Max']
last_name = ['Smith', 'Smith', 'Williams', 'Bell']

# Output: ['John Smith', 'Evan Smith', 'Jordan Williams', 'Max Bell']

def fullName(list_1, list_2):
    new_list = []
    num = 0
    for i in list_1:
        new_list.append(list_1[num] + "  " + list_2[num])
        num += 1
    return new_list
    
    
fullName(first_name, last_name)


# ## Scope <br>
# <p>Scope refers to the ability to access variables, different types of scope include:<br>a) Global<br>b) Function (local)<br>c) Class (local)</p>

# In[ ]:


number = 3 #global

def myFunc():
    num_3 = 6 # local
    return num_3

print(number)
print(myFunc())


# # Exercises

# ## Exercise 1 <br>
# <p>Given a list as a parameter,write a function that returns a list of numbers that are less than ten</b></i></p><br>
# <p> For example: Say your input parameter to the function is [1,11,14,5,8,9]...Your output should [1,5,8,9]</p>

# In[96]:


# Use the following list - [1,11,14,5,8,9]

l_1 = [1,11,14,5,8,9]

def lessList(list_1):
    new_list = []
    for i in list_1:
        if i <= 10:
            new_list.append(i)
    return(new_list)

lessList(l_1)


# ## Exercise 2 <br>
# <p>Write a function that takes in two lists and returns the two lists merged together and sorted<br>
# <b><i>Hint: You can use the .sort() method</i></b></p>

# In[100]:


l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]

def comboList(list_1, list_2):
    new_list = []
    for i in list_1:
        new_list.append(i)
    for i in list_2:
        new_list.append(i)
    new_list.sort()
    return new_list

comboList(l_1,l_2)



# In[ ]:




