count=[]
sum=0
sum1=0
while True:
    try:
        N = int(input('Введите натуральное число от 0: '))
        if N<0:
            print("Введенные данные не соответствуют условию")
        else:
            break
    except ValueError:
            print("Введенные данные не соответствуют условию")
N=str(N)
while len(count)!=len(N):
    for i in N:
        count.append(int(i))
print(count)
for i in count:
    sum+=i
    i=0
sum=str(sum)
count=[]
while len(sum)>=2 and sum!=0:
    while len(count)!=len(sum):
        for i in sum:
            count.append(int(i))
    print(count)
    sum=int(sum)
    sum=0
    for i in count:
        sum+=i
        i=0
    sum=str(sum)
    count=[]
print(sum)