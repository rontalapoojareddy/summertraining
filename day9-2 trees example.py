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
    def addnodes(self,root,sum):
        if root is None:
            return sum
        if(root.data%2==0):
            sum += root.data
        sum = self.addnodes(root.left, sum)
        sum = self.addnodes(root.right, sum)
        return sum
    def addingnodes(self,root):
        if(root==None):
            return 0
        return root.data+self.addingnodes(root.left)+self.addingnodes(root.right)
    def addevennodes(self,root):
        if(root==None):
            return 0
        if(root.data%2==0):
            return root.data+self.addevennode(root.left)+self.addingnodes(root.right)
        
        return self.addingnode(root.left)+self.adding(root.right)
            
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
print("diffSum:",abs(t1.addingnodes(t1.root.left)-t1.addingnodes(t1.root.right)))
print("evenSum:",t1.addnodes(t1.root,0))






