mas=[]
count=0
counts=[]
new=[]

with open('cities.txt','r') as file:
    lines=file.readlines()

    for i in lines:
        mas.append(i.strip('\n'))

while True:
    try:
        min=int(input('Введите минимальное кол-во жителей: '))
        break
    except:
        print('Количество может быть только натуральным числом')

for i in mas:
    i = i.split(':')
    if int(i[1])>int(min):
        new.append(i)
new=sorted(new)

with open('iltered_cities.txt','w') as file:
    for i in new:
        file.write(i[0]+':'+i[1]+"\n")