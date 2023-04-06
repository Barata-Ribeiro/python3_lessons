"""
Iterable -> str, range, etc. are containers which you can get an iterator from (__iter__)
Iterator -> 'contains a countable number of values', delivers one value at a time
next -> delivers the next value
iter -> delivers the iterator
"""

# for letter in text -> letter calls of iter(text)
# text = 'Whatever'.__iter__()
text = 'Whatever'
iterator = iter(text)  # iter() works as "__iter__()"
print(iterator)

# print(iterator.__next__())  # __next__() will print the next value

while True:
    try:
        letter = next(iterator)
        print(letter)  # Will print the next value
    # When the last value is returned and 'StopIteration' shows
    except StopIteration:
        # Breaks the loop
        break

# The above code can be simplified with the following:
# for letter in text:
#   print(letter)
# SO MUCH BETTER!
