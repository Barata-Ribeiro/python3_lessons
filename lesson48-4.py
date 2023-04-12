"""
Being careful with changing data
= - copied the value (immutable)
= - points to the same value in memory (mutable)
"""
name = "John Doe"
saved_name = name  # Saves the 'name' in memory
name = "Jane Doe"

print(name)
print(saved_name)

list_a = ['Jason', 'Alexa']
# list_b = list_a  # This isn't copying the value, but pointing to the same value
list_b = list_a.copy()  # This copies the value and returns a new list
list_a[0] = 'Jack'

print(list_a)
print(list_b)
