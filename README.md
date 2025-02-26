# GCP Python

# important notes on lambda, map, filter, reduce

Syntax:
lambda arguments : expression
map(function, iterable)  
 Best Use Case: When you want to apply a function to every element in a list.
filter(function, iterable)
Best Use Case: When you need to remove elements that don’t satisfy a condition.
reduce(function, iterable)  
 Best Use Case: When you need to aggregate elements into a single result (like sum, product, max, etc.).

<!--
                        #  Summary Table -->
<!-- # Function	  Purpose	                         Example
# lambda	 Anonymous function     	       lambda x: x * 2
# map()	    Apply a function to each item	   map(lambda x: x**2, [1,2,3])
# filter()	Filter items based on condition	   filter(lambda x: x > 2, [1,2,3])
# reduce()	Reduce items to a single value	   reduce(lambda x,y: x+y, [1,2,3]) -->

# important shortcut for dictionary to remember.........

keys = dict1.keys() # Get all keys /n
values = dict1.values() # Get all values
pairs = dict1.items() # Get all key-value pairs
