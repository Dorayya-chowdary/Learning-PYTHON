num=int(input('Enter the table:'))
s=int(input('enter the start range of steps:' ))
e=int(input('enter the end range of steps:'))
multiple_s=int(input('enter the multiple range start:'))
multiple_e=int(input('enter the multiple range end:'))
for i in range(s,e+1,1)
    if num*i>=multiple_s and num*i<=multiple_e:
        print(num,'X',i,'=',num*i)

