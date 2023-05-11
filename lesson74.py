"""
Closure and functions that return other functions
"""


def create_salutation(greeting):
    def salute(name):
        return f'{greeting}, {name}!'
    return salute


hello_function = create_salutation('Hello')
afternoon_function = create_salutation('Afternoon')

for name in ['Alice', 'Bob', 'Carol', 'Jason', 'Michael']:
    print(hello_function(name))
    print(afternoon_function(name))
    print()

"""
The inner function 'salute' remembers the values of 'greeting' and 'name' even after the 'create_salutation' function has finished executing.
"""
