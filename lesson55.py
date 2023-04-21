"""
Floating point inaccuracy
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""
import decimal

number_1 = decimal.Decimal('0.1')
number_2 = decimal.Decimal('0.7')
number_3 = number_1 + number_2
print(number_3)  # 0.799999... or 0.8 when using decimal.Decimal
print(f'{number_3:.2f}')  # 0.80 type str
print(round(number_3, 2))  # 0.8 type float
