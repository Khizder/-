def func(x,y):
    if y == 0:
        return x
    else:
        return func(y,x%y)

x = int(input('Введите делимое число: '))
y = int(input('Введите число, на которое делим: '))

res=func(y,(x%y))
print(res)