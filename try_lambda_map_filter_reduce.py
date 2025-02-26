# important notes on lambda, map, filter, reduce 
# Syntax:
#  lambda arguments : expression
#  map(function, iterable)   
#  Best Use Case: When you want to apply a function to every element in a list.
#  filter(function, iterable) 
#  Best Use Case: When you need to remove elements that don’t satisfy a condition.
#  reduce(function, iterable)  
#  Best Use Case: When you need to aggregate elements into a single result (like sum, product, max, etc.).

                        #  Summary Table
# Function	  Purpose	                         Example
# lambda	 Anonymous function     	       lambda x: x * 2
# map()	    Apply a function to each item	   map(lambda x: x**2, [1,2,3])
# filter()	Filter items based on condition	   filter(lambda x: x > 2, [1,2,3])
# reduce()	Reduce items to a single value	   reduce(lambda x,y: x+y, [1,2,3])


# Write a lambda function to check if a number is even.
# number= [1,2,3,4,5,6,7,8,9,10]
evennumber=lambda i:i%2==0
print(evennumber(3))

# Write a lambda function to calculate the square of a number.
sq_no=lambda i:i *i
print(sq_no(7))

# Write a lambda function to find the maximum of two numbers.
max_of_two=lambda i,j: max(i,j)
print(max_of_two(2,4))

# Write a lambda function to convert a temperature from Celsius to Fahrenheit
# Formula: (Celsius * 9/5) + 32

temp=lambda Celsius:(Celsius * 9/5) + 32
print(temp(37))


# Given a list of numbers [1, 2, 3, 4, 5], use map() to create a new list with each number doubled.
# # numbers= [1, 2, 3, 4, 5]
# new=list(map(lambda i:i*2 ,numbers))
# print(new)

# Given a list of words ["apple", "banana", "cherry"], use map() to convert each word to uppercase.
words= ["apple", "banana", "cherry"]
uppercases=list(map(lambda i:i.upper(),words)) #UPPER FUNCTION YAAD RAKHNA HAI
print(uppercases)

# Given a list of numbers [10, 20, 30, 40], use map() to divide each number by 2.
numbers=[10, 20, 30, 40]
num=list(map(lambda i:i/2,numbers))
print(num)

# Given a list [1, 5, 8, 10, 12, 15], use filter() to keep only the even numbers.
list1=[1, 5, 8, 10, 12, 15]
new_list=list(filter(lambda i: i%2==0, list1))
print(new_list)

# Given a list of words ["hello", "world", "python", "is", "fun"], use filter() to keep only the words that are longer than 3 letters.
list_of_words = ["hello", "world", "python", "is", "fun"]


words=list(filter(lambda i:len(i)>3,list_of_words)) #LENGTH FUNCTION YAAD RAKHNA HAI
print(words)

# Given a list of numbers [3, 9, 12, 18, 21, 25], use filter() to keep only the numbers divisible by 3.
list_of_numbers= [3, 9, 12, 18, 21, 25]
no=list(filter(lambda i:i%3==0, list_of_numbers))
print(no)

# Given a list [1, 2, 3, 4, 5], use reduce() to find the sum of all elements.
from functools import reduce
list2= [1, 2, 3, 4, 5]
sum_of_elements= reduce(lambda i,j:i+j,list2)
print(sum_of_elements)

# Given a list [2, 3, 4, 5], use reduce() to calculate the product of all elements.
list3= [2, 3, 4, 5]
product=reduce(lambda i,j:i*j,list3)
print(product)

# Given a list [10, 5, 20, 30], use reduce() to find the maximum number.
list4= [10, 5, 20, 30]
max_num=reduce(lambda i,j:  i if i>j else j ,list4) #BIT COMPLICATED IF CONDITION USE KRNA HAI MAX FIND KRNE KE LIYE
print(max_num)

# Given a list [100, 50, 20, 10], use reduce() to subtract all numbers from left to right.
LIST5=[100, 50, 20, 10]
subs=reduce(lambda i,j:i-j,LIST5)
print(subs)


# Given a list of numbers [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
# Use filter() to keep only even numbers.
# Use map() to square each filtered number.
# Use reduce() to find the sum of the squared numbers.

numbs= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even=list(filter(lambda i:i%2==0,numbs))
print(even)
sq=list(map(lambda i:i**2,even))
print(sq)
sums=reduce(lambda i,j:i+j, sq)
print(sums)

print(even,sq,sums)