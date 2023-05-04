"""
args - Unnamed arguments
* - *args (packing and unpacking)
"""
# Remember unpacking
x, y, *remainder = 1, 2, 3, 4, 534, 534, 534, 5, 345
print(x, y, remainder)


def add(x, y, *args):
    total = 0
    for arg in args:
        total += arg
    return x + y + total  # sum(args) also works...


print(add(234, 23, 423, 42, 34, 234, 23, 423, 4,
      234, 23, 423, 4, 234, 32, 4, 234))  # 2628

print(add(23, 45))  # 68

print("-----------------------")


def new_add(*args):
    total = 0
    for arg in args:
        total += arg
    return total


result1 = new_add(234, 23, 423, 2, 34, 234, 23, 423,
                  4, 235, 46, 54, 745, 765, 86, 978, 98, 0)
print(result1)  # 4407

numbers = [23, 4, 235, 4, 645, 76, 978, 0,
           780, 76, 949, 67, 321, 90, 7, 4679, 6, 79]
result2 = new_add(*numbers)
print(result2)  # 9019

new_numbers = 12, 312, 4, 235, 43, 645, 756, 865, 8909, 4, 39, 3, 93, 93
print(sum(new_numbers))  # 12013
# sum is a function from Python
