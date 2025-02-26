
# LIST COMPREHENSION PRACTICE
# Create a list of squares for numbers from 1 to 15, but include only those squares that are less than 100.
# list=[i**2 for i in range(16) if i**2<100]
# print(list)
# Write a list comprehension to find all numbers between 1 and 50 that are divisible by both 3 and 5.
# list1=[i for i in range(51) if i % 3 ==0 and i % 5==0 ]
# print(list1)
# Given a list of strings ["apple", "banana", "cherry"], use a list comprehension to create a list of the reversed strings.
# strings = ["apple", "banana", "cherry"]
# str=[strings[::-1] for strings in strings]
# print(str)
# OR# print(strings[::-1])

# Create a dictionary where the keys are numbers from 1 to 5, and the values are their cubes.
# dic={i:i**3 for i in range(6)}
# print(dic)

# # From a list nums = [1, 2, 3, 4, 2, 3, 1], create a set of their squares.
# nums = [1, 2, 3, 4, 2, 3, 1]

# # set2=set(nums)
# # print(set2)
# set1=set(i**2 for i in nums)
# print(set1)



# # Given a list words = ["hello", "world", "python", "is", "awesome"], use a list comprehension to filter words with more than 5 characters.
# words = ["hello", "world", "python", "is", "awesome"]
# list1=[i for i in words if len(i)>5]
# print(list1)

# # Create a list of all pairs (x, y) such that:

# x ranges from 1 to 3.
# y ranges from 4 to 6.
# new=[(i,j) for i in range(1,4) for j in range(4,7)]
# print(new)


# DICTIONARY COMPREHENSION PRACTICE

# # Create a dictionary where the keys are numbers from 1 to 10, and the values are their squares.
# dict1={i:i**2 for i in range(1,11)}
# print(dict1)

# # Given the string "dictionary", create a dictionary where the keys are characters, and the values are their frequency in the string.

# str1="dictionary"
# dict2= {i:str1.count(i) for i in str1}
# print(dict2) NHI AAYA SOLVR KRNA ...NEED TO REVISE

# Given a list of words ["apple", "banana", "cherry"], create a dictionary where the keys are the words, and the values are their lengths.
# words=["apple", "banana", "cherry"]
# dict3 = {i:len(i) for i in words}
# print(dict3)
# -------------------------------------------------------------------------
# import requests

# url= "https://jsonplaceholder.typicode.com/posts/1"

# response= requests.get(url)
# if requests.status_codes==200:
#     data=response.json()
#     print(data)
# else:
#     print("data was not found")
#---------------------------------------------------------------------------
# l=[1,2,3]
# l1=['a','b','c','d']
# zipped=zip(l,l1)
# print(list(zipped))
# ...................DICTIONARY PRACTICE....................

# dict1={'name': 'Alice', 'age':25, 'grade':'A'}
# print(type(dict1))

# print(dict1['name'])
# print(dict1['age'])
# dict1['age']=27
# dict1['city']='Delhi'
# print(dict1)

# del dict1['city']
# print(dict1)

# for key in dict1:
#     print(key)

# for value in dict1.values():
#     print(value)

# for pairs in dict1.items():
#     print(pairs) #output will be in tuple form e.g. ('name', 'Alice')

# for key, value in dict1.items():
#     print(key,value) #output will be in key value form e.g. name Alice

    # important shortcut for dictionary to remember.........
# keys = dict1.keys()  # Get all keys
# values = dict1.values()  # Get all values
# pairs = dict1.items()  # Get all key-value pairs

# ...................SET PRACTICE....................
# set1={'apple', 'banana', 'cherry'}
# print(type(set1))

# **set charachterstics(very Important)**
# No duplicate values.
# Unordered (no indexing).

# add()	Adds an element to the set
# set1.add('orange')
# print(set1)

# set1.add('hii')
# print(set1)

# set1.remove('hii')
# print(set1)

# set1.discard('hii')   # Doesn't throw an error although hii is already remove
# print(set1)

# set1={1,2,3,4}
# set2={4,5,6,7}

# print(set1|set2)
# print(set1&set2) #intersection .... for commomn element
# print('set2&set1:',set2&set1)
# print(set1-set2) #Elements in set1 but not in set2.
# print("set2-set1:",set2-set1) #element is s2 bt not in s1
# print(set1^set2) #Symmetric Difference: Elements in either set but not both.
# print(set2^set1) #output will be same as above
 
#"the quick brown fox jumps over the lazy dog"...Find all unique words using a set. 
# text = "the quick brown fox jumps over the lazy dog"
# words=text.split()
# print(words)
# newset=set(words)
# print(newset)

#"apple banana apple cherry banana apple"........Count the frequency of each word in the sentence: 
text1 = "apple banana apple cherry banana apple"
words1=text1.split()
count1={i:words1.count(i) for i in words1}
print(count1)


#...............Tuple...............................
my_tuple = (1, 2,2,5,6,8, 3, 4)
print(my_tuple.count(2))  #count of 2 (2 kitni baar aaya hai)

print(my_tuple.index(3))  # The first occurrence of 3 is at the 6th index (remember Python uses zero-based indexing).

#Tuple Packing and Unpacking
coordinates = (10, 20, 30) #this is packing
x, y, z = coordinates
print(x)  # Output: 10 #unpacking
print(y)  # Output: 20 #unpacking
print(z)  # Output: 30 #unpacking

# Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
result = tuple1 + tuple2
print(result)  # Output: (1, 2, 3, 4, 5, 6)

# Multiplication
tuple3 = (10, 20)
result = tuple3 * 3
print(result)  # Output: (10, 20, 10, 20, 10, 20)
