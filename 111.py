a=input()
b=set(a)
for i in b:
    print('{}_{}'.format(i,a.count(i)),end= '')
