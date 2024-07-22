end=[]
line=[]
info={}
subjects=[]

try:
    with open('input.txt','r') as file:
        lines=file.readlines()

        for i in lines:
            line.append(i)

        for i in line:
            ln=i.split(':')
            info[ln[0]]=ln[1].strip(' ')
except:
    print('Файл input.txt не найден')

for i in info.values():
    x=i.split(',')
    for i in x:
        i=i.strip()
        if i!='':
            subjects.append(i)
print(f'Список предметов: {set(subjects)}')

while True:
    lsn=str(input('Введите предмет: '))
    if lsn in set(subjects):
        break
    else:
        print('Нет предмета в списке')

for i in info.items():
    value=i[1].split(',')
    for j in value:
        if lsn==j.strip(' ').strip('\n'):
            end.append(i)
for i in end:
    print('\t'+i[0])

with open('output.txt','w') as file:
    file.write(lsn+':'+'\n')
    for i in end:
        file.write('\t'+i[0]+'\n')