"""
split and join with list and str
split - splits a string(list)
join - joins a string
"""
new_phrase = '     This is a interesting phrase.        Deal with it.           '
new_phrase_list = new_phrase.split('. ')

fixed_phrase_list = []
for i, phrase in enumerate(new_phrase_list):
    fixed_phrase_list.append(new_phrase_list[i].strip())

print(new_phrase_list)  # You still have the original list
print(fixed_phrase_list)  # This list is the same as an array in JavaScript

# Let's see join!

final_phrase = '. '.join(fixed_phrase_list)
print(final_phrase)
