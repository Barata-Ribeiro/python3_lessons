"""
This is only the proposed alternative solution.
It makes use of 're' and 'sys' libraries.
"""
import re
import sys

# cpf_sent_by_user = '746.824.890-70' \
#     .replace('.', '') \
#     .replace(' ', '') \
#     .replace('-', '')
input_entry = input('CPF [746.824.890-70]: ')
cpf_sent_by_user = re.sub(
    r'[^0-9]',
    '',
    input_entry
)

entry_is_sequential = input_entry == input_entry[0] * len(input_entry)

if entry_is_sequential:
    print('You have entered sequential data.')
    sys.exit()

nine_digits = cpf_sent_by_user[:9]
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

cpf_generated_by_calculation = f'{nine_digits}{digit_1}{digit_2}'

if cpf_sent_by_user == cpf_generated_by_calculation:
    print(f'{cpf_sent_by_user} is valid')
else:
    print('Invalid CPF')
