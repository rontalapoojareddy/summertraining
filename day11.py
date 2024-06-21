'''class node:
    def __init__(self,u):
        self.data=u
        self.left=None
        self.right=None
        
class tree:
    def __init__(self):
        self.root=None
    def create(self,root,x):
        if(root==None):
            return node(x)
        elif(root.data>x):
            root.left=self.create(root.left,x)
        else:
            root.right=self.create(root.right,x)
        return root
    def inorder(self,root):
        if(root):
            self.inorder(root.left)
            print(root.data,end="->")
            self.inorder(root.right)
            
    def preorder(self,root):
        if(root):
            print(root.data,end="->")
            self.preorder(root.left)
            self.preorder(root.right)
    def postorder(self,root):
        if(root):
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end="->")
    def leftview(self,root,c,l):
        if(root==None):
            return
        if(c not in l):
            l.append(c)
            print(root.data,c)
        self.leftview(root.left,c+1,l)
        self.leftview(root.right,c+1,l)
        
    def rightview(self,root,c,l):
        if(root==None):
            return
        if(c not in l):
            l.append(c)
            print(root.data,c)
        self.rightview(root.right,c+1,l)
        self.rightview(root.left,c+1,l)
    def topview(self,root):
        if (root==None):
            return 
        d={}
        q=[(root,0)]
        while q:
            root=q[0][0]
            if(root.left!=None):
                q.append((root.left,q[0][1]-1))
            if(root.right!=None):
                q.append((root.right,q[0][1]+1))
            if (q[0][1] not in d):
                d[q[0][1]]=root.data
            q.pop(0)
        for i in sorted(d):
            print(d[i],sep=",")
    def bottom(self,root,c,d,q):
        if root==None:
            return
        
        d={}
        q=[(root,0)]
        while(q):
            root=q[0][0]
            if(root.left!=None):
                q.append((root.left,q[0][1]-1))
            if(root.right!=None):
                q.append((root.right,q[0][1]+1))
            
            d[q[0][1]]=root.data
            q.pop(0)
        print(d)
        for i in sorted(d):
            print(d[i],end=" ")
            
    
        
t1=tree()
t1.root=node(10)
t1.create(t1.root,5)
t1.create(t1.root,20)
t1.create(t1.root,7)
t1.create(t1.root,1)

print("Inorder Traversal")

t1.inorder(t1.root)
print()
print("Preorder Traversal")
t1.preorder(t1.root)
print()
print("Postorder Traversal")
t1.postorder(t1.root)
print()
print("left view")
t1.leftview(t1.root,0,[])
print("right view")
t1.rightview(t1.root,0,[])
print("top view")
t1.topview(t1.root)
#print()
print("bottom view")
t1.bottom(t1.root,0,{},[])
print()
'''


'''def dfs(n, d, l):
    if n not in l:
        print(n, end=" ")  
        l.append(n) 
        for i in d[n]:
            dfs(i, d, l)  
d={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
l=[]
n=5
dfs(n, d, l)'''


'''def dfs(d,x):
    l.append(x)
    for i in d[x]:
        if i not in l:
            dfs(d,i)
d={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
l=[]
dfs(d,5)
print(l)'''


'''
def allpaths(n, d):
    l.append(n) 
    if(n==2):
        print(l)
        l.pop()
        return
    
    for i in d[n]:
        if i not in l:
            allpaths(i, d)
    l.pop()
d={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
l=[]
allpaths(5, d)'''

#d={5:[(7,2),(3,1)],7:[(5,2),(4,3),(3,4)],4:[(7,3),(8,5),(2,1)],8:[(3,2),(4,5),(2,1)],3:[(5,1),(7,4),(8,2)],2:[(4,1),(8,1)]}

'''def allpathssum(n, d, l=None, cost=0):
    if l is None:
        l = []
    l.append(n)
    if n == 2:
        print("Path:", l)
        print("Cost:", cost)
        l.pop()
        return
    for i in d[n]:
        if i[0] not in l: 
            allpathssum(i[0], d, l, cost + i[1])   
    l.pop()

d={5:[(7,2),(3,1)],7:[(5,2),(4,3),(3,4)],4:[(7,3),(8,5),(2,1)],8:[(3,2),(4,5),(2,1)],3:[(5,1),(7,4),(8,2)],2:[(4,1),(8,1)]}
l = []
n=5
allpathssum(n, d)'''


'''
def dfsallpathscost(n,d,l,cost):
    if l==None:
        l=[]
    l.append(n)
    if n == 2:
        print(l,cost)
        l.pop()
        return
    for i in d[n]:
        if i[0] not in l:  
            dfsallpathscost(i[0],d,l,cost+i[1]) 
    l.pop()

d={5:[(7,2),(3,1)],7:[(5,2),(4,3),(3,4)],4:[(7,3),(8,5),(2,1)],8:[(3,2),(4,5),(2,1)],3:[(5,1),(7,4),(8,2)],2:[(4,1),(8,1)]}
l = []
dfsallpathscost(5, d,None,0)
'''

'''def dfscount(n,d,e,c):
    l.append(n)
    if(n==e):
        c=c+1
        l.pop()
        return c
    for i in d[n]:
        if i not in l:
            c=dfscount(i,d,e,c)
    l.pop()
    return c
d={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
l=[]
print(dfscount(5,d,2,0))'''


'''def dfsmincostpath(d,n,e,cost,m,l1):
    l.append(n)
    if n == e:
        if(cost<m):
            m=cost
            l1=l.copy()
        l.pop()
        return m,l1
    for i in d[n]:
        if i[0] not in l:  
            m,l1=dfsmincostpath(d,i[0],e,cost+i[1],m,l1) 
    l.pop()
    return m,l1
d={5:[(7,2),(3,1)],7:[(5,2),(4,3),(3,4)],4:[(7,3),(8,5),(2,1)],8:[(3,2),(4,5),(2,1)],3:[(5,1),(7,4),(8,2)],2:[(4,1),(8,1)]}
l = []
print(dfsmincostpath(d,5,2,0,99999,[]))'''



def dfsmincostpathofallnodes(d,n,e,cost,m,l1):
    l.append(n)
    if n == e:
        if(cost<m):
            m=cost
            l1=l.copy()
        l.pop()
        return m,l1
    for i in d[n]:
        if i[0] not in l:  
            m,l1=dfsmincostpathofallnodes(d,i[0],e,cost+i[1],m,l1) 
    l.pop()
    return m,l1
d={5:[(7,2),(3,1)],7:[(5,2),(4,3),(3,4)],4:[(7,3),(8,5),(2,1)],8:[(3,2),(4,5),(2,1)],3:[(5,1),(7,4),(8,2)],2:[(4,1),(8,1)]}
l = []
for i in d.keys():
    print(dfsmincostpathofallnodes(d,5,i,0,99999,[]))