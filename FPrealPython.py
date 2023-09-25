# def func():
#     print("I am function func()!")
#
#
# print("cat", func, 42)
#
#
# objects = ["cat", func, 42]
# print(objects[1])
# #call function func
# objects[1]()
# d = {"cat": 1, func: 2, 42: 3}
# d[func]



### This is known as function composition.
"""
Technical note: Python provides a shortcut notation called a decorator to facilitate
 wrapping one function inside another. For more information, check out the Primer on
 Python Decorators.
"""
"""
A good example of this is the Python function sorted(). Ordinarily, if you pass a 
list of string values to sorted(), then it sorts them in lexical order:
A good example of this is the Python function sorted(). Ordinarily, if you pass
 a list of string values to sorted(), then it sorts them in lexical order:
"""
# def inner():
#     print("I am function inner()!")
#
# def outer(function):
#     function()
#
# outer(inner)
# animals = ["ferret", "vole", "dog", "gecko"]
# print(sorted(animals, key=len, reverse=True))
#
# def reverse_len(s):
#     return -len(s)
#
# print(sorted(animals, key=reverse_len))

###########################################################################

###Defining an Anonymous Function With lambda
'''
Functional programming is all about calling functions and passing them around, so it
 naturally involves defining a lot of functions. You can always define a function in the
  usual way, using the def keyword as you have seen in previous tutorials in this series.

Sometimes, though, it’s convenient to be able to define an anonymous function on the fly,
 without having to give it a name. In Python, you can do this with a lambda expression.
'''

##returns the characters in s in reverse order.
#s[-1] -> return the last element in a list or last char in string
#s[::-1]-> return all element in list but start from index-1 mean reverse the list and str
#lambda s: s[::-1]

'''
The built-in Python function callable() returns True if the argument passed to it appears
 to be callable and False otherwise.
'''
# print(callable(lambda s: s[::-1]))
#
# def reverse(s):
#     return s[::-1]
#
# print(reverse("I am a string"))
#
#
# reverse = lambda s: s[::-1]
# print(reverse("I am a string"))
#
# #You can also call the function defined by a lambda expression directly:
# print((lambda s: s[::-1])("I am a string"))

def func(x):
    return x, x ** 2, x ** 3

print(func(3))
#This implicit tuple packing doesn’t work with an anonymous lambda function:
#as tuble is immutable

#print((lambda x: x, x ** 2, x ** 3)(3))

#u can solve it by return tuble from lamda or list or dictionary
# print((lambda x: (x, x ** 2, x ** 3))(3))
#
# print((lambda x: [x, x ** 2, x ** 3])(3))
#
# print((lambda x: {1: x, 2: x ** 2, 3: x ** 3})(3))

#####################################################

#print(f"--- {lambda s: s[::-1]} ---")#syntax error unexpected EOF while parsing

#the solution add {( lamda s: s[] )}]

# print(f"--- {(lambda s: s[::-1])} ---")
#
# print(f"--- {(lambda s: s[::-1])('I am a string')} ---")


#############################################################################

'''Python offers two built-in functions, map() and filter(), t
hat fit the functional programming paradigm. A third, reduce()
Each of these three functions takes another function as one of its arguments.'''

#map(<f>, <iterable>)
"""map(<f>, <iterable>) returns in iterator that yields the results of applying
 function <f>to each element of <iterable>.
"""
def reverse(s):
    return s[::-1]
animals = ["cat", "dog", "hedgehog", "gecko"]
iterator = map(reverse, animals)
print(iterator)

"""But remember, map() doesn’t return a list. It returns an iterator called 
a map object. To obtain the values from the iterator, you need to either 
iterate over it or use list():
"""
for i in iterator:
    print(i)

iterator = map(reverse, animals)

print(list(iterator))