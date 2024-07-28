def func(x):

    if x==0:
        return 1
    
    num=[0]*(x+1)
    num[0]=1

    for i in range(1,x+1):
        if x>=1:
            num[i]+=num[i-1]
        if x>=2:
            num[i]+=num[i-2]
        
    return num[x]

try:
    x=int(input('Введите количество ступенек: '))
except ValueError:
    print('Кол-во ступенек может быть только целым числом')

count = func(x)

print(count)