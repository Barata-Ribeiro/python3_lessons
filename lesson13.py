name = 'Barata Ribeiro'
height = 1.84
weight = 88
bmi = weight / (height * height)  # (height ** 2) also works

line_1 = f'{name} is {height:.2f} meters in height'
line_2 = f'weights {weight} kilograms, and his BMI is: {bmi:.2f}'

# Barata Ribeiro is 1.84 meters in height
print(line_1)
# weights 88 kilograms and his BMI is...
# BMI 25.99
print(line_2)
