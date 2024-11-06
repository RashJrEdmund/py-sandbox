"""
    The pythagoras theorem for triangles, state; h^2 = a^2 + b^2;
"""

# so to calculate the hypotenuse of a trianglew, we do h = (a^2 + b^2)^(1/2)

print("Welcome to the pythagoras session, Please provide the following information")
print("So I can calculate the length of the hypotenuse of your triangle\n")

print("Given a triangle OAH, where H is the hypotenuse, and OA the other 2 sides, provide, the values of O and A so I can calculate H\n")

O = int(input("Enter the opposite side "))
A = int(input("Enter the Adjacent side \n"))

"""
    In python, to raise a vale to a power, we use either the "pow(val, power)" function, or the "**" operator (double asterisk)
"""
H = pow((O**2 + A**2), 1/2) # or (O**2 + A**2)**(1/2)


print("The triangle's hypotenuse is", H)
