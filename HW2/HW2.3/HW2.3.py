num1=[]
num2=[]
sum=[]
rez=[]
index=[]
end=[]
count=0
try:
    with open('input1.txt','r') as n1:
        lines1 = n1.readlines()
        for i in lines1:
            num1.append(i.strip('\n'))
except FileNotFoundError:
    print('Файл input.txt не находится в одной папке с данным кодом')
try:
    with open('input2.txt','r') as n2:
        lines2 = n2.readlines()
        for i in lines2:
            num2.append(i.strip('\n'))
except FileNotFoundError:
    print('Файл input.txt не находится в одной папке с данным кодом')
for i in num1:
    sum.append(i)
for i in num2:
    sum.append(i)
for i in sum:
    for j in sum:
        if i>=j:
            continue
        else:
            rez.append(i)
            count+=1
    index.append(count)
    count=0
indexes=int(len(index))-1
while indexes!=-1:
    for i in range(len(index)):
        if index[i] == indexes:
            end.append(sum[i])
    indexes-=1
try:
    with open('output.txt','w') as o:
        for i in end:
            print(i)
            o.write(i+'\n')
except FileNotFoundError:
    print('Файл output.txt не находится в одной папке с данным кодом')