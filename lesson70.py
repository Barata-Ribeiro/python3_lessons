"""
Returning values from functions (return)
"""
print()  # returns None


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def square(a):
    return a * a


def cube(a):
    return a * a * a


print(add(1, 2))  # 3
print(subtract(4, 2))  # 2
print(multiply(3, 2))  # 6
print(divide(6, 2))  # 3.0
print(square(4))  # 16
print(cube(5))  # 125


def another_add(x, y):
    if x > 10:
        # If 'x' is greater than 10, return sum of the list and ignore x, y
        return sum([10, 20])
    return int(x + y)


result1 = another_add(5, 12)
result2 = another_add(20, 8)
total = result1 + result2

print(total)  # 31 or 47
