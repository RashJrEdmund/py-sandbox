"""
    we declare functions using the "def" key word"

    def func_name(parameters):
        code
        return;
"""
def print_n_times(n = 3): # also defines default values just like in JS
    for i in range(abs(n + 1)):
            print(i)

# print_n_times()

def hypotenuse_calculator():
    side_a = int(input("Enter Adjacent Side "))
    side_o = int(input("Enter Opposite Side "))


    hypotenuse = pow(side_a**2 + side_o**2, 1/2)
    return round(hypotenuse, 2)


# print(hypotenuse_calculator())

# EXERCISE

"""
    Create a "shouter" function that takes 2 arguments: a string and a number.
    The function should print the string as many times as the number parameter.
    Capitalize every letter that is printed.

    If the number is greater  than 9, don't print the input string, instead, print "you are too loud"
    once.

    The function should also return the string "done" and have default values.
"""

# SOLUTION
def shouter(word = "word", num_repeats = 2):
    if (abs(num_repeats) >= 9):
        print("you are too loud")
    else:
        for i in range(int(num_repeats)):
            print(word);

    return "done"

word = input("Enter word to print ")
num = int(input("Enter number of times to print word "))

res = shouter(word, num)

print(res)


# LAMBDA FUNCTIONS
"""
    Functions so simple that don't really merrit an entire function definition.
    Here where we keep the entire logic on single line.
    They are also assigned to variable names just like in Js, except we make use of the lambda keyword
"""

# normal simple function that doesn't need so much writing
def normal_doubler(num):
    return num * 2

# lambda version of the doubler function

lambda_doubler = lambda num: num * 2 # receiving one paramter.
"""
    to recieve multiple parameters, we do

    test_func = lambda num1, num2: num1 * num2 
"""

print("lambda func", lambda_doubler(2))

"""
    they can be used commoning in other functions like the sorted() function
"""
# Example
"""
    sort the following list of tuples, where the second value in the tuple is the age of
    of the person given as the firts value in that tuple
"""
random_num_list = [2, 40, 1, 3, 5, 4, 9, 6]

print(sorted(random_num_list)) # sorts the numbers in ascending order. [1, 2, 3, 4, 5, 6, 9, 40]

#  but now
random_tuple_list = [("Kelmith", 21), ("Ekep", 20), ("Rash", 19)]

sorted_tuple_list = sorted(random_tuple_list, key = lambda user_tuple: user_tuple[1]) #

print(sorted_tuple_list)

"""
    Create a list comprehension for a battleship board. A list that starts from A1, and ends at E5
    i.e [A1, A2,..., B1, B2, ..., E5], making use of letters from A - E and numbers from 1 - 5.

    To make it hard exclude C3 from you list.
"""

battleship_board = [f"{letter}{num}" for letter in ("A", "B", "C", "D", "E") for num in range(1, 6) if f"{letter}{num}" != "C3"]

print(battleship_board)
