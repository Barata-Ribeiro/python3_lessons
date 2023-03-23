"""
Comparison Operators (Relational)
OP      Meaning                         Example (True)
>       greater than                    2 > 1
>=      greater than or equal to        2 >= 2
<       less than                       1 < 2
<=      less than or equal to           2 <= 2
==      equals                          'a' == 'a'
!=      different than                  'a' != 'b'
"""

greather_than = 2 > 2
greather_than_or_equal_to = 2 >= 2
less_than = 1 < 2
less_than_or_equal_to = 2 <= 2
equals = 'a' == 'c'
different = 'a' != 'b'

print(greather_than)  # False
print(greather_than_or_equal_to)  # True
print(less_than)  # True
print(less_than_or_equal_to)  # True
print(equals)  # False
print(different)  # True, we want to know if it is different
