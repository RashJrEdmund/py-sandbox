"""
    By containers, I mean data structures that can contian multiple data, and even of different data types.
    They include "Lists, Tuples, Dictionaries, and Sets"

"""

# TUPLES AND LISTS

"""
    Think of turples and lists like arrays in JS except that tuples are immutable, and use paranthesis "()" instead
    instead of square braces to add their openning and closing boundraris. Also, you can not use the .append()
    method data to a tuple.
"""

myTuple = (1, 0, "some-val", ("another tuple", 1), [1,2])

myList = [1, 0, "some-val", ["another array"], (2,31)]

"""
    - We can Index tuples and lists with this array like syntax

        - myList[0] # to get the first item in the list


    - also, we can slice the list with the following syntax

        - myList[0:2] # [1, 0] ____just like Array.slice in JS where the last index (2 in this case) is not included.
        
    - Also, we can add a step size, to tell how many indecies to skip
        - myList[0:4:2] # [1, "some-val"]
"""

print("\n", myTuple, "\n", myList, "\n")
print(myList[0:2], "\n"); # just like Array.slice(0, 2);

print(myList[0:4:2]); # just like Array.slice(0, 4) but will skip 2 elements just like for (let i = 0; i < arr.length; i += 2) {...}.


# SETS
"""
    Sets follow the same comma seperated pattern as LISTS, and Tuples execpt it's like the JavaScript "Set" data
    structure. All values in a set are unique and any duplicates are removed
"""

mySet = {1,2,3, "test"}

print(mySet)

# DICTIONARIES
"""
    My favorite data structure so far. They are like JavaScript Maps and objects. with key value pairs,
    where the values could be any data type
"""

myDictionary = { "name": "Rash", "Age": 201 }

print(myDictionary)
