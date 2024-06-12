"""
    Create a list or tuple with values from 1 to 10 and make it print
    [8, 6, 4, 2]
"""

myTuple = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sliced = myTuple[1:-1:2]

print(sliced[::-1]) # giving a negative step value will reverse the data

# OR SIMPLY

print(myTuple[7::-2]) # removing the value completely is like saying the lowest index
