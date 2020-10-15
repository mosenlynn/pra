a=input()
a=a.split()
dic={}
r=[]
n=0
for i in a:
    dic[i] = a
for j in dic.value:
    r[n]=j
    n+=1
res=max(r)
num=a.count(res)   
print('{} {}'.format(res,num))


