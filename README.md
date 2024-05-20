mean=[]
treangle=[]
probel=[]
while True:
    try:
        N = int(input('Введите высоту триугольника (целое число): '))
        break
    except ValueError:
        print('Введено неправильное значение')
x=N-1
mean.append('*'*(N*2-1))
side=len(mean[0])
space=side-(N*2-1)
while space!=N:
    In=' '*space+(N*2-1)*'*'
    Ins=(N-1)*' '
    N=N-1
    treangle.append(In)
    probel.append(Ins)
treangle=treangle[::-1]
while x!=-1:
    treangle[x]=probel[x]+treangle[x]
    x=x-1
for i in treangle:
    print(i)
