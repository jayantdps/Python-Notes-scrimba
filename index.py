print('welcome to python 101')

item_name = 'widget'
price = 23.5
inventory = 100
in_in_inventory = True

print(item_name,price,inventory)

# arithmetic opertaion

a=10
b=3
print('Addition : ', a + b)
print('Subtraction : ', a - b)
print('Multiplication : ', a * b)
print('Division (float) : ', a / b)
print('Division (floor) : ', a // b)
print('Modulus : ', a % b)
print('Exponent : ', a ** b)


# string basics


msg='welcome to it\'s Python 101: Strings'
print(msg)
print(msg.upper())
print(msg.lower())
print(msg.capitalize())
print(msg.title())


# string functions

msg='welcome to Python 101: Strings'
print(msg)
print(len(msg))
print(msg.count('o'))

# string basics

msg='welcome to Python 101: Strings'
    #012345678
print(msg)
#slicing
print(msg[5])

# -1 gives the last character
print(msg[-1])

# 2: gives all after 2
print(msg[2:])


# 2:15 gives all after 2 and before 15
print(msg[2:15])

# :7 gives all before 7
print(msg[:7])

# excercise string basics

msg='welcome to Python 101: Strings'
msg1=msg[18]+' '+msg[:8]+msg[25:29]+msg[7:11]+msg[13]+msg[12]+msg[2]+msg[1]+msg[-5] 

print(msg1.title())

# print a string backword
print(msg1[::-1].title()) 

# find and replace

msg='Welcome to Python 101: Strings'
print(msg.find('Python'))

msg='Welcome to Python 101: Strings'
print(msg.replace('Python','Java'))

# to save a string
msg='Welcome to Python 101: Strings'
print(msg.replace('Python','C'))
msg1=msg.replace('Python','C')
print(msg1)

# exists or not
msg='Welcome to Python 101: Strings'
print('Python' in msg)
print('Python' not in msg)

# longer strings with variable
name='TERRY'
color = 'RED'
msg = '[' + name + '] loves the color ' + color.lower() + '!'
msg1 = f'[{name}] loves the color {color.lower()}!'
print(msg)
print(msg1)

# user input
name= input('What is your name?: ')
print(name)

name= input('What is your name?: ')
age=input('What is your age?: ')
print('Hello '+ name + '! You are '+ age + ' years old.')

# assignment
name = input('Enter your name: ')
distance_km = input('Enter distance in km: ')
distance_mi = float(distance_km)/1.609
print(f'Hi {name.title()}! {distance_km}km is equivalent to {distance_mi} miles.')

# round to decimal places
print(f'Hi {name.title()}! {distance_km}km is equivalent to {round(distance_mi,1)} miles.')


# lists same as array
friends = ['John','Michael','Terry','Eric','Graham']

print(friends[1],friends[4])

# to get the full list
print(friends[:])

# to get the length
print(len(friends))

#  to get the index
print(friends.index('Eric'))

# to count the indexes
print(friends.count('Eric'))

#  to sort list
friends = ['John','Michael','Terry','Eric','Graham']
cars = [911,130,328,535,740,308]
print(friends)


# to reverse the list in ascending order
friends.sort()
print(friends)

# to reverse the list in descending order
friends.sort(reverse=True)
print(friends)

# to reverse the string
friends.reverse()
print(friends)

# min in the list
print(min(cars))

# max in the list
print(max(cars))

# sum of the list
print(sum(cars))

# modifying list
friends.append('TerryG')
print(friends)

# insert values to a list
friends.insert(1,'TerryG')
print(friends)
friends[2]='TerryG'
print(friends)

# add list to a list
friends.extend(cars)
print(friends)

# remove values
friends.remove('Terry')
print(friends)

# pop values
# this can be used later in the program
friends.pop()
print(friends)

# pop at a place
friends.pop(2)
print(friends)

friends.pop(-1)
print(friends)

# empty list
friends.clear()
print(friends)

# delete list
del friends
print(friends)

# delete an index
del friends[2]
print(friends)

# copy of a list
friends = ['John','Michael','Terry','Eric','Graham']
# method 1
new_friends = friends[:]
print(friends)
print(new_friends)
# method 2
new_friends = friends.copy()
print(new_friends)
# method 3
new_friends = list(friends)
print(friends)
print(new_friends)

# assignment
sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []
new_day = input('Enter #of lemonades for new day: ')
sales_w2.append(int(new_day))
sales.extend(sales_w1)
sales.extend(sales_w2)
#sales = sales_w1 + sales_w2
sales.sort()
worst_day_prof = sales[0] * 1.5
best_day_prof = sales[-1] * 1.5
print(f'Worst day profit:$ {worst_day_prof}')
print(f'Best day profit:$ {best_day_prof}')
print(f'Combined profit:$ {worst_day_prof + best_day_prof}')

# without sorting the list
sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []
new_day = input('Enter #of lemonades for new day: ')
sales_w2.append(int(new_day))
#sales.extend(sales_w1)
#sales.extend(sales_w2)
sales = sales_w1 + sales_w2
#sales.sort()
worst_day_prof = min(sales) * 1.5
best_day_prof = max(sales) * 1.5
print(f'Worst day profit:$ {worst_day_prof}')
print(f'Best day profit:$ {best_day_prof}')
print(f'Combined profit:$ {worst_day_prof + best_day_prof}')

# strings to list (split and join function)
msg ='Welcome to Python 101: Split and Join'
csv = 'Eric,John,Michael,Terry,Graham'
friends_list = ['Eric','John','Michael','Terry','Graham']
# below command splits the string to each characters
print(list(msg))
# output
# ['W', 'e', 'l', 'c', 'o', 'm', 'e', ' ', 't', 'o', ' ', 'P', 'y', 't', 'h', 'o', 'n', ' ', '1', '0', '1', ':', ' ', 'S', 'p', 'l', 'i', 't', ' ', 'a', 'n', 'd', ' ', 'J', 'o', 'i', 'n']

# string to each word in a list
print(msg.split())
# output
# ['Welcome', 'to', 'Python', '101:', 'Split', 'and', 'Join']

# split using a space
print(msg.split(' '))

print(msg.split(','))

# join command
print('-'.join(friends_list))
# output
# Eric-John-Michael-Terry-Graham

# one long string
friends_list = ['Eric','John','Michael','Terry','Graham']
print(''.join(friends_list))
# output
# EricJohnMichaelTerryGraham

# 
#  we split for a list and join for a string
# 

# replace on a string
print(''.join(msg.split()))
print(msg.replace(' ', ''))

# excercise

csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
print(','.join(csv.split(';')))
print(','.join(csv.split(';')).split(':'))
print(','.join(','.join(csv.split(';')).split(':')))
print(','.join((','.join(csv.split(';')).split(':'))).split(','))
friends_list = ['Exercise: fill me with names']
print(friends_list)

# step 2
csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'

print((','.join(','.join(csv.split(';')).split(':'))).split(','))
friends_list = (','.join(','.join(csv.split(';')).split(':'))).split(',')
print(friends_list)

# From the list above fill a list(friends_list) properly
# with the names of all the friends. One per "slot"
# you may need to run same command several times
# use print() statements to work your way through the exercise

# second method using replace

csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'


friends_list = (','.join(','.join(csv.split(';')).split(':'))).split(',')
print(friends_list)
print('replace', csv.replace(';',',').replace(':',',').split(','))
# From the list above fill a list(friends_list) properly
# with the names of all the friends. One per "slot"
# you may need to run same command several times
# use print() statements to work your way through the exercise

 #Tuples - faster Lists you can't change
friends = ['John','Michael','Terry','Eric','Graham']
friends_tuple = ('John','Michael','Terry','Eric','Graham')
print(friends)
# tuples user () instead of []

#Sets - blazingly fast unordered Lists 
friends = ['John','Michael','Terry','Eric','Graham']
friends_tuple = ('John','Michael','Terry','Eric','Graham')
friends_set = {'John','Michael','Terry','Eric','Graham','Eric'}
print(friends)
print(friends_tuple)
print(friends_set)
# sets user {} instead of [], no repetition allowed

# intersection and different
friends = ['John','Michael','Terry','Eric','Graham']
friends_tuple = ('John','Michael','Terry','Eric','Graham')
friends_set = {'John','Michael','Terry','Eric','Graham','Eric'}
my_friends_set = {'Reg','Loretta','Colin','Eric','Graham'}

print(friends_set.difference(my_friends_set))

print(friends_set.intersection(my_friends_set))


print(friends_set.union(my_friends_set))


# 
#Sets - blazingly fast unordered Lists 
#empty Lists
empty_list = []
empyt_list = list()

#empty Tuple
empty_tuple = ()
empty_tuple = tuple()

#empty Set
empty_set = {} # this is wrong, this is a dictionary
empty_set = set()
# 

#Sets - Exercise

#1. Check if ‘Eric’ and ‘John’ exist in friends
#2. combine or add the two sets 
#3. Find names that are in both sets
#4. find names that are only in friends
#5. Show only the names who only appear in one of the lists
#6. Create a new cars-list without duplicates

friends = {'John','Michael','Terry','Eric','Graham'}
my_friends = {'Reg','Loretta','Colin','John','Graham'}
cars =['900','420','V70','911','996','V90','911','911','S','328','900']

print('Eric' in friends and 'John' in friends)
print(friends.union(my_friends))
print(friends | my_friends)

print('Eric' in friends and 'John' in friends)
print(friends.intersection(my_friends))
print(friends & my_friends)

print('Eric' in friends and 'John' in friends)
print(friends.difference(my_friends))
print(friends - my_friends)

print('Eric' in friends and 'John' in friends)
print(my_friends.difference(friends))
print(my_friends - friends)


print('Eric' in friends and 'John' in friends)
print(my_friends.symmetric_difference(friends))
print(my_friends ^ friends)

print('Eric' in friends and 'John' in friends)
print(my_friends.symmetric_difference(friends))
print(my_friends ^ friends)
cars_no_dupl =set(cars)
print(cars_no_dupl)

print('Eric' in friends and 'John' in friends)
print(my_friends.symmetric_difference(friends))
print(my_friends ^ friends)
cars_no_dupl =list(set(cars))
print(cars_no_dupl)


# functions
def greeting():
    print("Hello Friend!")
    
greeting()

# function with argument
def greeting(name):
    print("Hello " + name + "!")
    
greeting("Brian")

# 

def greeting(name,age):
    print("Hello " + name + ", you are " + age + "!")
    print(f"Hello {name}, you are {age}!")
    
greeting("Brian","32")

# default parameter
def greeting(name,age="28"):
    print("Hello " + name + ", you are " + age + "!")
    print(f"Hello {name}, you are {age}!")
    
greeting("Brian","32")
greeting("Judith")


# excercise

def greeting(name, age=28):
    #Greets user with 'name' from 'input box' and 'age', if available, default age is used
    print('Hello '  +  name + ', you are ' + str(age) +'!')
    print(f'Hello {name}, you are {age}!')
    

name = input('Enter your name: ')
age = input('Enter your age: ')
greeting(name, 32)
# 1. Add new print statement - on a new line
#    which says 'We hear you like the color xxx! xxx is a string with color 
# 2. extend the function with another  input parameter 'color', that defaults to 'red'
# 3. Capture the color via an input box as variable:color 
# 4. Change the 'You are xx!' text to say 'you will be xx+1 years old next birthday 
#  adding 1 to the age
# 5. Capitalize first letter of the 'name', and rest are small caps 
# 6. Favorite color should be in lowercase 


def greeting(name, age=28, color = 'red'):
    #Greets user with 'name' from 'input box' and 'age' next year, if available, default age is used
    # also includes favorite color
    print('Hello '  +  name.capitalize() + ', you will be ' + str(age+1) +' next birthday!')
    print(f'Hello {name.capitalize()}, you will be {age+1} next birthday!')
    print(f'We hear you like the color {color.lower()}!')

name = input('Enter your name: ')
age = input('Enter your age: ')
color = input('Enter favorite color: ')
greeting(name, int(age), color)

# named notation
def greeting(name, age=28, color="red"):
 #Greets user with “name” from “input box” and “age”, if unavailable, default age is used   
   
   print(f"Hello {name.capitalize()}, you will be {age+1} next birthday!")
   print(f"We hear you like the color {color.lower()}!")

greeting(age=27, name="brian",color="Blue")

# return statements
def value_added_tax(amount):
    tax = amount * 0.25
    return tax
    
print(value_added_tax(100))
# output
# 25.0

# return can be anything from a function
def value_added_tax(amount):
    tax = amount * 0.25
    total_amount = amount * 1.25
    return f"{amount}, {tax}, {total_amount}"
    
price = value_added_tax(100)    
print(price, type(price))

# comparisons
a = [3,7,42]
b = [3,7,42]
print(a == b)
print(a is b)
print(id(a), id(b))

a=7
b=3
print('a == b is', a == b)
print('a != b is', a != b)
print('a > b is', a > b)
print('a < b is', a < b)
print('a >= b is', a >= b)
print('a <= b is', a <= b)
print('o in John is ','o' in 'John') #membership
print('o in John is ','o' not in 'John') #non membership
print('John is John ','John' is 'John') #identity
print('John is not John is ','John' is not 'John') # negative identity

# conditionals: if,Else, Elif
is_raining = True
print("Good Morning")
if is_raining:
    print("Bring Umbrella")

# 
is_raining = False
is_cold = False
print("Good Morning")
if is_raining or is_cold:
    print("Bring Umbrella or jacket or both")
else:
    print("Umbrella is optional")

# 
is_raining = False
is_cold = False
print("Good Morning")
if is_raining and is_cold:
    print("Bring Umbrella and jacket")
elif is_raining and not(is_cold):
    print("Bring Umbrella")
elif not(is_raining) and is_cold:
    print("Bring Jacket")
else:
    print("Umbrella is optional")

# 
amount = 20
if amount <= 50:
    print("Purchase approved")
else:
    print("Please enter your pin!")

# assignment with answer
mode = input('Enter math operation(+,-,*,/) or f for Celsius to Fahrenheit conversion: ')
num1 = float(input('Enter first number: '))
if mode.lower() == 'f':
    print(f'{num1} Celsius is equivalent to {(num1*9/5)+32 } fahrenheit')
else:
    num2 = float(input('Enter second number: '))

    if mode == '+':
        print(f'Answer is: {num1 + num2}')
    elif mode == '-':
        print(f'Answer is: {num1 - num2}')
    elif mode == '*':
        print(f'Answer is: {num1 * num2}')
    elif mode == '/':
        print(f'Answer is: {num1 / num2}')
    else:
        print('Input error!')
# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs 
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f

# improving conditionals
def num_days(month):
    days = 31
    if month in {'apr','jun','sep','nov'}:
    #if month == 'apr' or month =='jun' or month =='sep' or month =='nov':
        days = 30
    elif month == 'feb':
        days = 28
    print('number of days in',month,'is',days)
    

num_days('jan')
# optimize/shorten the code in the function
# try to reduce the number of conditionals 

# 


# while loops
"""while condition: 
      code
      iterator"""
# Three Loop Questions:
#1. What do I want to repeat?
#  -> 
#2. What do I want to change each time?
#  -> 
#3. How long should we repeat?
#  -> 

i=0
while i < 5:
    i=i+1
    print(f"{i}."+ "*"*i + "Loops are awesome" + "*"*i)

# output
"""
1.*Loops are awesome*
2.**Loops are awesome**
3.***Loops are awesome***
4.****Loops are awesome****
5.*****Loops are awesome*****
"""

# while excercise
print('Guessing game') 
# Guess the correct number in 3 guesses. If you don’t get it right after 3 guesses you lose the game. 
# Give user input box: 1. To capture guesses, 
# print(and input boxes) 1. If user wins 2. If user loses
# Tip:( remember you won’t see  print statements durng execution, so If you want to see prints during whle loop, then print to the input box

#Modification 1: number 1-100, tell user if guess is too high/low ,and let them have 5-10 guesses.
# Tip:( remember you won’t see  print statements during execution, so If you want to see prints during whle loop, print to the input box (This is specific to this platform)
# Three Loop Questions:
#1. What do I want to repeat?
#  -> guesses
#2. What do I want to change each time?
#  -> guess number and number of guesses
#3. How long should we repeat?
#  -> until user loses, runs out of guesses, or wins

num = 76
guess = 0
guess_limit=5
guess_number = 0
guess = int(input(f'Guess a number 1-100: '))
guess_number +=1
while guess_number < guess_limit:
    
    if guess != num:
        guess_number +=1
        if guess > num:
            guess = int(input(f'{guess} Too high - Guess again 1-100: '))
        else:
            guess = int(input(f'{guess} too low - Guess again 1-100: '))
    if guess == num:
        print(f'You Win! You Guessed it: {guess}')
        break
    
if guess != num:
    print(f'Sorry you lose! It was {num}')
#
 
# for loops
for letter in 'Norwegian blue':
    print(letter)

print("For Loop done!")

# another way
for furgle in range(1,15,3):
    print(furgle)

print("For Loop done!")

# another way
friends = ['John','Terry','Eric','Michael','George']
for friend in friends:
    print(friend)

print("For Loop done!")

# 
friends = ['John','Terry','Eric','Michael','George']
for friend in friends:
    if friend == 'Eric':
        print('Found' + friend + '!')
        break
    print(friend)

print("For Loop done!")
# output
"""John
Terry
FoundEric!
For Loop done!
"""

# 
friends = ['John','Terry','Eric','Michael','George']
for friend in friends:
    if friend == 'Eric':
        print('Found ' + friend + '!')
        continue
    print(friend)

print("For Loop done!")
# output
"""
John
Terry
Found Eric!
Michael
George
For Loop done!
"""

# nesting for loop
friends = ['John','Terry','Eric']
for friend in friends:
    for number in [1,2,3]:
        print(friend, number)

print("For Loop done!")
# output
"""
John 1
John 2
John 3
Terry 1
Terry 2
Terry 3
Eric 1
Eric 2
Eric 3
For Loop done!
"""

# print name with msg using for loop
names = ['john ClEEse','Eric IDLE','michael']
names1 = ['graHam chapman', 'TERRY', 'terry jones']
msg = 'You are invited to the party on saturday.'
#names.extend(names1)
names += names1
for index in range(2):
    names.append(input('Enter a new name: '))

for name in names:
    #msg1 = f'{name.title()}! {msg}'
    msg1 = name.title() + '! ' + msg
    print(msg1)
# output
"""
john ClEEse! You are invited to the party on saturday.
Eric IDLE! You are invited to the party on saturday.
michael! You are invited to the party on saturday.
graHam chapman! You are invited to the party on saturday.
TERRY! You are invited to the party on saturday.
terry jones! You are invited to the party on saturday.
john jay! You are invited to the party on saturday.
jamie lee! You are invited to the party on saturday.
"""

# enumerate function
print('python101 - Enumerate')
friends = ['Brian', 'Judith', 'Reg', 'Loretta', 'Colin']
for num, friend in enumerate(friends,1):
    print(num, friend)

print(type(enumerate(friends)))
print(list(enumerate(friends)))
# output
"""
python101 - Enumerate
1 Brian
2 Judith
3 Reg
4 Loretta
5 Colin
"""

# Dictionaries : key - value pair
movie = {
    'title' : 'Life of Brian',
    'year' : 1979,
    'cast' : ['John','Eric','Michael','George','Terry']
}
print(movie)
# use .get() 
print(movie.get('budget'))
 
# example 
movie = {
    'title' : 'Life of Brian',
    'year' : 1979,
    'cast' : ['John','Eric','Michael','George','Terry']
}
movie.update({'title' : 'The Holy Grail','year':1975,'cast':['John','Eric','Michael','George','Terry']})
movie['budget'] = 250000
del movie['year']
print(movie)

# example
movie = {
    'title' : 'Life of Brian',
    'year' : 1979,
    'cast' : ['John','Eric','Michael','George','Terry']
}
movie.update({'title' : 'The Holy Grail','year':1975,'cast':['John','Eric','Michael','George','Terry']})
movie['budget'] = 250000
year = movie.pop('year')
print(movie)
print(year)
print(len(movie))
print(movie.keys())
print(movie.values())
print(movie.items())

# loop for items in a disctionary
for key in movie:
    print(key)

# printing key and values
for key, value in movie.items():
    print(key,value )   

# dictionary update 3 methods
python = {'John':35,'Eric':36,'Michael':35,'Terry':38,'Graham':37,'TerryG':34}
holy_grail = {'Arthur':40,'Galahad':35,'Lancelot':39,'Knight of NI':40, 'Zoot':17}
life_of_brian = {'Brian':33,'Reg':35,'Stan/Loretta':32,'Biccus Diccus':45}
#membership test
print('Arthur' in holy_grail)
if 'Arthur' not in python:
    print('He\'s not here!')

people = {}
people1 = {}
people2 = {}
#method 1 update
people.update(python)
people.update(holy_grail)
people.update(life_of_brian)
print(people)
#method 2 comprehension
for groups in (python,holy_grail,life_of_brian) : people1.update(groups)
print(people1)
#method 3 unpacking 3.5 later
people2 = {**python,**holy_grail,**life_of_brian}
print(people2)

# sorted dictionaries
print(sorted(people.items()))
#method 2 comprehension
for groups in (python,holy_grail,life_of_brian) : people1.update(groups)
print(sorted(people1.items()))

# dictionary assignment
#It’s...not really an adventure game...#Ver 1.0
#Your village is being attacked by 'a germanic tribe' and you need to run to the stores and get the right things to save your village, and probably some good looking girl or boy you want to marry. All prices in gold pieces excl. VAT... chop chop!! ze germanz are coming!
#The code should allow you to get 1 thing from each store and each item you get should be removed from the store inventory, then do same for next store...
# one way to buy by typing the key 'newt' in an input box...or something
# at end you should print the 'items' you have taken..in this version you don't have to pay for stuff or add it up
#ver 1.2 add ability to exit a store without buying and go to next by typing 'exit', and to exit if a nonexistant item is bought(typed)
# Add purse with 1000 gold pieces and payment for the items during or at end of code and show a message about total cost and how much gold you have left
#ver 1.4 random bug fix, ' browser compatability', refactoring code... basically being lazy ..stop scrolling TikTok/Facebook! ;-)
#Ver 1.5 print inventory before and after purchases as one department_store of stuff(combine inventories from all stores into one...pretend Big Biz bought all the local stores, and want constant reporting for inventory management...)
# as in all games there is a special way to do this that actually makes money and solves the problem...can you find 'them'? Do you know why? May require knowledge of actual python 'lore'

#create stores
freelancers = {'name':'freelancing Shop','brian': 70, 'black knight':20, 'biccus diccus':100, 'grim reaper':500, 'minstrel':-15}
antiques = {'name':'Antique Shop','french castle':400, 'wooden grail':3, 'scythe':150, 'catapult':75, 'german joke':5}
pet_shop = {'name':'Pet Shop','blue parrot':10, 'white rabbit':5, 'newt': 2}

#create an dempty shopping cart
cart = {}
#loop through stores/dicts
for shop in (freelancers,antiques) :
    #inputbox  to show what you can buy...capture textstring of what was bought...make lowercase
    buy_item = input(f'Welcome to {shop["name"]}! what do you want to buy: {shop}').lower()
    #update the cart
    cart.update({buy_item:shop.pop(buy_item)}) # use pop...
print(f'You Purchased {cart.keys()} Today it is all free. Have a nice day of mayhem!')

# output
"""
You Purchased dict_keys(['brian','catapult']) Today it is all free. Have a nice day of mayhem!
"""

# print another way
print(f'You Purchased {", ".join(list(cart.keys()))} Today it is all free. Have a nice day of mayhem!')

# output
"""
›You Purchased grim reaper, scythe Today it is all free. Have a nice day of mayhem!
"""
# dictionary assignment ends

# dictionary assignment 2 with solutions

#It’s...not really an adventure game...#Ver 1.0
#Your village is being attacked by 'a germanic tribe' and you need to run to the stores and get the right things to save your village, and probably some good looking girl or boy you want to marry. All prices in gold pieces excl. VAT... chop chop!! ze germanz are coming!
#The code should allow you to get 1 thing from each store and each item you get should be removed from the store inventory, then do same for next store...
# one way to buy by typing the key 'newt' in an input box...or something
# at end you should print the 'items' you have taken..in this version you don't have to pay for stuff or add it up
#ver 1.2 add ability to exit a store without buying and go to next by typing 'exit', and to exit if a nonexistant item is bought(typed)
# Add purse with 1000 gold pieces and payment for the items during or at end of code and show a message about total cost and how much gold you have left
#ver 1.4 random bug fix, ' browser compatability', refactoring code... basically being lazy ..stop scrolling TikTok/Facebook! ;-)
#Ver 1.5 print inventory before and after purchases as one department_store of stuff(combine inventories from all stores into one...pretend Big Biz bought all the local stores, and want constant reporting for inventory management...)
# as in all games there is a special way to do this that actually makes money and solves the problem...can you find 'them'? Do you know why? May require knowledge of actual python 'lore'

#create stores
freelancers = {'name':'freelancing Shop','brian': 70, 'black knight':20, 'biccus diccus':100, 'grim reaper':500, 'minstrel':-15}
antiques = {'name':'Antique Shop','french castle':400, 'wooden grail':3, 'scythe':150, 'catapult':75, 'german joke':5}
pet_shop = {'name':'Pet Shop','blue parrot':10, 'white rabbit':5, 'newt': 2}

#create an dempty shopping cart
cart = {}
#create purse with 100Gp
purse = 1000
#loop through stores/dicts
for shop in (freelancers,antiques,pet_shop) :
    #inputbox  to show what you can buy...capture textstring of what was bought...make lowercase
    buy_item = input(f'Welcome to {shop["name"]}! (type exit to exit store) what do you want to buy: {shop}').lower()
    #exit on exit typed or buying nonexistant item
    if buy_item == 'exit':
        continue
    if buy_item not in shop:
        continue
        
    #update the cart
    cart.update({buy_item:shop.pop(buy_item)}) # use pop...
    buy_items = ", ".join(list(cart.keys()))
print(f'You Purchased {buy_items}. Your total is {sum(cart.values())} Gp. Your change is {purse - sum(cart.values())} Gp. Have a nice day of mayhem!')

# output
"""
You Purchased grim reaper, catapult, white rabbit. Your total is 580 Gp. Your change is 420 Gp. Have a nice day of mayhem!
"""

# final code for dictionary problem
#It’s...not really an adventure game...#Ver 1.0
#Your village is being attacked by 'a germanic tribe' and you need to run to the stores and get the right things to save your village, and probably some good looking girl or boy you want to marry. All prices in gold pieces excl. VAT... chop chop!! ze germanz are coming!
#The code should allow you to get 1 thing from each store and each item you get should be removed from the store inventory, then do same for next store...
# one way to buy by typing the key 'newt' in an input box...or something
# at end you should print the 'items' you have taken..in this version you don't have to pay for stuff or add it up
#ver 1.2 add ability to exit a store without buying and go to next by typing 'exit', and to exit if a nonexistant item is bought(typed)
# Add purse with 1000 gold pieces and payment for the items during or at end of code and show a message about total cost and how much gold you have left
#ver 1.4 random bug fix, ' browser compatability', refactoring code... basically being lazy ..stop scrolling TikTok/Facebook! ;-)
#Ver 1.5 print inventory before and after purchases as one department_store of stuff(combine inventories from all stores into one...pretend Big Biz bought all the local stores, and want constant reporting for inventory management...)
# as in all games there is a special way to do this that actually makes money and solves the problem...can you find 'them'? Do you know why? May require knowledge of actual python 'lore'

#create stores
freelancers = {'name':'freelancing Shop','brian': 70, 'black knight':20, 'biccus diccus':100, 'grim reaper':500, 'minstrel':-15}
antiques = {'name':'Antique Shop','french castle':400, 'wooden grail':3, 'scythe':150, 'catapult':75, 'german joke':5}
pet_shop = {'name':'Pet Shop','blue parrot':10, 'white rabbit':5, 'newt': 2}
#morning inventory
department_store = {}
for department in (freelancers, antiques, pet_shop) :department_store.update(department)
department_store.pop('name')
print('Morning inventory of stores', sorted(department_store.items()))
print('-----------------')
#create an dempty shopping cart
cart = {}
#create purse with 100Gp
purse = 1000
buy_items1 = ''
#loop through stores/dicts
for shop in (freelancers,antiques,pet_shop) :
    #inputbox  to show what you can buy...capture textstring of what was bought...make lowercase
    buy_item = input(f'Welcome to {shop["name"]}! (type exit to exit store) what do you want to buy: {shop}').lower()
    #exit on exit typed or buying nonexistant item
    if buy_item == 'exit':
        continue
    if buy_item not in shop:
        continue
    #update string
    buy_items1 = buy_items1 + f'{buy_item}:{shop[buy_item]} Gp, '    
    #update the cart
    cart.update({buy_item:shop.pop(buy_item)}) # use pop...
    buy_items = ", ".join(list(cart.keys()))
    total_sum = sum(cart.values())
print(f'You Purchased {buy_items}. Your total is {total_sum} Gp. Your change is {purse - total_sum} Gp. Have a nice day of mayhem!')
print(f'You Purchased {buy_items1}. Your total is {total_sum} Gp. Your change is {purse - total_sum} Gp. Have a nice day of mayhem!')
#evening inventory
department_store_after = {**freelancers, **antiques, **pet_shop} #pyth 3.5
department_store_after.pop('name')
print('-----------------')
print('Evening inventory of stores', sorted(department_store_after.items()))

# output
"""
Morning inventory of stores [('biccus diccus', 100), ('black knight', 20), ('blue parrot', 10), ('brian', 70), ('catapult', 75), ('french castle', 400), ('german joke', 5), ('grim reaper', 500), ('minstrel', -15), ('newt', 2), ('scythe', 150), ('white rabbit', 5), ('wooden grail', 3)]
-----------------
You Purchased minstrel, german joke, white rabbit. Your total is -5 Gp. Your change is 1005 Gp. Have a nice day of mayhem!
You Purchased minstrel:-15 Gp, german joke:5 Gp, white rabbit:5 Gp, . Your total is -5 Gp. Your change is 1005 Gp. Have a nice day of mayhem!
-----------------
Evening inventory of stores [('biccus diccus', 100), ('black knight', 20), ('blue parrot', 10), ('brian', 70), ('catapult', 75), ('french castle', 400), ('grim reaper', 500), ('newt', 2), ('scythe', 150), ('wooden grail', 3)]
scrimba
Learn Python for free
Dictionaries Exercise v 1.2, 1.5


"""

# reading files in python
my_file = open('greeting.txt','r') #w, a
print(my_file.read(10))
print(my_file.readline())
print(my_file.readline())

line_by_line = my_file.readlines()
line_by_line1 = my_file.read().splitlines()
print('readlines: ',line_by_line)
print('splitlines: ',line_by_line1)
my_file.close()

# reading file with open command
with open('friends.csv','r') as f:
    print(f.read())
    friends = f.read().splitlines()
    print(friends)
    for friend in friends:
        friend = friend.split(',')
        name = friend[0]
        year = int(friend[1].strip())
        print(f'In 2030 {name} will be {2030 -year} years old')

# 
with open('movies.txt','r') as f:
    #for line in f: #not in scrimba
    for line in f.readlines(): #Scrimba workaround
        print(line)

# 

# Exceptions: try/except,raise

#try:
    #code you want to run
#except:
    #executed if error occurs
#else:
    #executed if no error
#finally:
    #always executed 

""" example """
try:
    num=int(input('Enter a number between 1 and 30: '))
    num1 = 30/num
    if num > 30:
        raise ValueError(num)
except ZeroDivisionError as err:
    print(err, "You can't divide by Zero!!!")
except ValueError as err:
    print(err,num, "Bad Value not between 1 and 30!")
except:
    print("Invalid Input!")
else:
    print("30 divided by",num, "is: ", 30/num)
finally:
    print("**Thank you for playing!**")

""" example ends"""

# classes and objects

#Classes are blueprints
#Objects are the actual things you built
#variables => attributes
#functions => methods

# 
class Movie:
    def __init__(self,title,year,imdb_score,have_seen):
        self.title = title
        self.year = year
        self.imdb_score = imdb_score
        self.have_seen = have_seen
    
    def nice_print(self):
        print("Title: ", self.title)
        print("Year of production: ", self.year)
        print("IMDB Score: ", self.imdb_score)
        print("I have seen it: ", self.have_seen)
        
film_1 = Movie("Life of Brian",1979,8.1,True)
film_2 = Movie("The Holy Grail",1975,8.2,True)

#print(film_1.title, film_1.imdb_score)
film_2.nice_print()

"""output:

Title: The Holy Grail
Year of production: 1975
IMDB Score: 8.2
I have seen it: True

"""


# 
class Movie:
    def __init__(self,title,year,imdb_score,have_seen):
        self.title = title
        self.year = year
        self.imdb_score = imdb_score
        self.have_seen = have_seen
    
    def nice_print(self):
        print("Title: ", self.title)
        print("Year of production: ", self.year)
        print("IMDB Score: ", self.imdb_score)
        print("I have seen it: ", self.have_seen)
        
film_1 = Movie("Life of Brian",1979,8.1,True)
film_2 = Movie("The Holy Grail",1975,8.2,True)

films = [film_1,film_2]
print(films[1].title,films[0].title)
films[0].nice_print()

# inheritence
class Person:
    def move(self):
        print("Moves 4 paces")
    def rest(self):
        print("Gains 4 health points")
class Doctor(Person):
    def heal(self):
        print("Heals 10 health points")
    
character1=Doctor()
character1.heal()


# example
class Person:
    def move(self):
        print("Moves 4 paces")
    def rest(self):
        print("Gains 4 health points")
class Doctor(Person):
    def heal(self):
        print("Heals 10 health points")

class Fighter(Person):
    def fight(self):
        print("Do 10 health points of damage")
    def move(self):
        print("Moves 6 paces")
        
class Wizard(Doctor,Fighter):
    def cast_spell(self):
        print("Turns invisble")
    def heal(self):
        print("Heals 15 health points")
    
    
character1=Wizard()
character1.move()

# modules

# https://docs.python.org/3/py-modindex.html

import platform

print(dir(platform))

print(platform.python_version())

# another way as alias

import platform as pl

print(pl.python_version())

# zip and unzip
nums = [1,2,3,4] 
letters = ['a','b','c','d']
names =['John','Eric','Michael','Graham','Joe']
combo = list(zip(nums,letters))
print(combo)
# output
[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]

combo = dict(zip(nums,letters))
print(combo)
# output
{'1': 'a', '2': 'b', '3': 'c', '4': 'd'}

# unzip
num,let,nam =zip(*combo)
print(num,let,nam)
"""
output

[('1', 'a', 'John'), ('2', 'b', 'Eric'), ('3', 'c', 'Michael'), ('4', 'd', 'Graham')]
›('1', '2', '3', '4') ('a', 'b', 'c', 'd') ('John', 'Eric', 'Michael', 'Graham')
"""

# zip unzip for dictionary
keys = 'this parrot is deceased'
values = 'denna papegojan är avliden'
keys = keys.split()
values = values.split()
print(keys,values)
en_sv_dict = dict(zip(keys,values))
print(en_sv_dict)
new_dict = {key:value for key,value in zip(keys,values)}
print(new_dict)
en,sv = list(en_sv_dict.keys()),list(en_sv_dict.values())
print(en,sv)

# output
"""
['this', 'parrot', 'is', 'deceased'] ['denna', 'papegojan', 'är', 'avliden']
{'this': 'denna', 'parrot': 'papegojan', 'is': 'är', 'deceased': 'avliden'}
{'this': 'denna', 'parrot': 'papegojan', 'is': 'är', 'deceased': 'avliden'}
['this', 'parrot', 'is', 'deceased'] ['denna', 'papegojan', 'är', 'avliden']

"""

# lamda functions
def square(x):
    return x*x
#name = lambda parameter(s): expression
square1 = lambda x: x*x

print(square1(3))

# ordered list by first name
monty_python = ['John Marwood Cleese','Eric Idle','Michael Edward Palin','Terrence Vance Gilliam','Terry Graham Perry Jones', 'Graham Arthur Chapman']

monty_python.sort(key = lambda name:name.split(' '))
print(monty_python)

# ordered by last name
monty_python = ['John Marwood Cleese','Eric Idle','Michael Edward Palin','Terrence Vance Gilliam','Terry Graham Perry Jones', 'Graham Arthur Chapman']

monty_python.sort(key = lambda name:name.split(' ')[-1])
print(monty_python)

# lamda functions

def price_calc(start,hourly_rate):
    return lambda hours: start + hourly_rate * hours
    
walkin_cost = price_calc(10,30)
premium_cost = price_calc(1,25)
print(walkin_cost(2))
print(premium_cost(2))
print(price_calc(1,25)(2))

print((lambda a,b,c: a+b+c)(2,3,4))
print((lambda a,b,c=2: a+b+c)(2,3,4))
print((lambda a,b,c=2: a+b+c)(2,c=3,b=4))
print((lambda *args: sum(args))(2,3,4,50))


# comprehensions-Lists
"""(anything you can do with comprehension can be done with for loop)"""

numbers = [1,2,3,4,5,6,7,8,9]
# give me a list with num squared for each num in numbers
new_list = []
for num in numbers:
    new_list.append(num*num)
print(new_list)
# compre method
new_list = [num*num for num in numbers]
print(new_list)

# give me a list with num for each num in numbers if num is even 
new_list = [num for num in numbers if num % 2 == 0]
print(new_list)

# give me a list with num for each num in numbers if num is even 
new_list = [num for num in numbers if num % 2 == 1]
print(new_list)

# Dictionary comprehensions
movies = ["And Now for Something Completely Different","Monty Python and the Holy Grail",
"Monty Python's Life of Brian","Monty Python Live at the Hollywood Bowl","Monty Python's The Meaning of Life","Monty Python Live (Mostly)"]
year =[1971,1975,1979,1982,1983,2014]
names = ['John','Eric','Michael','Graham','Terry','TerryG']
print(list(zip(movies, year)))
# give me a dict('movies': year) for each movies, year in zip(movies, year)
new_dict = dict()
for movie, yr in zip(movies,year):
    new_dict[movie] = yr
print(new_dict)

new_dict = {movie:yr for movie,yr in zip(movies,year) if yr < 1983 and movie.startswith('Monty')}
print(new_dict)
n1 =[[name + "s favorite movie was " + movie + " from " + str(yr)] for name,movie,yr in zip(names,movies,year) if yr < 1981 ]
print(n1)

# Randomness

import random
for i in range(5):
    print(random.random())


# example 2
import random
friends_list = ['John', 'Eric', 'Micheal', 'Terry', 'Graham']
print(random.sample(friends_list,5))
random.shuffle(friends_list)
print(friends_list)

# example 3
""" can be used for OTP """

import random,string

smallcaps = 'abcdefghijklmnopqrstuvwxyz'
largecaps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
letters_numbers = string.ascii_letters + string.digits
word = ''
for i in range(7):
    word = word + random.choice(letters_numbers)

print(word)  

# random string without duplicate example
# example 3
""" can be used for OTP """

import random,string

smallcaps = 'abcdefghijklmnopqrstuvwxyz'
largecaps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
letters_numbers = string.ascii_letters + string.digits
word = ''
for i in range(7):
    word = word + random.choice(letters_numbers)
word1 = ''.join(random.sample(letters_numbers,7))
print(word) 
print(word1)

# time it and performance
import timeit

print('Performance and Timeit module')
# Experiment with sieve of Eratosthenes
def test1():
    [x for x in range(1, 151) if not any([x % y == 0 for y in range(2, x)]) and not x == 1]
    return(1)
def test2():
    [x for x in range(2, 151) if not any([x % y == 0 for y in range(2, x)])]
def test3():
    # Initialize a list
    primes = []
    for possiblePrime in range(2, 151):
    # Assume number is prime until shown it is not.
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(possiblePrime)
    #print(primes)
    return(1)

print(timeit.timeit('test1()', globals=globals(), number=10))
print(timeit.timeit('test2()', globals=globals(), number=10))
print(timeit.timeit('test3()', globals=globals(), number=10))
"""output
Performance and Timeit module
3.819000005722046
3.441999912261963
0.17100000381469727
"""


# code to encrypt and decrypt a message
def enigma_light():
# create keys string
    keys = 'abcdefghijklmnopqrstuvwxyz !'
# autogenerate the values string by offsetting original string
    values = keys[-1] + keys[0:-1]
    #print(keys)
    #print(values)
# create two dictionaries
    dict_e = dict(zip(keys,values))
    dict_d = dict(zip(values,keys)) 
# OR create 1 and then flip 
    dict_e = dict(zip(keys,values))
    dict_d = {value:key for key, value in dict_e.items()}
#user input 'the message' and mode
    msg = input('Enter your secret message quietly: ')
    mode = input('Crypto mode: encode (e) OR decode (d): ')
# run encode or decode
    if mode == 'e':
        new_msg = ''.join([dict_e[letter] for letter in msg])
    elif mode == 'd':
        new_msg = ''.join([dict_d[letter] for letter in msg])
    
    return new_msg
# return result
# clean and beautify the code 

print(enigma_light())
