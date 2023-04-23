"""
CPF: 123.456.789-00
Collect the sum of the first 9 digits of the CPF
by multiplying each value
by a countdown starting from 10.

EX: 123.456.789-00 -> (123456789)
    10   9   8   7   6   5   4   3   2
*    1   2   3   4   5   6   7   8   9
     10  18  24  28  30  30  28  24  18

Sum all the results:
10+18+24+28+30+30+28+24+18 = 210
Multiply the previous result by 10:
210 * 10 = 2100
Get the remainder of the previous operation divided by 11:
2100 % 11 = 0
If the previous result is greater than 9:
    result is 0
else:
    result is the value of the operation

The first digit of the CPF is 1.
"""
cpf = str(input('Type in your CPF: '))
cpf = cpf.replace('.', '')
cpf = cpf.replace('-', '')
cpf = list(map(int, cpf[0:9]))
"""
The code above can be replaced with the following code:
cpf = list(map(int, input('Type in your CPF: ').replace('.', '').replace('-', '')[:9]))
for simplification...
But for learning purposes, it stays as it is!
"""

cpf_first_sum = 0
cpf_first_div = 0

for i in range(9):
    # Multiply each value by 10 minus index in a countdown
    cpf_first_sum += cpf[i] * (10-i)

# Get the remainder of the previous operation divided by 11
cpf_first_div = 0 if ((cpf_first_sum * 10) %
                      11) > 9 else (cpf_first_sum * 10) % 11

# Appends the first digit of the CPF to the end of the list
cpf.append(cpf_first_div)

print(f'First Digit: {cpf_first_div}')

cpf_second_sum = 0
cpf_second_div = 0

for i in range(10):
    # Multiply each value by 11 minus index in a countdown
    cpf_second_sum += cpf[i] * (11-i)

# Get the remainder of the previous operation divided by 11
cpf_second_div = 0 if ((cpf_second_sum * 10) %
                       11) >= 10 else (cpf_second_sum * 10) % 11

print(f'Second Digit: {cpf_second_div}')

# Appends the second digit of the CPF to the end of the list
cpf.append(cpf_second_div)

formatted_cpf = '{0}{1}{2}.{3}{4}{5}.{6}{7}{8}-{9}{10}'.format(*cpf)
print(f'The CPF you provided is: {formatted_cpf}')

# BELLOW IS THE TEACHER'S SOLUTION

user_sent_cpf = '74682489070'
nine_digits = user_sent_cpf[:9]
regressive_counter_1 = 10

result_digit_1 = 0
for digit in nine_digits:
    result_digit_1 += int(digit) * regressive_counter_1
    regressive_counter_1 -= 1

digit_1 = (result_digit_1 * 10) % 11
digit_1 = digit_1 if digit_1 <= 9 else 0

ten_digits = nine_digits + str(digit_1)

regressive_counter_2 = 11

result_digit_2 = 0
for digit in ten_digits:
    result_digit_2 += int(digit) * regressive_counter_2
    regressive_counter_2 -= 1

digit_2 = (result_digit_2 * 10) % 11
digit_2 = digit_2 if digit_2 <= 9 else 0

calculated_cpf = f'{nine_digits}{digit_1}{digit_2}'

if user_sent_cpf == calculated_cpf:
    print(f'{user_sent_cpf} is valid')
else:
    print('Invalid CPF')
