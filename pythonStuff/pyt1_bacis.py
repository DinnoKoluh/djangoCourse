import numpy as np

str1 = "asbsjdjgr"
print(str1[1:])
print(str1[:3])
print(str1[2:5])
print(str1[:])
print(str1[::2])
str1.upper()
str1.capitalize()

str2 = "aaa {}".format("bbbb")
print(str2)

str3 = "aaa {y} bbb {x}".format(x = "ccc", y = "ddd")
print(str3)

# Lists are Pythons version of JS arrays
mylist = [1, 'a', 3]
len(mylist) # length of a list
mylist.append(2)
mylist.extend([1, 3, 4])
item = mylist.pop(-1)
print(mylist)
mylist.reverse()
# mylist.sort()

mat = [[1, 2], [3, 4]]

# List comprehension
first_col = [row[0] for row in mat]

print(first_col)

new_mat = np.array([[1, 2], [3, 4]])
new_col = new_mat[:, 0]
print(new_col)

# Dictionaries
# Python's version of Hash Tables, or JS objects (I guess sctructures in C++)
# Key value pair system
my_dict = {
    "key1": 1,
    "key2": "2"
}
my_dict["key3"] = "newKey"
print(my_dict)
print(my_dict["key1"])

# Tuples - basically immutable lists (meaning you cannot change the content by indexing)
t1 = (1,3,4)
# t1[1] = 2 you cannot do thist
print(t1)

# Sets - same shit as in C++
s1 = set([1,3,4,5,5])
s1.add(2)
print(s1)

for item in mylist:
    print(item)

t2 = [(1,3),(3,2)]
# tuple unpacking
for tup1, tup2 in t2:
    print(tup1)
    print(tup2)


l1 = list(range(0,12,2))
print(l1)

l2 = [num**2 for num in l1] 

print(l2)

for item in range(0,10,1):
    print("This is the " + str(item))

def new_fun (a, b):
    """
    A function that does nothing
    """
    if type(a) == type(b) == type(1):
        return a + b

new_fun(1,2)

# python generators
# lambda functions
l3 = [1,2,3,4,5,6]

evens = list(filter(lambda num: num % 2 == 0, l3))
print(evens)
print(1 in evens)

print("1, 2, 3" in str(l3))
print("a"*2)

if 2 in [1,2]:
    print("aaaaa")







