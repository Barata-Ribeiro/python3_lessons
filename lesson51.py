"""
Introduction to packing and unpacking
"""
# The convention says that the underscore '_' will be used
# as a variable to pack values but that will not be use it.
_, name, *_ = ['John', 'Jason', 'Mary']
print(name)
