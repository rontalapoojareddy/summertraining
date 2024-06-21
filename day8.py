'''#a = [1, 2, 3, 4, 1, 2, 3, 1, 2]
a=[2,3,1,3,4,3,2] # op:[[2, 3, 1], [3, 4], [3, 2]]
#a=[4,5,2,1] #[[4, 5, 2, 1]]
r= []
c= []
for i in a:
    if i in c:
        r.append(c)
        c= [i]
    else:
        r.append(i)
if c:
    r.append(c)
print(r)
'''
'''
a=[2,3,1,3,4,3,2]
m=[]
c=0
while(c!=len(a)):
    r=[]
    for i in range(len(a)):
        if (not str(a[i]).isalpha()):
            if(a[i] not in r):
                c=c+1
                r.append(a[i])
                a[i]='a'
    m.append(r)
print(m)
'''
'''#using dictionaries
a=[2,3,1,3,4,3,2]
d={}
m=[]
c=0
for i in a:
    if(i not in d):
        d[i]=1
    else:
        d[i]=d[i]+1
while(c!=len(a)):
    r=[]
    for i in d:
        if (d[i]!=0):
            d[i]=d[i]-1
            c=c+1
            r.append(i)
    m.append(r)
print(m)
'''
'''
l='the quick brown for juumps over the lazy dog'
a=set(l)
if len(a)==27:
    print("yes")
else:
    print("no")'''

'''#a='the 4quick br$%^own foENDx j45umps o.ver the lazy dog'
a=input()
for i in range(97,123):
    if(chr(i) not in a):
        print("no")
        break
else:
    print("yes")'''


'''a=input()
d={}
for i in a:
    if(i.islower()):
        if(i not in d):
            d[i]=1
print(d)'''

'''a=input()
d=set()
for i in a:
    if(i.islower()):
        d.add(i)
print(d)'''

'''
a=input()
d=[0]*26
for i in a:
    if(i.islower()):
        d[ord(i)-97]=1
print(d)'''


'''a=input()
d=[0]*26
for i in a:
    if(i.islower()):
        d[ord(i)-97]+=1
print(d)'''

'''
a=input()
d=[0]*26
for i in a:
    if(i.islower()):
        d[ord(i)-97]=1
print(all(d))'''

'''
# Input string
s = "abfgresagtyuiofde"
l = {}
m= 0
st= 0
for i in range(len(s)):
    ch = s[i]
    if ch in l:
        st = max(st, l[ch] + 1)
    l[ch] = i
    m = max(m, i - st + 1)
print(m)
'''

'''#not executing

a = "abfgresagtyuiofds"
d={}
s=''
m=0
i=0
while(i<len(a)):
    while(i<len(a)):
        if (a[i] not in s):
            s=s+a[i]
            d[s[i]]=i
        else:
            if(len(s)>m):
                m=len(s)
            s=""
            break
        i=i+1
    i=d[a[i]]+1
print(m)'''


"""
ip: 6
    0 1 1 1 0 1
    0 1 0 1 0 0
    1 0 1 1 0 0 
    0 0 0 1 1 1
    1 1 0 0 0 1 
    1 1 1 0 1 0 
    4 6

op: 8


n = 6
a = [
    [0, 1, 1, 1, 0, 1],
    [0, 1, 0, 1, 0, 0],
    [1, 0, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 1],
    [1, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 0]
]
def fun(i,j):
    if (i<0 or j<0 or i>=n or j>=n or a[i][j]!=1):
        return
    if (a[i][j]==1):
        a[i][j]=2
    fun(i-1,j)
    fun(i,j-1)
    fun(i+1,j)
    fun(i,j+1)
    return
fun(3,5)
c=0
for i in range(n):
    for j in range(n):
        if (a[i][j]==1):
            c=c+1
print(c)
# op:8
"""

# 
# def fun(l,i,j,n): 
#     if(i<0 or j<0 or i>=n or j>=n or l[i][j]!=1):
#         return
#     if l[i][j]==1:
#         l[i][j]=2
#     fun(l,i-1,j,n)
#     fun(l,i,j-1,n)
#     fun(l,i+1,j,n)
#     fun(l,i,j+1,n)
#     return 
# 
# n=int(input())
# l=[]
# co=0
# for i in range(n):
#     l1=[]
#     for j in range(n):
#         l1.append(int(input()))
#     l.append(l1)
# r=int(input())
# c=int(input())  
# fun(l,r-1,c-1,n) 
# for i in range(n):
#     for j in range(n):
#         if l[i][j]==1:
#             co=co+1
# print(l)
# print("Trees:",co)

'''ip:6
0
1
1
1
0
1
0
1
0
1
0
0
1
0
1
1
0
0
0
0
0
1
1
1
1
1
0
0
0
1
1
1
1
0
1
0
4 
6
op:[[0, 2, 2, 2, 0, 1], [0, 2, 0, 2, 0, 0], [1, 0, 2, 2, 0, 0], [0, 0, 0, 2, 2, 2], [1, 1, 0, 0, 0, 2], [1, 1, 1, 0, 1, 0]]
Trees: 8'''


class node:
    def __init__(self,u):
        self.data=u
        self.left=None
        self.right=None
class tree:
    def __init__(self):
        self.root=None
    def creat(self,root,x):
        if(root==None):
            self.root=node(x)
        elif(root.data>x):
            self.creat(root.left,x)
        else:
            self.creat(root.right,x)
t1=tree()
t1.creat(t1.root,10)
t1.creat(t1.root,5)
t1.creat(t1.root,2)
t1.creat(t1.root,8)