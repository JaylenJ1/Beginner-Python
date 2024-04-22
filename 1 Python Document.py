#!/usr/bin/env python
# coding: utf-8

# # Week 2 - Monday Lesson (variable assignment, loops, lists)

# ## Tasks Today:
# 
# 1) Int & Float assignments <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Assigning int <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Assigning float <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) Performing Calculations on ints and floats <br>
#  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Addition <br>
#  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Subtraction <br>
#  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Multiplication <br>
#  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Division <br>
#  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Floor Division <br>
#  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Modulo <br>
#  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Exponential <br>
# 2) String Input-Output <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) String Assignment <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) print() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) String Concatenation <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) Type Conversion <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) input() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; f) format() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; g) Old Way (python 2) <br>
# 3) <b>In-Class Exercise #1</b> <br>
# 4) If Statements <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) 'is' keyword <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) 'in' keyword <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) 'not in' keyword <br>
# 5) <b>In-Class Exercise #2</b> <br>
# 6) Elif Statements <br>
# 7) Else Statements <br>
# 8) <b>In-Class Exercise #3</b> <br>
# 9) For Loops <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Using 'in' keyword <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Continue Statement <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) Break Statement <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) Pass Statement <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) Double For Loops <br>
# 10) While Loops <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Looping 'While True' <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) While and For Loops Used Together <br>
# 11) Built-In Functions <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) range() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) len() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) help() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) isinstance() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) abs() <br>
# 12) Try and Except <br>
# 13) Lists <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Declaring Lists <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Indexing a List <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) .append() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) .insert() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) .pop() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; f) .remove() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; g) del() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; h) Concatenating Two Lists <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; i) Lists Within Lists <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; j) Looping Through Lists <br>

# ### Int & Float Assignments

# ##### Assigning int

# In[1]:


number = 6

print(number)


# ##### Assinging float

# In[2]:


numfloat = 2.3

print(numfloat)


# #### Performing Calculations on ints and floats

# ##### Addition

# In[3]:


numfloat + number 


# ##### Subtraction

# In[5]:


num1=1
num2=3.14
x = num2-num2
print(x)


# ##### Multiplication

# In[7]:


result_mul = num1 * num2

print(result_mul)


# ##### Division

# In[8]:


result_div = num2 / num1

print(result_div)


# ##### Floor Division

# In[10]:


rslt_floor = num2//num1
print(rslt_floor)


# ##### Modulo

# In[11]:


rslt_mod=num1/num2
print(rslt_mod)


# ##### Exponential

# In[13]:


sqaure = 5 **2
print(sqaure)


# ### String Input-Output

# ##### String Assignment

# In[ ]:


name = 'Jaylen'


# ##### print() <br>
# <p>Don't forget about end=' '</p>

# In[15]:


name = 'JJ'
print('This is my first name:',name)


# ##### String Concatenation

# In[16]:


name='John'
lastName='Smith'

fullName = name + ' '+ lastName
print(fullName)


# ##### Type Conversion

# In[17]:


num = "32"
change_type_num = int(num)
print(num)
print(change_type_num)


# ##### input()

# In[18]:


name = input('What is it?')
print('Nice to meet you' + name)


# ##### format()

# In[19]:


age = input('How old are you?')

result_age = 'You are {} {} and you grow wiser'.format(age, name)
print(result_age)


# ##### Old Way (python 2)

# In[ ]:





# # In-Class Exercise 1 <br>
# <p>Create a format statement that asks for color, year, make, model and prints out the results</p>

# In[21]:


color = input('What is your favorite color?')
year = input('What year were you born?')
model = input('What model do you use?')

result_statment = "Here are your statments, this is your favorite color {}, this is the year you were born {}, and here is your year model {}".format(color,year,model)
print(result_statment)


# ### If Statements

# In[23]:


# Available operators: Greater(>), Less(<),Equal(==)
# Greater or Equal(>=), Less or Equal (<=)

# Truth Tree:
# T && F = F
# T && T = T
# T || F = T
# F || T = T
# F || F = 
num = 5 
if num1 == 5: 
    print('This is True')
else:
    print("It is false")


# ##### 'is' keyword

# In[24]:


num3 = 55

if num3 is 55:
    print("Hello")


# ##### 'in' keyword

# In[25]:


char_name = "Frodo J"

if "Frodo" in char_name:
    print("The Ring B")


# ##### 'not in' keyword'

# In[26]:


sega_char = 'Sonic'

if 'a' not in sega_char:
    print('non')


# # In-Class Exercise 2 <br>
# <p>Ask user for input, check to see if the letter 'p' is in the input</p>

# In[30]:


user_input = input(' Enter your favorite word?')

if 'p' in user_input:
    print('Yes')


# ## Using 'and'/'or' with If Statements

# In[4]:


num_11 = 15
num_12 = 3
num_15 = 10
num_22 = 3

if num_11 / 5 == num_12 and num_15 - 7 == num_22:
    print("True and True")
if num_11 > num_15 or num_12 == num22:
    print('True and True')


# ### Elif Statements

# In[6]:


first_name=input("What is your name?")

if first_name == 'Smith':
    print("The name is Smith")
elif first_name == "Brandon":
    print("The name is Brandon")
else:
    print("WHat is your name?")


# ### Else Statements

# In[ ]:


# see above


# ### For Loops

# In[7]:


#for counter in condition
name = 'Jaylen Johnson'
for letters in name:
    print(letters)


# ##### Using 'in' keyword

# In[ ]:


# see above


# ##### Continue Statement

# In[ ]:


# will continue to next iteration


# In[8]:


for i in range(20):
    if i == 5:
        continue
    print(i)


# ##### Break Statement

# In[ ]:


# will break out of current loop


# In[9]:


for i in range(20):
    if i == 5:
        break
    print(i)


# ##### Pass Statement

# In[ ]:


# mostly used as a placeholder, and will continue on same iteration


# In[10]:


for i in name:
    pass


# ##### Double For Loops

# In[11]:


for i in range(5):
    for j in range(5):
        print('i = ', i, 'j = ',j)


# ### While Loops

# In[12]:


#while keyword, condition statment
num = 0

while num < 10:
    print(num)
    num +=1


# ##### Looping 'While True'

# In[ ]:


game_over = False

#while True:
    #print("Infinite Loop")
    #if game_over == False


# ##### While & For Loops Used Together

# In[ ]:


num = 0

while num < 5:
    print('While loop iteration' + str(num))
    
    for i in range()


# ### Built-In Functions

# ##### range()

# In[14]:


#range(start,stop,step)

for i in range(2,20):
    print(i)


# ##### len()

# In[16]:


name = input('Give me the name of your favorite book: ')

length = len(name)
print(length)


# ##### help()

# In[17]:


help(range)


# ##### isinstance()

# In[20]:


#Check a variable to find out what object family it belongs to
  
print(isinstance(4.5, int))


# ##### abs()

# In[21]:


#absolute value
print(abs(-5))


# ### Try and Except

# In[23]:


#Use this to log out gracefull and usefull error
#Does not stop program
try:
    number_test = 0
    input_num = int(input('Guess the Number  '))
    if input_num != input_num + number_test:
        input_num = input_num + number_test
        print('Your number is '+ str(input_num))
except:
    print("That didnt work Change your input to a number")
    


# ### Lists

# ##### Declaring Lists

# In[ ]:


list_1 = []

names = ['Max', 'Cindy', 'Kathy', 'Bob']


# ##### Indexing a List

# In[26]:


#list_name(start,stop,step)
names = ['Max', 'Cindy', 'Kathy', 'Bob']

#single index
print(names[0])

#prints starting at Index 1 going to the end 
print(names[1:])


# ##### .append()

# In[29]:


names.append('Brandon')
print(names)


# ##### .insert()

# In[30]:


names.insert(3,'Devon')
print(names)


# ##### .pop()

# In[32]:


#Defaults to the last value if no parameter is given
#Pop returns the element that was removed in case you want to assign it to a varabile 
my_name = names.pop(2)
print(names)


# 
# ##### .remove()

# In[ ]:


#Value to be removed
names.remove('Bob')
print(names)


# ##### del()

# In[33]:


#goes by index

del(names[1])
print(names)


# ##### Concatenating Two Lists

# In[ ]:


#list can hold lists
#will append two list together
#adding lists together


# ##### Lists Within Lists

# In[ ]:


nums = [1,3,7,7[4,7,8]]


# ##### Looping Through Lists

# In[34]:


#by index
for i in range(len(names)):
    print(names[i])


# ## Exercise #1 <br>
# <p>Cube Number Test... Print out all cubed numbers up to the total value 1000. Meaning that if the cubed number is over 1000 break the loop.</p>

# In[ ]:


num1 = 1

while num1 < 1000:
    cubed= num1 ** num1
    if cubed <= 1000:
        print(cubed)
        num1 +=1


# ## Exercise #2 <br>
# <p>Get first prime numbers up to 100</p>

# In[4]:


# HINT::
# An else after an if runs if the if didn’t
# An else after a for runs if the for didn’t break
num2 = 0

while num2 <= 100:
    if num2 % 2 != 0:
        print(num2)
    num2 += 1



# # Exercise 3 <br>
# <p>Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors</p>

# In[2]:


user_age = int(input('How Old are you?'))

if user_age < 18:
    print('Kid')
elif user_age > 18 and user_age < 65:
    print('Adult')
else:
    print('Seniors')


# In[ ]:





# In[ ]:




