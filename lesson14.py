a = 'A Aa AA'
b = 'B Bb BB'
c = 1.15123
string = 'a={nome1} b={nome2} c={nome3:.2f}'
# .format is a function (method) of string
str_format = string.format(
    # Parameter = Argument
    # In this case: Name = variable
    nome1=a,
    nome2=b,
    nome3=c
)

print(str_format)
