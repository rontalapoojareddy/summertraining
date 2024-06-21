'''q=int(input())
l1=[]
l2=[]
l3=[]
c=0
c1=0
for i in range(q):
    x=input()
    if x[0]=="1":
        l1.append(x[1:])
    elif x[0]=="4":
        if x[1:] in l1:
            l1.remove(x[1:])
    else:
        l2.append(x)
for i in l2:
    if i[0]=="2":
        for j in l1:
            if i[1:]==j:
                c=c+1
        if c!=0:
            print("True")
        else:
            print("False")
        c=0
    else:
        for j in l1:
            if i[1:]==j[:len(i[1:])] and i not in l3:
                c=c+1
                l3.append(i)
        if c!=0:
            print("True")
        else:
            print("False")
        print(c)
        c=0
print(l1)
print(l2)
'''
class node:
    def __init__(self):
        self.d={}
        self.flag=0  
class tries:
    def __init__(self):
        self.root=node()
    def insert(self,str):
        t=self.root
        for i in str:
            if(i not in t.d):
                t.d[i]=node()
            t=t.d[i]
        t.flag=1
    def search(self,str):
        t=self.root
        for i in str:
            if(i not in t.d):
                return False
            t=t.d[i]
        if(t.flag==1):
            return True
        else:
            return False
    def searchprefix(self,str):
        t=self.root
        for i in str:
            if(i not in t.d):
                return False
            t=t.d[i]
        return True
    def print_all_prefix(self,str):
        def fun(t,s):
            if(t.flag==1):
                print(s)
            for i in t.d:
                fun(t.d[i],s+i)
        t=self.root
        s=""
        for i in str:
            if(i in str):
                s=s+i
                t=t.d[i]
            else:
                return
        fun(t,s)
t1=tries()
n=int(input())
for i in range(n):
    a,s=input().split()
    if a=='1':
        t1.insert(s)
    if a=='2':
        print(t1.search(s))
    if a=='3':
        print(t1.searchprefix(s))
    if(a=='4'):
        print(t1.print_all_prefix(s))
        
        
'''op:6 
1 apple
1 word
1 world
1 wow
3 wo
True
4 wo
word
world
wow
None


6
1 word
1 world
1 words
2 word
True
2 wor
False
3 wo
True'''