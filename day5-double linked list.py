class node:
    def __init__(self,x):
        self.next=None
        self.data=x
        self.prev=None

class  dll:
    def __init__(self):
        self.head=None
        self.tail=None

    def display(self):
        t=self.head
        while(t!=None):
            print(t.data,end="->")
            t=t.next
        print()
    def addback(self,x):
        if(self.head==None):
            self.head=node(x)
            self.tail=self.head
        else:
            #self.tail.next=node(x)
            #self.tail.next.prev=self.tail
            #self.tail=self.tail.next
            t=node(x)
            self.tail.next=t
            t.prev=self.tail
            self.tail=self.tail.next

    def addfront(self,x):
        if(self.head==None):
            self.head=node(x)
            self.tail=self.head
        else:
            #self.head.prev=node(x)
            #self.head.prev.next=self.head
            #self.head=self.head.prev
            t=node(x)
            t.next=self.head
            self.head.prev=t
            self.head=t
    def revdisplay(self):
        t=self.tail
        while(t!=None):
            print(t.data,end="->")
            t=t.prev
        print()
    def search(self,x):
        t=self.head
        while(t!=None):
            if(t.data==x):
                print("found",x)
                break
            t=t.next
        else:
            print("not found")
    
    def hsearch(self,x):
        t=self.head
        t1=self.head
        while(t!=t1 and t!=t1.next):
            if(t.data==x or t1.data==x):
                #print("found",x)
                break
            t=t.next
            t1=t1.prev
        if(t.data==x):
            print("found")
        else:
            print("not found")
    def evenorodd(self):
        slow=self.head
        fast=self.head
       
        while(fast!=None and fast.next!=None):
            slow=slow.next
            fast=fast.next.next
            
        if(fast==None):
            print("even")
        else:
            print("odd")
    def pevenorodd(self):
        t=self.head
        t1=self.tail
        while(t!=t1 and t!=t1.next):
            t=t.next
            t1=t1.prev
        if(t==t1):
            print("odd")
        else:
            print("even")
    def palindrome(self):
        t=self.head
        t1=self.tail
        while(t!=t1 and t!=t1.next):
            if(t.data!=t1.data):
                print("np")
                return 0
            t=t.next
            t1=t1.prev
        print("p")
        return 1
    def swap(self):
        f=self.head
        s=self.head
        while(f!=None):
            f=f.next.next
            s=s.next
        f=self.head
        while(s!=None):
            s.data,f.data=f.data,s.data
            s=s.next
            f=f.next
l1=dll()
l1.addback(20)
l1.addback(30)
l1.addfront(10)
l1.addfront(40)
l1.display()
l1.revdisplay()
l1.search(20)
l1.hsearch(101)
#l1.evenorodd()
l1.pevenorodd()
l1.palindrome()
l1.swap()
l1.display()
