# F STRINGS
"""
    f-strings allow us to write logic in between strings. just like back-ticks (``) in js allow us to insert
    logic within a string. When writing f-strings, the "f" is required else the parsing won't work
"""

user_name = input("Enter name ")
user_age = int(input("Enter age "))
user_info = f"{ user_name } is { user_age } years old"

print(user_info)


# SINGLE LINE IF STATEMENTS
"""
    Kinda like tenary operations but more if-like. The also work well with f-strings
"""

# value1 if condition else value2.

print("I knew it" if user_name.lower() == "rash" else "I didn't guess right")
# is similar to console.log(user_name.toLowerCase() === "rash" ? "I knew it" : "I din't guess right")

# making it complex by chaining operations
print(user_name, "You are", "a child" if user_age <= 12 else "a teenage" if user_age <= 19 else "an adult")


# LIST COMPREHENSION
"""
    you could add valuse to an array by doing

    simple_list = []
    for i in range(10):
        simple_list.append(i)

    but theres  better way, with list comprehenshion
"""

simple_list = [i for i in range(10)]

# We could even write 2 for loops
simple_list2 = [f"{i} {j}" for i in range(10) for j in ("a", "b", "c")] # double for loop

simple_list3 = [f"{i}{j}" for i in range(10) for j in ("a", "b", "c") if j == "a"] # only run when j == "a"

print(simple_list)
print("\n", simple_list2)

print("\n \n", simple_list3)
