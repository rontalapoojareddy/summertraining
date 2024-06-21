'''# job sequencing
d=[(1,3),(2,5),(4,6),(6,7),(5,8),(7,9)]
a=[5,6,5,4,11,2]
b=a.copy()#[5,6,5,4,11,2]

for i in range(1,len(a)):
    for j in range(0,i):
        if d[j][1]<=d[i][0]:
            if(b[j]+a[i]>b[i]):
                b[i]=b[j]+a[i]
print(max(b))
            '''


'''s1="abcd"
s2="axbd" # if axbdc then out put as cba
m=[]
for i in range(len(s1)+1):
    l=[0]*(len(s2)+1)
    m.append(l)
for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        if(s1[i-1]==s2[j-1]):
            m[i][j]=m[i-1][j-1]+1
        else:
            m[i][j]=max(m[i][j-1],m[i-1][j])
print(m[len(s1)][len(s2)])
s=''
u,v=len(s1),len(s2)
while(u!=0 and v!=0):
    if(s1[u-1]==s2[v-1]):
        s=s+s1[u-1]
        u=u-1
        v=v-1
    else:
        if(m[u][v])==m[u-1][v]:
            u=u-1
        else:
            v=v-1
print(s)        
print(s[::-1])
'''


'''n = 4
a = [
    [0, 1, 0, 0, 1],
    [1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 1]
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
fun(1,5)
c=1
for i in range(n):

for j in range(n):
        if (a[i][j]==1):
            c=c+1
print(c)'''

'''
def fun(i,j,c):
    if(i<0 or j<0 or i>=n or j>=n or a[i][j]!=1):
        return c
    a[i][j]=2
    c+=1
    c=fun(i,j-1,c)
    c=fun(i,j+1,c)
    c=fun(i-1,j,c)
    c=fun(i+1,j,c)
    return c
a=[
    [0, 1, 0, 0, 1],
    [1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 1]
]
n=len(a)  
m = 0
co=0
for i in range(n):
    for j in range(n):
        if(a[i][j]==1):
            k=fun(i,j,0)
            if(k>m):
                m=k
            co=co+1
print(co,m)'''

'''
n=65476
d=n//360
m=d//30
w=m//6
print(d,m,w)
'''

'''
ip: 7262 sec
op: 2h:1m:2s

ip:500 sec
op: 0h:8m:20s
'''
'''
n=7262
rem1=n%3600
div1=n//3600
rem2=rem1%60
div2=rem1//60
print(div1,"h:",div2,"m:",rem2,"s")
'''

