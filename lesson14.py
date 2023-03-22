a = 'A Aa AA'
b = 'B Bb BB'
c = 1.15123
string = 'a={name1} b={name2} c={name3:.2f}'
# .format is a function (method) of string
str_format = string.format(
    # Parameter = Argument
    # In this case: Name = variable
    name1=a,
    name2=b,
    name3=c
)

print(str_format)
