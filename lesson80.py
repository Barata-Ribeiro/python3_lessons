"""
Exercise
Create a function that finds the first duplicate
considering the second occurrence as the duplication.
Return the considered duplication.
Requirements:
    The order of the duplicate number is considered from the second occurrence of the number, i.e., the duplicate number itself.
    Example:
        [1, 2, 3, ->3<-, 2, 1] -> 1, 2, and 3 are duplicates (return 3)
        [1, 2, 3, 4, 5, 6] -> Return -1 (no duplicates)
        [1, 4, 9, 8, ->9<-, 4, 8] (return 9)
    If no duplicates are found in the list, return -1
"""
list_of_integer_lists = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]


def find_first_duplicate(list_to_evaluate):
    # Stores the first duplicate of each sublist in a list.
    list_of_duplicates = []
    # For each sublist in the object...
    for sublist in list_to_evaluate:
        # Stores all the seen numbers in a set.
        seen_num = set()
        # Default value of False is set to found a duplicate.
        found_a_duplication = False
        # For each number in the sublist...
        for num in sublist:
            # If the number is already in the set...
            if num in seen_num:
                # Adds the first duplicate to the list.
                list_of_duplicates.append(num)
                # Tells the algorithm to stop looking for duplicates
                # in the current list...
                found_a_duplication = True
                break
            # Adds the number to the set.
            seen_num.add(num)
        # If no duplicates were found, return -1.
        if not found_a_duplication:
            # appends the '-1' to the list_of_duplicates list
            list_of_duplicates.append(-1)
    return list_of_duplicates


# print(find_first_duplicate(list_of_integer_lists))

# TEACHER'S SOLUTION
def find_the_first_duplicate(list_of_integers):
    # Create a set to store the numbers we've checked so far
    checked_nums = set()

    # Initialize the first duplicate as -1,
    # which will be the return value if no duplicate is found
    first_duplicate = -1

    # Loop through each number in the list
    for num in list_of_integers:
        # If the number is already in our set of checked numbers,
        # it's a duplicate, and we've found our first duplicate
        if num in checked_nums:
            # Set the first duplicate to this number
            first_duplicate = num
            # Stop checking for more duplicates -
            # we've found the first one
            break

        # Add the number to our set of checked numbers
        # because we've now checked it
        checked_nums.add(num)

    # Return the first duplicate number we found,
    # or -1 if no duplicate was found
    return first_duplicate


# Now we use our function on each list in the list_of_integer_lists
for lst in list_of_integer_lists:
    # For each list, print the list and the first duplicate number in that list
    print(f'{lst}: {find_the_first_duplicate(lst)}')
