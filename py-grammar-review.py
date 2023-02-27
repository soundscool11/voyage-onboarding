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

# print(person[0]) - dict has no order => no indexing
