answer=[]
End=[]
x=''
while True:
    try:
        N = int(input('Введите число от 1 до 999: '))
        if N<1 or N>999:
            print("Вы ввели число не целое число из промежутка")
        else:
            break
    except ValueError:
            print("Вы ввели число не целое число из промежутка")
N=str(N)
while len(N)<3:
    N='0'+N
answer.append(int(N[0]))
answer.append(int(N[1]))
answer.append(int(N[2]))
if N[0]==0:
    answer[0]=''
elif answer[0]==1:
    answer[0]='Сто '
elif answer[0]==2:
    answer[0]='Двести '
elif answer[0]==3:
    answer[0]='Триста '
elif answer[0]==4:
    answer[0]='Четыреста '
elif answer[0]==5:
    answer[0]='Пятьсот '
elif answer[0]==6:
    answer[0]='Шестьсот '
elif answer[0]==7:
    answer[0]='Сесьмот '
elif answer[0]==8:
    answer[0]='Восемьсот '
elif answer[0]==9:
    answer[0]='Девятьсот '
if N[1]==0:
    pass
elif answer[1]==1 and answer[2]==0:
    answer[1]='десять'
    answer[2]=''
elif answer[1]==1 and answer[2]==1:
    answer[2]=''
    answer[1]='одинадцать'
elif answer[1]==1 and answer[2]==2:
    answer[2]=''
    answer[1]='двенадцать'
elif answer[1]==1 and answer[2]==3:
    answer[2]=''
    answer[1]='тринадцать'
elif answer[1]==1 and answer[2]==4:
    answer[2]=''
    answer[1]='четырнадцать'
elif answer[1]==1 and answer[2]==5:
    answer[2]=''
    answer[1]='пятнадцать'
elif answer[1]==1 and answer[2]==6:
    answer[2]=''
    answer[1]='шестнадцать'
elif answer[1]==1 and answer[2]==7:
    answer[2]=''
    answer[1]='семнадцать'
elif answer[1]==1 and answer[2]==8:
    answer[2]=''
    answer[1]='восемнадцать'
elif answer[1]==1 and answer[2]==9:
    answer[2]=''
    answer[1]='девятнадцать'
elif answer[1]==2:
    answer[1]='двадцать '
elif answer[1]==3:
    answer[1]='тридцать '
elif answer[1]==4:
    answer[1]='сорок '
elif answer[1]==5:
    answer[1]='пятьдесят '
elif answer[1]==6:
    answer[1]='шестьдесят '
elif answer[1]==7:
    answer[1]='семдесят '
elif answer[1]==8:
    answer[1]='восемдесят '
elif answer[1]==9:
    answer[1]='девяносто '
if N[2]==0:
    pass
elif answer[1]!='одинадцать' and answer[2]==1:
    answer[2]='один'
elif answer[1]!='двенадцать' and answer[2]==2:
    answer[2]='два'
elif answer[1]!='тринадцать' and answer[2]==3:
    answer[2]='три'
elif answer[1]!='четырнадцать' and answer[2]==4:
    answer[2]='четыре'
elif answer[1]!='пятнадцать' and answer[2]==5:
    answer[2]='пять'
elif answer[1]!='шестнадцать' and answer[2]==6:
    answer[2]='шесть'
elif answer[1]!='семнадцать' and answer[2]==7:
    answer[2]='семь'
elif answer[1]!='восемнадцать' and answer[2]==8:
    answer[2]='восемь'
elif answer[1]!='девятнадцать' and answer[2]==9:
    answer[2]='девять'
if answer[0] !=0:
    End.append(answer[0])
if answer[1] !=0:
    End.append(answer[1])
if answer[2] !=0:
    End.append(answer[2])
for i in End:
    x+=(str(i))
print(x)