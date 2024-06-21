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
print(t1.search(t1.root,10))
print(t1.depth(t1.root,7,0))







'''
i=5
for i in range(7):
    i=i+2
    print("hi")
print(i)
'''

'''i=5
for i in range(7):
    #i=i+2
    print("hi")
print(i)
'''

'''for i in range(4):
    i=i+2000
    print("hi")
print(i)
'''

'''for i in [3,6,10,13]:# sequence
    print(i)'''

'''for i in {3,6,10,13}:
    print(i) #no sequence'''

'''a=[30,20,40,14]
for i in range(4):
    print(a[i])'''