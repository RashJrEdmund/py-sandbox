"""
    We use "==" to compare the equality of 2 entities
"""

print(5 >= 5)


# IF STATEMENT
"""
   if condition 1:
        block of code # make sure you indent.
   elif condition 2:
        another block of code
   else :
        default block
"""

userInput = abs(int(input("Enter a number ")))

if (userInput > 5):
    print("\nInput greater than 5\n")
elif (userInput < 5):
    print("\nInput less than 5\n")
else:
    print("\ninput is equal to 5\n")



# WHILE LOOP
"""
    while condition:
        block of code # well indented
"""

counter = 0

while (counter <= userInput):
    print(counter)
    counter += 1

print("while loop done")
    

# FOR LOOP
"""
    Can iterate over Tuples, Lists, and Dictionaries.

    for holder in dataStructure:
        block of code
"""
# LISTS, Tuples, and Sets
testList = [1, 2, 3, 4, 5]

for val in testList: # would work same for tuples
    print(val)

# Dictionaries
testDictionary = {
    "key 1": "val 1",
    "key 2": "val 2",
    "key 3": "val 3"
}

# 1
for key in testDictionary: # defaults to testDictionary.keys()
    print(key)

# 2
print("\nprinting values only\n")

for val in testDictionary.values():
    print(val)

# 3
print("\nprinting both key and value\n")

for items in testDictionary.items():
    print("items", items) # prints in the form ('key 1', 'val 1')

print(testDictionary.items()) # dict_items([('key 1', 'val 1'), ('key 2', 'val 2'), ('key 3', 'val 3')])

# 4
print("\ndestructuring items both key and value\n")

for key, val in testDictionary.items():
    print("key:", key, "| and |", "value:", val)


