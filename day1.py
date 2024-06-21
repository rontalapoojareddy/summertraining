'''# ip:2 5 7 9
#     1 3 6 7 10 13
#     
# op: 1 2 3 5 6 7 7 9 10 13 list,set,strings,userdefine,lamda function

# l= list(map(int,input().split()))
# m= list(map(int,input().split()))
# c=l+m
# c.sort()
# print(c)

# l=[2,5,7,9]
# m=[1,3,6,7,10,13]
# i,j=0,0
# c=[]
# while i<len(l) and j<len(m):
#     if l[i]<m[j]:
#         c.append(l[i])
#         i=i+1
#     else:
#         c.append(m[j])
#         j=j+1
# while j<len(m): #if(j<len(m)):
#     c.append(m[j]) # c.extend(m[j:])
#     j=j+1
# while i<len(l):#if(i<len(l)):
#     c.append(l[i])# c.extend(a[i:])
#     i=i+1
# print(c)'''

'''# ip: aaabbaaaaddd   op:a3b2a4d3
a="aaabbaaaadddb"
b=''
c=1
for i in range(len(a)-1):
    if(a[i]==a[i+1]):
        c=c+1
    else:
        b=b+a[i]+str(c)
        c=1
b=b+a[-1]+str(c)#a[i+1] is also possible in place of a[-1] but a[i] is not possible.
print(b)'''

'''#ip:3 5 4 3 6 7 1 2 4 3 3 7 6 8 8
#op: 3-4
     #5-1
     #4-2
     #6-2
     #7-2
     #1-1
     #2-1
     #8-2
    
# a=[3,5,4,3,6,7,1,2,4,3,3,7,6,8,8]
# b={}
# c=0
# for i in a:
#     if i in b:
#         b[i]+=1
#     else:
#         b[i]=1
# for i,c in b.items():
#     print(i,"-",c)

# a=[3,5,4,3,6,7,1,2,4,3,3,7,6,8,8]
# b=[]
# for i in a:
#     if(i not in b):
#         b.append(i)
# for i in b:
#     print(i,'-',a.count(i))'''


'''# ip:f46feLK9y56u#@&56hIjbn6KJhA
#o/p:lv-2 uv-2 lc- uc- d- s-

a='f46feLK9y56u#@&56hIjbn6KJhA'
uv,uc,lv,lc,d,s=0,0,0,0,0,0
for i in a:
    if(i.isupper()):
        if(i in 'AEIOU'):
            uv=uv+1
        else:
            uc=uc+1
    elif(i.islower()):
        if(i in 'aeiou'):
            lv=lv+1
        else:
            lc=lc+1
    elif(i.isdigit()):
        d=d+1
    elif(not i.isalnum()): #else:
        s=s+1
print('UV -',uv)
print('UC -',uc)
print('LV -',lv)
print('LC -',lc)
print('D -',d)
print('S -',s)

O/P:
UV - 2
UC - 4
LV - 2
LC - 8
D - 8
S - 3'''

'''#ip:placements    op:plAcEmEnts
#ip:School      op:schOOl

a='placements'
b=''

for i in a:
    if(i in 'aeiou'):
        i.upper()
print(i)  # NOT COMPLETED'''

'''a=[5,3.8,7,5.6,4,2,3]
i,e,o,f=0,0,0,0.0
for i in a:
    if(i%2==0):
        e=e+i
    elif(i%2==1):#elif isinstance(i,float):   f+=i
        o=o+i
    else:   # o+=i
        f=f+i
print(e)
print(o)
print(f)

i/p:[5,3.8,7,5.6,4,2,3]
o/p:
6
15
9.39999999

'''
'''
a=300
b=400
print(abs((300/7)-(400/7))) # for i in range(a,b+1,7):#     print(i) # the nos between 300 and 400 divisible by 7

o/p:14.285714285714292'''

'''# n=int(input())
# c=0
# for i in range(1,n+1):
#     if n%i==0:
#         c=c+1
# if(c==2):
#     print("prime")
# else:
#     print("not prime")


    
# n=int(input())
# c=0
# for i in range(2,(n//2)+1):
#     if n%i==0:
#         c=c+1
#         break
# if(c==0):
#     print("prime")
# else:
#     print("not prime")
        
        
n=int(input())
while(1):
    c=0
    for i in range(2,(n//2)+1):
        if n%i==0:
            c=c+1
            break
    if(c==0):
        print(n)
        break
    else:
    n=n+1
o/p:
15   
17

13
13'''

'''n=int(input())
c=0
while(n):
    if(n%10 in [2,3,5,7]):
        c=c+1
    n=n//10
print(c)

o/p:
35723
5'''

n=input()
c=0
m,u,l,s,d=0,0,0,0,0
for i in n:
    if(i.isdigit()):
        d=1
    elif(i.islower()):
        l=1
    elif(i.isupper()):
        u=1
    else:
        s=1
m=4-(u+l+d+s)
if (len(n)+m)<8:
    print(8-len(n))
else:
    print(m)