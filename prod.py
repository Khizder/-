mas=[]
prod=[]
key=[]
count=0
sells={
}
try:
    with open('input.txt','r') as file:
        lines=file.readlines()
        
        for i in lines:
            i=i.strip('\n').strip('\t\t').strip('{').strip('}').strip(',').strip(' :').strip('"store')
            if i !='':
                mas.append(i)

        for i in mas:
            try:
                i=int(i)
            except:
                prod.append(str(i))
        print(prod)

        for i in prod:
            ln=i.split(':')
            key.append(ln[0])
        ln=0

        for i in set(key):
            for j in prod:
                ln=j.split(':')
                if i == ln[0]:
                    count+=int(ln[1].strip(' '))
            sells[i]=count  
            count=0
except:
    print('Не получается найти файл input.txt')

with open('output.txt','w') as file:
    for i in sells.items():
        file.write(i[0].rstrip('"')+':'+str(i[1])+'\n')