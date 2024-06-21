'''def bfs(st, d):
    l = [] #visited
    q = [st] #queue
    while q:
        n = q.pop(0)  #pop first element
        if n not in l:
            print(n, end=" ")  
            l.append(n)  
            for ne in d[n]:
                if ne not in l:
                    q.append(ne)
d= {5: [7, 3], 7: [5, 4, 3], 4: [7, 8, 2], 8: [3, 4, 2], 3: [5, 7, 8], 2: [4, 8]}
st=5
bfs(st, d)
'''
'''# other method explained in class
def bfs(d,n):
    vi=[]
    q=[n]
    while(q):
        for i in d[q[0]]:#d[q[0]]
            if(i not in q and i not in vi):
                q.append(i)
        vi.append(q.pop(0))
        print(vi[-1])
d= {5: [7, 3], 7: [5, 4, 3], 4: [7, 8, 2], 8: [3, 4, 2], 3: [5, 7, 8], 2: [4, 8]}
l=[]
bfs(d,5)
'''
'''# not executing dijkstra algorithm
g={5:[(3,1),(1,2),(6,3)],1:[(5,2),(2,1)],3:[(5,1),(6,3)]}
def fun(x):
    d={5:999,1:9999,3:9999,6:9999,2:9999}
    d[x]=0
    vi=[]
    q=[x]
    while(q):
        m=9999
        for i in q:
            if(d[i]<m):
                m=d[i]
                x=i
        for i in g[x]:
            if(i[0] not in vi):
                q.append(i[0])
                if d[i[0]]>i[1]+d[x]:
                    d[i[0]]=i[1]+d[x]
        vi.append(x)
        q.remove(x)
    return d
print(fun(1))
        '''
'''
def dijkstra(s):
    d1={1:999,2:999,3:999,4:999,5:999}
    d1[s]=0
    v=[]
    q=[s]
    while(q):
        m=9999
        for i in q:
            if d1[i]<m:
                m=d1[i]
                s=i
        for i in d[s]:
            if i[0] not in v:
                if d1[i[0]]>(d1[s]+i[1]):
                    d1[i[0]]=d1[s]+i[1]
                if i[0] not in q:
                    q.append(i[0]) 
        v.append(s)  
        q.remove(s)
    return (d1)

d={1:[(2,2),(3,2),(4,1)],2:[(1,2),(4,2),(5,3)],3:[(1,2),(4,3)],4:[(1,1),(2,2),(3,3),(5,2)],5:[(2,3),(4,2)]}
print("Dijkstra:",dijkstra(1))
        '''

#op:[13,11,9,15,9,7,5,11,11,9,7,13]

def fun(i):
    if i==len(l):
        return 
    if l[i]%2==0:
        def fun2(a,r,j,s,b):
            if j==len(a):
                r.append(s)
                return 
            if a[j]%2!=0:
                b.append(l[i]+a[j])
                s=s+l[i]+a[j] 
            fun2(a,r,j+1,s,b) 
        fun2(a,r,0,s,b) 
        fun(i+1)
    else: 
        fun(i+1)

l=[6,3,2,9,4,7]
a=[8,7,5,3,6,9]
r=[]
b=[]
s=0
fun(0) 
print(b)
print(r)


        