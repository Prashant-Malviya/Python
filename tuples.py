# tuple is an *immutable* data type in python

a = () #empty tuple

a = (1,) # tupel with only one element needs a comma

a = (1,3,4,5) #tupe more than one element

# Defining a tuple
my_tuple = (1, "Hello", 3.14, [1, 2, 3])
print(my_tuple)  # Output: (1, 'Hello', 3.14, [1, 2, 3])


from_list = tuple([1, 2, 3])  # Converts a list to a tuple

# Accessing elements
my_tuple = (10, 20, 30, 40)

print(my_tuple[1])   # Output: 20
print(my_tuple[-1])  # Output: 40

# Slicing
print(my_tuple[1:3])  # Output: (20, 30)


t = (1, 2, 3, 1, 1)
print(t.count(1))  # Output: 3

t = (1, 2, 3, 1, 1)
print(t.index(2))  # Output: 1

# concatenation : 

t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)  # Output: (1, 2, 3, 4)

#Repetition :
t = (1, 2)
print(t * 3)  # Output: (1, 2, 1, 2, 1, 2)

# membership testing
t = (1, 2, 3)
print(2 in t)  # Output: True

# length

t = (1, 2, 3)
print(len(t))  # Output: 3


# unpacking

t = (1, 2, 3)
a, b, c = t
print(a, b, c)  # Output: 1 2 3

'''
Why Use Tuples?
Data Integrity: Since tuples are immutable, their content is protected from accidental modification.
Performance: Tuples are faster than lists in terms of memory usage and access time.
Key in Dictionaries: Tuples can be used as keys in dictionaries, unlike lists.

When to Use Tuples
Use tuples for fixed collections of items (e.g., coordinates, configurations).
Use lists when the collection's size or content might change.
'''