'''class node:
    def __init__(self,u):
        self.data=u
        self.nxt=None

head=node(10)
b=node(20)
c=node(30)
head.nxt =b
b.nxt=c
print(head.data,head.nxt)
print(b.data,b.nxt)
print(c.data,c.nxt)
'''

'''class node:
    def __init__(self,u):
        self.data=u
        self.nxt=None
class sll:
    def __init__(self):
        self.head=None

    def display(self):
       
        t=self.head
        while(t!=None):
            
            print(t.data,end="->")
            
            t=t.nxt
    def addback(self,x):
        t=self.head
        while(t.nxt!=None):
            t=t.nxt
        t.nxt=node(x)
    def addfront(self,x):
        t=node(x)
        t.nxt=self.head
        self.head=t
        
    def search(self,x):
        t=self.head
        while(t!=None):
            if(t.data==x):
                return "found"
            t=t.nxt
        return "notfound"
    def addeven(self):
        t=self.head
        s1=0
        while(t!=None):
            if(t.data%2==0):
                s1=s1+t.data
                t=t.nxt
            else:
                t=t.nxt
        print(s1)
#     def addmiddle(self,x):
#         t=self.head
#         c=0
#         while(t!=None):
#             c+=1
#             t=t.nxt
#         c=c//2
#         t=self.head
#         for i in range(c):
#             t=t.nxt
#         print(t.data)
    def addmiddle(self):
        f=self.head
        s=self.head
        while(f!=None and f.nxt!=None):
            s=s.nxt
            f=f.nxt.nxt
            
        print(s.data)
    def length(self):
        s=self.head
        f=self.head
        while(f!=None and f.nxt!=None):
            s=s.nxt
            f=f.nxt.nxt
        if f==None:
            print("even")
        else:
            print("odd")
    def lon(self):
        t=self.
        
l1=sll()
l2=sll()
l1.head=node(10)
l1.addback(20)
l1.addback(30)
l2.head=node(100)
l2.addback(201)

l1.display()
print()
l2.display()
print()
l1.addeven()

l2.addeven()
print(l1.search(60))
l1.addmiddle()
print(l1.length())'''

class node:
    def __init__(self,u):
        self.data=u
        self.nxt=None
class sll:
    def __init__(self):
        self.head=None

    def display(self):
       
        t=self.head
        while(t!=None):
            
            print(t.data,end="->")
            t=t.nxt
       
    def addback(self,x):
        t=self.head
        while(t.nxt!=None):
            t=t.nxt
        t.nxt=node(x)
    def addfront(self,x):
        t=node(x)
        t.nxt=self.head
        self.head=t
    def search(self,x):
        t=self.head
        while(t!=None):
            
            if(t.data==x):
                print("found",x)
                break
            t=t.nxt
        else:
            print("not found")
            
    def middle(self):
       
        slow=self.head
        fast=self.head
        while(fast!=None and fast.nxt!=None):
            slow=slow.nxt
            fast=fast.nxt.nxt
            
        print(slow.data)
    def evenorodd(self):
        slow=self.head
        fast=self.head
       
        while(fast!=None and fast.nxt!=None):
            slow=slow.nxt
            fast=fast.nxt.nxt
            
        if(fast==None):
            print("even")
        else:
            print("odd")
       
    def allpair(self):
        t=self.head
        while(t.nxt!=None):
            t1=t.nxt
            while(t1!=None):
                print(t.data,t1.data)
                t1=t1.nxt
            t=t.nxt
    def bubble(self):
        c=0
        T=self.head
        p=None
        while(T.nxt!=None):
            f=0
            t=self.head
            while(t.nxt!=p):
                if (t.data>t.nxt.data):
                    f=1
                    t.data,t.nxt.data=t.nxt.data,t.data
                t=t.nxt
                c=c+1
            if(f==0):
                break
            p=t
            T=T.nxt
        return c
    def addeven(self):
        t=self.head
        s1=0
        while(t!=None):
            if(t.data%2==0):
                s1=s1+t.data
                t=t.nxt
            else:
                t=t.nxt
        print(s1)
        
    #def maxlength(self)
        
    
    
l1=sll()

l1.head=node(105)
l1.addback(60)
l1.addback(30)
l1.addback(40)
l1.addfront(5)
l1.search(6)
l1.display()
print()
l1.addeven()
l1.middle()
l1.evenorodd()
l2=sll()
l2.head=node(100)
l2.addback(201)
l2.addfront(25)
l2.addfront(42)
l2.search(201)

l2.display()
print()
l2.addeven()
l2.middle()
l2.evenorodd()
l1.allpair()
b=l1.bubble()
l1.display
print(b)

'''
class node:
    def _init_(self,u):
        self.data=u
        self.nxt=None
class sll:
    def _init_(self):
        self.head=None

    def display(self):
       
        t=self.head
        while(t!=None):
            
            print(t.data,end="->")
            t=t.nxt
       
    def addback(self,x):
        t=self.head
        while(t.nxt!=None):
            t=t.nxt
        t.nxt=node(x)
    def addfront(self,x):
        t=node(x)
        t.nxt=self.head
        self.head=t
    def search(self,x):
        t=self.head
        while(t!=None):
            
            if(t.data==x):
                print("found",x)
                break
            t=t.nxt
        else:
            print("not found")


    def sub(self):
        t=self.head  
       
        max1=0
        while(t.nxt!=None):
            if(t.data==t.nxt.data-1):
                p=p+1
                max1=max(max1,p)
                
            else:
                p=1
            t=t.nxt
        print("max sub string is",max1)
 
    def pairs(self):
        t=self.head
        t1=t.nxt
        print("pairs:")
        while(t.nxt!=None):
            while(t1!=None):

                print(t.data,t1.data)
                t1=t1.nxt
            t=t.nxt
            t1=t.nxt

    def bubble(self):
        
        T=self.head
        p=None
        while(T.nxt!=None):
            f=0
            t=self.head
            while(t.nxt!=p):
                if(t.data>t.nxt.data):
                    f=1
                    t.data,t.nxt.data=t.nxt.data,t.data
                t=t.nxt
            if(f==0):
                break
            p=t
            T=T.nxt
        l1.display() 
            
    def middle(self):
       
        slow=self.head
        fast=self.head
        while(fast!=None and fast.nxt!=None):
            slow=slow.nxt
            fast=fast.nxt.nxt
            
        print("middle element",slow.data)
    def evenorodd(self):
        slow=self.head
        fast=self.head
       
        while(fast!=None and fast.nxt!=None):
            slow=slow.nxt
            fast=fast.nxt.nxt
            
        if(fast==None):
            print("even")
        else:
            print("odd")
    
    

    
    
    def addeven(self):
        t=self.head
        s1=0
        while(t!=None):
            if(t.data%2==0):
                s1=s1+t.data
                t=t.nxt
            else:
                t=t.nxt
        print("sum of even",s1)
l1=sll()

l1.head=node(2)
l1.addback(1)
l1.addback(6)
l1.addback(8)
l1.addfront(6)
l1.search(6)
l1.display()
print()
l1.addeven()
l1.middle()
l1.sub()
l1.pairs()
l1.bubble()
print()
l1.evenorodd()
# l2=sll()
# l2.head=node(100)
# l2.addback(201)
# l2.addfront(24)
# l2.addfront(25)
# l2.search(201)

# l2.display()
# print()
# l2.addeven()
# l2.middle()
# l2.evenorodd()
# l2.sub()
# l2.pairs()'''