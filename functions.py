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
