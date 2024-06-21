'''a=list(map(int,input().split()))
#a = [3, 2, 5, 4, 1, 6, 8]
if len(a) < 3:
    print("3 nos minimum")
else:
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            for k in range(j + 1, len(a)):
            
                print((a[i], a[j], a[k]))
'''
'''def comb(arr,n,s=0,c=[]):#comb=combinations,c=cuttent position
    if len(c) == n:
        print(list(c))
        return
    for i in range(s,len(arr)):
        comb(arr, n, i + 1, c + [arr[i]])
#a = list(map(int, input().split()))
a = [3, 2, 5, 4, 1, 6, 8]

comb(a, 3)
'''

'''def comb(l,k):#comb-combinations, c=current,s=start
    def fun(c,s):
        if len(c)==k:
            print(c)


return
        for i in range(s,len(l)):
            fun(c+[l[i]],i+1)
        return
    fun([],0)
#a = list(map(int, input().split()))
a=[3,2,5,4,1,6,8]
#k=int(input())
k=3
comb(a,k)'''



# l='school'
# n=3
# L=2
# R=3
# S=1
# c=[]
# for i in range(len(l)-1):
#     if i==L or i==R or i==S:
#         c.append(l[i])
# print(c)
# for i in range(len(l)-n+1):
#     subset = [l[i],l[i+1],l[i+2]]
#     print(subset)
#     if sorted(c) == sorted(subset):
#         print("yes")
# '''
# '''a=input()
# n=int(input())
# str=''
# for i in range(n):
#     b=input()
#     if(b[0]=='L'):
#         str=str+a[int(b[2])]
#     else:
#         str=str+a[-int(b[2])]
# print(str)
# '''Upto here OP:school
# 3
# L 2
# R 3
# L 1
# hoc'''
# str=list(str)
# str.sort()
# b=[]
# for i in range(len(a)-n+1):
#     t=list(a[i:n+i])
#     t.sort()
#     b.append(t)
# print(b)
# print(str)
# for i in b:
#     if(i==str):
#         print("yes")
#         break
# else:
#     print("no")
# '''    
# ip:school
# 3
# L 2
# R 3
# L 1
# 
# op:hoc
# [['c', 'h', 's'], ['c', 'h', 'o'], ['h', 'o', 'o'], ['l', 'o', 'o']]
# ['c', 'h', 'o']
# yes
#     '''

'''
to check a no is framed by adding 2 prime nos or not
def isprime(x):
    if(x==1):
        return 1
    if(x==2):
        return 1
    for i in range(2,(x//2)+1):
        if(x%i==0):
            return 0
    return 1

a=int(input())
for i in range(1,(a//2)+1):
    if(isprime(i) and isprime(a-i)):
        print('yes')
        break
else:
    print("no")

op:12    11
   yes   no  '''



'''
a = "polikujmnhytgbvfredcxswqaz"
b = "abbcdd"
c= {}
for i in range(len(a)):
    c[a[i]] = i
s= ''.join(sorted(b,key =c.get))
print(s)'''

'''
alp='polikujmnhytgbvfredcxswqaz'
b=''
s='abbcdd'
for i in range(len(alp)):
    for j in range(len(s)):
        if alp[i]==s[j]:
            b += alp[i]
print(b)'''

''' code vita question



n=int(input())
while(n):
    a=input()
    c=input()
    s=''
    for i in a:
        if(i in c):
            s=s+(i*c.count(i))
    print(s)
    n=n-1
    
    
op:2
qwertyuiopasdfghjklzxcvbnm
abbcdde
eaddcbb
poiuytrewqlkjhgfdamnbvcxz
ghu
uhg


1
dfgh
kjhg
gh'''

'''
l = [13, 9, 4, 10, 5, 7]
n = len(l)
if n == 0:
    value = 0
elif n == 1:
    value = l[0]

else:
    dp = [0] * n
    dp[0] = l[0]
    dp[1] = max(l[0],l[1])
    for i in range(2, n):
        dp[i] = max(l[i] + dp[i-2], dp[i-1])
    value = dp[n-1]
print(value)
'''


'''
          l=[13,9,4,10,5,7]
          /               \
 30  13+[4,10,5,7]      9+[10,5,7]
       /        \           /     \
     4+[5,7]   10+[7] 17 10+[7]   5+[]
    /   \      /    \     /    \
   5+[] 7+[]  7+[]  []  7+[]  []
 '''

'''def fun(l):
    if(len(l)==0):
        return 0
    if(len(l)==1):

return l[0]
    if(len(l)==2):
        return max(l)
    le=l[0]+fun(l[2:]) #30
    ri=l[1]+fun(l[3:]) #26
    return max(le,ri)
l=[13,9,4,10,5,7]
print(fun(l))
'''


'''[5,9,8,2,1,4]


def fun(root):
    if(root==None):
        root=node(x)
    elif(x<root.data):
        fun(root.left)
    else:
        fun(root.right)'''