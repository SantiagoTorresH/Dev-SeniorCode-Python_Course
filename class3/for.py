terminos = 5

a, b = 0, 1
for i in range(terminos):
    print(a)
    tempA = a
    a = b
    b = tempA + b