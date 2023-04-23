# LESSON CODE HERE 1
import re
import random

for _ in range(10):
    nine_digits = ''
    for i in range(9):
        nine_digits += str(random.randint(0, 9))
# END LESSON CODE 1

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

    # LESSON CODE HERE 2
    eleven_digits = ten_digits + str(digit_2)

    cpf_generated_by_calculation = re.sub(
        r'(\d{3})(\d{3})(\d{3})(\d{2})', r'\1.\2.\3-\4', eleven_digits)

    print(cpf_generated_by_calculation)
    # END LESSON CODE 2
