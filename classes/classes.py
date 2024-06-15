# a basic class

class TestClass:
    test_var = "hello"
    another_var = "Some other thing"

# creating an instance of the classe
test = TestClass()
test.another_var = "new var"
print(test.another_var)

test2 = TestClass()

print(test2.another_var)


####
class NewClass():
    my_tuple = (1, 2, 3)

    """
        when defining a function in a class, the first argument that is always passed to the function
        is the instance of the class. By convention, this parameter is called "self", just like "this" in JS
    """
    def test_func(self):
        return "this self is like this in js"

    def another_func(self, test_param):
        print(test_param)

subDictionary = NewClass()

print(subDictionary.test_func())

subDictionary.another_func("test-param")

