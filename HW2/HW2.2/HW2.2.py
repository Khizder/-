num=[]
values=[]
modvalue=[]
values1=[]
end=[]
try:
    with open('input.txt','r') as n:
        lines = n.readlines()
        for i in lines:
            num.append(i.strip('\n'))
except FileNotFoundError:
    print('Файл input.txt не находится в одной папке с данным кодом')
print(num)
value=input('Enter your items you want to remove: ') 
'''     for i in value:
            values.append(i)
        print(values)
        for i in value:
            for j in values1:
                if i != j:
                    continue
                else:
                    i=i.strip(i)
            values1.append(i)
        for i in values1:
            if i!='':
                values2.append(i)
        print(values2)
        times=int(len(values2))'''
for i in num:
    modline=i.rstrip(value)+';'
    values.append(modline)
print(values)
for i in values:
    values1.append(i[::-1])
print(values1)
try:
    with open('output.txt','w') as o:
        for i in values1:
            print(i)
            o.write(i+'\n')
except FileNotFoundError:
    print('Файл output.txt не находится в одной папке с данным кодом')