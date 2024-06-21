'''def isprime(x):
    for i in range(2,(x//2)+1):
        if(x%i==0):
            return 0
    return 1

def lprime(n,m):
    for i in range(m-1,n,-1):
        if(isprime(i)):
            return i
    return 0

a=list(map(int,input().split()))
s=0
for i in range(len(a)-1):
    s=s+lprime(a[i],a[i+1])
print(s)
'''
'''#not proper output
def is_prime(x):
    for i in range(2,(x//2)+1):
        if x%i==0:
            return is_prime(x-1)
    else:
        return x

l=list(map(int,input().split()))
y=0
for i in range(len(l)-1):
    y+=is_prime(l[i+1])
print(y)
'''

#a=list(map(int,input().split()))
# a.sort()
# print(a)

'''a=list(map(int,input().split()))
for i in range(len(a)-2):
    if(a[i]>a[i+1]):
        a[i],a[i+1]=a[i+1],a[i]
    if(a[i+1]>a[i+2]):
        a[i+1],a[i+2]=a[i+2],a[i+1]
    if(a[i]>a[i+1]):
        a[i],a[i+1]=a[i+1],a[i]
print(a)'''

'''#a=input().split(',') op:oaxp
a="hello:5438,car:214,book:8799,apple:2187".split(',')
s=''
for i in a:
    b=i.split(":")
    print(b[0],b[1])
    l=len(b[0])
    if(str(l) in b[1]):
        s=s+b[0][-1]
    else:
        for i in range(l-1,0,-1):
            if(str(i) in b[1]):
                s=s+b[0][i-1]
                break
        else:
                s=s+'x'
print(s)'''



class node:
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
#     def addnodes(self,root,sum):
#         if root is None:
#             return sum
#         else:
#             sum += root.data
#             sum = self.addnodes(root.left, sum)
#             sum = self.addnodes(root.right, sum)
#             return sum
    def addingnodes(self,root):
        if(root==None):
            return 0
        return root.data+self.addingnodes(root.left)+self.addingnodes(root.right)
    def addevennodes(self,root):
        if(root==None):
            return 0
        if(root.data%2==0):
            return root.data+self.addevennodes(root.left)+self.addevennodes(root.right)
        else:
            return self.addevennodes(root.left)+self.addevennodes(root.right)
    
    def addoddnodes(self,root):
        if(root==None):
            return 0
        if(root.data%2!=0):
            return root.data+self.addoddnodes(root.left)+self.addoddnodes(root.right)
        else:
            return self.addoddnodes(root.left)+self.addoddnodes(root.right)
        
    def absdiff(self,root):
        if root==None:
            return 0
        if(root.data%2==0):
            return root.data+self.absdiff(root.left)+self.absdiff(root.right)
        else:
            return (self.absdiff(root.left)+self.absdiff(root.right))-root.data
        
    def height(self,root):
        if(root==None):
            return -1
        return max(self.height(root.left),self.height(root.right))+1
        
    def bal(self,root):
        
        return abs(self.height(root.left)-self.height(root.right))<=1
    def leaf(self,root,c):
        if root==None:
            return 0
        elif root.right==None and root.left==None:
            c=c+1
        return c+self.leaf(root.left,c)+self.leaf(root.right,c)
    def addleaf(self,root,s):
        if root==None:
            return 0
        elif root.right==None and root.left==None:
            
            s=s+root.data
        return s+self.addleaf(root.left,s)+self.addleaf(root.right,s)
    def search(self,root,s):
        if root==None:
            return "not found"
        if root.data==s:
           return "found"
        if(root.data>s):
            return self.search(root.left,s)
        else:
            return self.search(root.right,s)
        
    def depth(self,root,y,c):
        if(root==None):
            return -1
        if(root.data==y):
            return c
        if (root.data>y):
            return self.depth(root.left,y,c+1)
        else:
            return self.depth(root.right,y,c+1)
        
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
#print("Sum:",t1.addnodes(t1.root,0))
print("Sum:",t1.addingnodes(t1.root))
print("leftSum:",t1.addingnodes(t1.root.left))#left subtree
print("absalute diffSum:",abs(t1.addingnodes(t1.root.left)-t1.addingnodes(t1.root.right)))
print("evenSum:",t1.addevennodes(t1.root))
print("oddSum:",t1.addoddnodes(t1.root))

print("absolute difference by function",abs(t1.absdiff(t1.root)))
print("height",t1.height(t1.root))
#print("balt",t1.bal(t1.root)) # true or false
if(t1.bal(t1.root)):
    print("bal")
else:
    print("not bal")    

print("count of leaf nodes",t1.leaf(t1.root,0))

print("add the leaf ",t1.addleaf(t1.root,0))
print("Searching the element",t1.search(t1.root,10))
print("depth of the element",t1.depth(t1.root,7,0))
#print("left view",t1.leftview(t1.root,0))
print("left view")
t1.leftview(t1.root,0,[])
print("right view")
t1.rightview(t1.root,0,[])