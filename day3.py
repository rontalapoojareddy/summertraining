'''str=input()
str1=""
shift=int(input())
for i in str:
    c=ord(i)
    c-=shift
    if(c<97):
        r=97-c
        c=123-r
    str1+=chr(c)
print(str1)

ip:
   khoor     bcdmnwc   bvec
   3         9         4
op:hello     student   xray'''

# str="s"
# p=""
# c=ord(str)
# p=chr(c)
# print(c,p)

'''
a='bvec'
b=30
c=b%26
d=''
for i in a:
    if((ord(i)-c)>=97):
       d+=(chr(ord(i)-c))
    else:
        d+=(chr(ord(i)-c+26))
print(d)#xray'''

'''#ip:xyzabcdefklmnopqefgh op:7
s=input()
c=1
m=0
s=list(s)
for i in range(len(s)-1):
    if (ord(s[i+1])-ord(s[i]))==1:
        c=c+1
        m=max(m,c)
    else:
        c=1
print(m)
'''
'''ip:                                
    3
    xyz
    pqr
    abc
    "yraxpazr"
op:yes


4
abcd
xyze
pqrw
stuv
"cyptdzsayq" op:no 

n=int(input())
m=[]
for i in range(n):
    m.append(input())
s=input()
f=0
for i in range(len(s)):
    if(s[i] in m[i%n]):
        continue
    else:
        f=1
        break
if(f==1):
    print("no")
else:
    print('yes')'''

'''n=int(input())
m=[]
for i in range(n):
    m.append(list(input()))
s=input()
f=0
for i in range(len(s)):
    if(s[i] not in m[i % n]):
        print('no')
        f=1
        break
    else:
        m[i].remove(s[i])
        
if(f==0):
    print('yes')'''

'''def fun(x,re):
    if(x==0):
        return re
    re=re*10+(x%10)
    return fun(x//10,re)

#print(fun(123,0))
n=int(input())
if(n==fun(n,0)):
    print("pal")
else:
    print("np")'''

'''l=[]
# l=list(map(int,input().split()))
m1=0
for i in range(6):
    l.append(int(input()))
for i in range(len(l)):
    for j in range((i+1),len(l)):
        if(l[j]>l[i]):
            m=l[j]-l[i]
            m1=max(m,m1)
print("profit:",m1)

op:
                    
5
4
2
9
7
1
profit: 7


15
3
2
7
8
4
profit: 6

5
3
2
7
8
4
profit: 6


9
8
7
6
5
4
profit: 0'''
 
'''#logic
pr=[]
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if(a[i]<a[j] and a[j]-a[i] >pr):
            pr=a[j]-a[i]
print(pr)'''

'''
ip=5

op:
* * * * *
* 1 2 3 *
* 4 5 6 *
* 7 8 9 *
* * * * *

n=int(input())
c=1
for i in range(n):
    for j in range(n):
        if(i==0 or j==0 or i==n-1 or j==(n-1)):
            print('*',end=' ')
        elif(j!=(n-1)):  #else:
            print(c,end=' ')
            c=c+1
    print("\n")

'''

n=int(input())
for i in range(n):
    for j in ran