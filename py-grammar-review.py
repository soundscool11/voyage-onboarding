# Operator
print(10 // 3) # quotient - 3
print(10 % 3) # remainder - 1
print(10 ** 2) # exponential - 100



# String
str1 = 'Hello'
str2 = "World!"
print(len(str1))
print(str1 + ' ' + str2)

# String Methods
sentence = 'Python is FUN!!'
email = 'siwon@naver.com'

print(sentence.upper())
print(sentence.lower())

print(email.split('@')[1].split('.')) # return list

print(sentence.replace('!', ':)'))



# Indexing and Slicing
f = 'abcdefghijkl'
print(f[1])

print(f[4:15]) # f[4] ~ f[14]
print(f[8:]) # f[8] ~ end
print(f[:7]) # front ~ f[6]
print(f[:]) # everything



# List
a = [3, "a", 6, True, [2, 3]] # order matters & data type convertible
print(len(a))
empty = []
empty = list()

print(a[1:3])
print(a[-1]) # last index value
print(a[4][0])

# List Methods
a = [1, 2, 3]
a.append(4)
a.append([5, 6])
a += [7, 8]
print(a)

b = [5, 2, 1]
b.sort() # ascending
print(b)
b.sort(reverse=True) # descending
print(b)

print(1 in b)
print("1" not in a)



# Dictionary
person = {"name": "Bob", "age": 21}
print(person["name"])

empty = {}
empty = dict()

# print(person[0]) # dict has no order => no indexing

# update dictionary 
person["name"] = "Robert"

# add (key, value)
person["height"] = 174.8
person["score"] = {"math": 81, "science": 90, "English": 100}
print(person["score"]["math"])

# check existance
print("name" in person)
print("email" not in person)


# List and dictionary
people = [{'name': 'Bob', 'age': 21}, {'name': 'Alice', 'age': 25}]

print(people[0]['name'])

person = {'name': 'Tom', 'age': 19} 
people.append(person)
print(people[2]['name'])



# for loop
people = [
{'name': 'bob', 'age': 20},
{'name': 'carry', 'age': 38},
{'name': 'john', 'age': 7},
{'name': 'smith', 'age': 17},
{'name': 'ben', 'age': 27},
{'name': 'bobby', 'age': 57},
{'name': 'red', 'age': 32},
{'name': 'queen', 'age': 25}
]

for person in people:
    if person['age'] > 20:
        print(person['name'])

fruits = ['orange', 'apple', 'banana', 'pear', 'watermelon']

for i, fruit in enumerate(fruits):
    print(i, fruit)
    if i == 4: # printing only first 5 values
        break 



# Function
def check_gender(pin):
    num = int(pin.split('-')[1][0])
    if num % 2 == 0:
        print('W')
    else:
        print('M')

my_pin = "001108-1202302"
check_gender(my_pin)



# Tuple - immutable, order matters
a = (1, 2, 3)
print(a[0])
# a[0] = 99 - not acceptable
a_dict = [('Bob', 21), ('Alice', 25), ('Tom', 19)]
print(a_dict)



# Set - no duplicates
a = [1,2,3,4,5,3,4,2,1,2,4,2,3,1,4,1,5,1]
a_set = set(a)
print(a_set)

a = set(['apple', 'banana', 'strawberry'])
b = set(['apple', 'melon'])
print(a & b) # intersection
print(a | b) # union
print(a - b) # except



# f-string
names = ['Tom', 'David', 'Alice']
for name in names:
    print(f'My name is {name}.')



# Error handling: try-except statement
people = [
    {'name': 'bob', 'age': 20},
    {'name': 'carry', 'age': 38},
    {'name': 'john', 'age': 7},
    {'name': 'smith', 'age': 17},
    {'name': 'ben', 'age': 27},
    {'name': 'bobby'},
    {'name': 'red', 'age': 32},
    {'name': 'queen', 'age': 25}
]

for person in people:
    try:
        if person['age'] > 18:
            print(person['name'])
        else:
            print(f'{name} - minor')
    except:
        name = person['name']
        print(f'{name} - error')



# File import
# On main_func.py
def say_hi():
    print('Hi!')

# On main.py
# from main_func import *
say_hi()



# Ternary operators
num = 3

if num % 2 == 0:
    result = 'even'
else:
    result = 'odd'
print(f'{num} is {result}')

result = 'even' if num % 2 == 0 else 'odd' # ternary
print(f'{num} is {result}')

#-----------------------------------------

a_list = [1, 3, 2, 5, 1, 2]
b_list = []

for a in a_list:
    b_list.append(a * 2)

print(b_list)

b_list = [a * 2 for a in a_list]
print(b_list)



# map, filter, lambda
people = [
{'name': 'bob', 'age': 20},
{'name': 'carry', 'age': 38},
{'name': 'john', 'age': 7},
{'name': 'smith', 'age': 17},
{'name': 'ben', 'age': 27},
{'name': 'bobby', 'age': 57},
{'name': 'red', 'age': 32},
{'name': 'queen', 'age': 25}
]

# map - manipulate the elements in list
# 1
def check_adult1(person):
    if person['age'] > 18:
        return 'adult'
    else:
        return 'minor'
    
result1 = map(check_adult1, people)
print(list(result1)) # ['adult', 'adult', 'minor', 'minor', 'adult', 'adult', 'adult', 'adult']

# 2
def check_adult2(person):
    return 'adult' if person['age'] > 18 else 'minor'

result2 = map(check_adult2, people)
print(list(result2))

# 3 - lambda
result3 = map(lambda x: ('adult' if x['age'] > 20 else 'minor'), people)
print(list(result3))

# filter
result = filter(lambda x: x['age'] > 18, people)
print(list(result)) 



# Funtion arguments
def cal(a, b):
    return a + 2 * b

print(cal(3, 5)) # 13
print(cal(5, 3)) # 11
print(cal(a=3, b=5)) # 13
print(cal(b=5, a=3)) # 13

def cal2(a, b=3): # setting default value
    return a + 2 * b

print(cal2(4))
print(cal2(4, 2))
print(cal2(a=6))
print(cal2(a=1, b=7))

def call_names(*args): # no limit in the number of arguments
    for name in args:
        print(f'{name} is called')
call_names('Tom', 'David', 'Alice')

def get_kwargs(**kwargs): # no limit in the number of keyword arguments
    print(kwargs)

get_kwargs(name='bob')
get_kwargs(name='john', age='27')



# Class
class Monster():
    hp = 100
    alive = True

    def damage(self, attack):
        self.hp = self.hp - attack
        if self.hp < 0:
            self.alive = False

    def status_check(self):
        if self.alive:
            print('Alive!')
        else:
            print('Dead...')

m1 = Monster()
m1.damage(120)

m2 = Monster()
m2.damage(90)

m1.status_check()
m2.status_check()