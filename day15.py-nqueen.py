'''def Nqueen(board,r):
    if r==len(board):
        return True
    for c in range(len(board)):
        if issafe(board,r,c):
            board[r][c]="1"
            if Nqueen(board,r+1):
                return True
            board[r][c]='0'
    
def issafe(board,r,c):
    for i in range(r):
        if board[i][c]=="1":
            return False
    i,j=r,c
    while i>=0 and j<len(board):
        if board[i][j]=="1":
            return False
        i=i-1
        j=j+1
    i,j=r,c
    while i>=0 and j>=0:
        if board[i][j]=="1":
            return False
        i=i-1
        j=j-1
    return True
n=int(input("enter number of queens:"))
board=[["0" for i in range(n)] for j in range(n)]
if Nqueen(board,0):
    for i in board:
        print("".join(i))
else:
    print(False)'''


'''
def Nqueen(board,r,r1,c1):
    if r==len(board):
        return 
    if r!=r1:
        for c in range(len(board)):
            if issafe(board,r,c,c1):
                board[r][c]="1"
                break
        
            board[r][c]='0'
        return Nqueen(board,r+1,r1,c1)

    else:
        Nqueen(board,r+1,r1,c1)
def issafe(board,r,c,c1):
    for i in range(r):
        if c==c1:
            return False
        if board[i][c]=="1":
            return False
        
    i,j=r,c
    while i>=0 and j<len(board):
        if board[i][j]=="1":
            return False
        i=i-1
        j=j+1
    i,j=r,c
    while i>=0 and j>=0:
        if board[i][j]=="1":
            return False
        i=i-1
        j=j-1
    return True
n=int(input("enter number of queens:"))
r1=int(input())
c1=int(input())
board=[["0" for i in range(n)] for j in range(n)]
Nqueen(board,0,r1,c1)
for i in board:
        print("".join(i))
        
ip:
enter number of queens:5 
1
3
op:
10000
00000
01000
00001
00100 '''



'''#l1=[3,4,5,10,4,3]
l1=[3,5,9,6,8,10]
c1=1
k=l1[0]
for i in range(1,len(l1)):
    if k<l1[i]:
        k=l1[i]
        c1=c1+1
print(c1)
c1=1
k=l1[-1]
for i in range(len(l1)-1,-1,-1):
    if k<l1[i]:
        k=l1[i]
        c1=c1+1
print(c1)'''

'''a = 'tu5g2k1h8'
b = 'g5g8gd6h3'

al= [char for char in a + b if char.isdigit()]
u=list(set(al))
u.sort(reverse=True)
l = ''.join(u)
print(l)'''

'''
# l=[2,3,5,6]
# n=11
l=list(map(int,input().split()))
n=int(input())
m=[]
for i in range(len(l)):
    l1=[0]*(n+1)
    m.append(l1)
for i in range(len(l)):
    for j in range(n+1):
        if j==0 or j==l[i]:
            m[i][j]=1
        elif j<l[i]:
            m[i][j]=m[i-1][j]
        else:
            k=j-l[i]
            if m[i-1][k]==1 or m[i-1][j]==1:
                m[i][j]=1
print(m)
if m[len(l)-1][n]==1:
    print("True")
else:
    print("False")'''


'''#find if we can form the value with the numbers in the list
l1=[2,3,5,6]
val=11
l2=[0]*(val+1)
l2[0]=1
l3=l2.copy()
for i in l1:
    for j in range(i,val+1):
        l3[j]=max(l2[j-i],l2[j])
    l2=l3.copy()
print(l3[-1])'''
 
''' #print the largest even number by taking uniqe numbers from strings
st="tu5g2k1h8"
st1="g5g8gd6h3"
nu=""
for i in st:
    if i.isdigit() and i not in nu:
        nu=nu+i
for i in st1:
    if i.isdigit() and i not in nu:
        nu=nu+i
num=list(nu)
num.sort()
nu=num[::-1]
print(nu)
if int(nu[-1])%2==0:
    print(int("".join(nu)))
else:
    for i in range(len(nu)-2,-1,-1):
        if int(nu[i])%2==0:
            t=nu[i]
            nu[i]=nu[-1]
            nu[-1]=t
            k=i
            while(k<len(nu)-2):
                if nu[k]<nu[k+1]:
                    t=nu[k]
                    nu[k]=nu[k+1]
                    nu[k+1]=t
                k=k+1
            break
    print(int("".join(nu)))
 
 '''

'''
# a = 'tu5g2k1h8'
# b = 'g5g8gd6h3'
a = input()
b = input()
c=set()
for i in a:
    if(i.isdigit()):
        c.add(i)
for i in b:
     if(i.isdigit()):
        c.add(i)
d=list(sorted(c,reverse=True))
if(int(d[-1])%2==0):
    print(''.join(d))
else:
    for i in range(len(d)-2,-1,-1):
        if(int(d[i])%2==0):
            d.append(d.pop(i))
            print(''.join(d))
            break
    else:
        print(-1)
  '''  

'''n=int(input())
m=n
rev=0
while n>0:
    rev=rev*10+(n%10)
    n=n//10
if(m==rev):
    print("p")
else:
    print("np")
    m += 1
    while True:
        n = m
        rev = 0
        while n > 0:
            rev = rev * 10 + (n % 10)
            n = n // 10
        if m == rev:
            print(m)
            break
        m += 1'''

ip='abdbsdabca' #op:bdb
