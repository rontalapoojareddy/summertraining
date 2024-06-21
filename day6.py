'''def e(n1):
    k = 0
    c = 0
    for n in n1:
        if c == 0:
            k = n
            c = 1
        elif n == k:
            c += 1
        else:
            c-= 1
    c = 0
    for n in n1:
        if n == k:
            c += 1
    if c > len(n1) // 2:
        return k
    else:
        return "NO VALUE"
l = [6,6,7,7,7,6,6,7]
r = e(l)
print(r)'''

'''
a=[1,1,1,2,2,2,2,1,1]
c=1
p=a[0]
for i in range(1,len(a)):
    if (a[i]==p):
        c=c+1
    else:
        c=c-1
        if(c==0):
            c=1
            p=a[i]
print(p)
'''
'''n=7
a=[0,5,3,4,7,2,1]
b=sum(a)
n=(n*(n+1))//2
print(n-b)

'''


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
    def swaphalf(self):
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
            
            
    def evod(self,t,es,os):
        if(t==None):
            return abs(es-os)
        if(t.data%2==0):
            es=es+t.data
        else:
            os=os+t.data
        return self.evod(t.next,es,os)
    def prime(self,t,c):
        if(t==None):
            return c
        def primeornt(s,n):
            if(s>=(n//2)+1):
                return 1
            if(n%s==0):
                return 0
            return primeornt(s+1,n)
        if(primeornt(2,t.data)):
            c=c+1
        return self.prime(t.next,c)
l1=dll()
l1.addback(201)
l1.addback(30)
l1.addfront(11)
l1.addfront(40)
l1.display()
l1.revdisplay()
l1.search(20)
l1.hsearch(101)
#l1.evenorodd()
l1.pevenorodd()
l1.palindrome()
l1.swaphalf()
l1.display()
print(l1.evod(l1.head,0,0))
print(l1.prime(l1.head,0))
l1.display()



'''n=24
k=2
l=[]
for i in range(1,n):
    if n%i==0:
        l.append(i)
print(l)
a=len(l)-k
print(l[a])'''



''''import math
a=10
b=5
print(math.gcd(a,b)==1)'''



'''a=9
b=9
for i in range(2,(min(a,b)//2)+1):
             if (a%i==0) and (b%i==0):
                 print ("ncp")
                 break
else:
    print("cp")'''




'''a=input()
c,f=0,0
s=[]
for i in a:
    if(i in '{[('):
        c=c+1
        s.append(i)
    elif(not s):
        if(i=='}' and s[-1]=='{' or i==']' and s[-1]=='[' or i=='(' and s[-1]==')'):
            c=c-1
            s.pop()
        else:
            print(c)
            f=1
            break
    else:
        print(c)
        f=1
        break
        c=c+1
if(f==0):
    print(-1)
                
'''



