# n=input()
# m=sum(list(map(int,n)))
# print(m)

'''
recursion bringing the return value out
def fun(x):
    if(x==3):
        return 500
    print(x)
    t=fun(x+1)
    print(x)
    return t
print(fun(1))
o/p:
1
2
2
1
500'''
'''def add(n):
    s=0
    while(n):
        s=s+(n%10)
        n=n//10
    return s
def pnp(x):
    if(n in [2,3,5,7]):
        return m
    else:
        return m+1
n=int(input())
m=n
while(1)
    if(n<10):
        print(pnp(n))
    else:
        while(1):
            n=add(n)
            if(n<10):
                break
        print(pnp(n))'''

'''def fun(x,s):
    if (x==len(a)):
        return s
    s=s+a[x]
    return fun(x+1,s)
a=[6,7,2,5]
print(fun(0,0))'''
'''def fun(i,s1,s2):
    if(i==len(a)):
        return s1,s2
    if(a[i]%2==0):
        s1=s1+a[i]
    if(b[i]%2!=0):
        s2=s2+b[i]
    return fun(i+1,s1,s2)
a=[3,8,5,4,3]
b=[5,0,9,3,2]
x,y=fun(0,0,0)
print(x,y)'''

'''def fa(x):
    if(x==1):
        return 1
    return x*fa(x-1)
print(fa(5))'''

'''
n=10 add all even nos
def fa(x):
    if(x==0):
        return 0
    return x+fa(x-2)
print(fa(10))

o/p: 30 '''

'''add all even nos
def fa(x):
    if(x==0):
        return 0
    return x+fa(x-2)
n=13
if(n%2==0):
    print(fa(n))
else:
    print(fa(n-1))
    '''

'''def fun(i):
    if(len(i)%2==0):
        print("yes")
    else:
        print("no")
        return
i=[5,8,9,5,2,4.7]
fun(i)'''

'''a=[5,8,9,5,2,4.7]
print(type(id(a[0])))'''

'''a=[10,4,8,3]
b=[]
for i in range(len(a)):
    b.append(abs(sum(a[:i])-sum(a[i+1:])))
print(b)'''

'''ip="MMFFMMFFMMFFF"
c,s=0,0
for i in ip:
    if i=='M':
        c=c+1
    if i=='F':
        s=s+1
if(c==s):
    print('0')
elif(c>s):
    print('M')
else:
    print('F')
    '''
'''# for space complexity we use logic as
ip="MMFFMMFFMMF"
c=0
for i in ip:
    if i=='M':
        c=c+1
    else:
        c=c-1
if(c==0):
    print('0')
elif(c>0):
    print('M')
else:
    print('F')'''

'''a="leet**cod*e"
b=[]
for i in a:
    if i!='*':
        b.append(i)
    else:
        b.pop()
print(b)
print(''.join(b))

o/p: ['l', 'e', 'c', 'o', 'e']
lecoe'''

a="is2 sentence4 this1 a3"
a=a.split()
i=0
re=[0]*len(a)
for i in a:
    re[int(i[-1])-1]=i[:-1]
    
print(' '.join(re))