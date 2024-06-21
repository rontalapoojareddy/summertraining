'''class Solution:
    def trap(self, height):
        if not height: 
            return 0
        l=0
        r=len(height)-1
        maxl=height[l]
        maxr=height[r]
        res=0
        while l<r:
            if maxl<maxr:
                l+=1
                maxl=max(maxl,height[l])
                res+=(maxl-height[l])
            else:
                r-=1
                maxr=max(maxr,height[r])
                res+=(maxr-height[r])
        print("trapped water =",res)
height = Solution()
height.trap([2,5,2,3,6,7,1,0,5,7])
height.trap([4,3,4,5,6,1,0,6,7])
height.trap([9,4,5,6,2,4])'''


'''arr=[2,5,2,3,6,7,1,0,5,7]
l=[0]*len(arr)
r=[0]*len(arr)
m=0
for i in range(len(arr)):
    if(arr[i]>m):
        m=arr[i]
    l[i]=m
m1=0

for i in range(len(arr)-1,-1,-1):
    if(arr[i]>m1):
        m1=arr[i]
    r[i]=m1
s=0
for i in range(len(arr)):
    s=s+abs(min(l[i],r[i])-arr[i])
print(s)'''

'''
l=[1,3,4,5],n=17

  0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17       
3 0 1 2 1 2 3 2 3 4 3 4  5  4  5  6  5  6  7
4 0 1 2 1 1 2 2 2 2 3 3  3  3  4  4  4  4  5
5 0 1 2 1 1 1 2 2 2 2 2  3  3  3  3  3  4 *4* as ans 4'''

'''l=[3,4],n=5

  0 1 2 3 4 5
3 0 1 2 1 2 3
4 0 1 2 3 1 '2'  as ans 2 its wrong ans is -1

l=[3,4,5],n=7
  0 1 2 3 4 5 6 7
3 0 1 2 1 2 3 2 3
4 0 1 2 1 1 2 2 2
5 0 1 2 1 1 1 2 2   as ans '2'


'''

'''def fun():
    l1=[-1]*(n+1)
    l1[0]=0
    for i in l:
        for j in range(1,n+1):
            if (j>=i):
                if (l1[j-i]!=-1):
                    if(l1[j]!=-1):
                        l1[j]=min(l1[j],l1[j-i]+1)
                    else:
                        l1[j]=l1[j-i]+1
    print(l1[-1])
l=[3,4]
#l=[1,3,4,5]
#n=17 #op:4
n=5
fun()'''


'''ip=4*3
op:
 ----
 ----
 ----'''

'''def op():
    for i in range(m):
        for j in range(n):
            print('-',end=' ')
        print()
n=4
m=3
op()'''

'''def fun(i,j,c):
    if(i<0 or i>=n or j<0 or j>=m or (i==k and j==l)):
        return c
    if(i==n-1 and j==m-1):
        c=c+1
        return c
    vi.append((i,j))
    if((i-1,j) not in vi):
        c=fun(i-1,j,c)
    if((i,j-1) not in vi):
        c=fun(i,j-1,c)
    if((i+1,j) not in vi):
        c=fun(i+1,j,c)
    if((i,j+1) not in vi):
        c=fun(i,j+1,c)
    vi.pop()
    return c
m=4
n=3
vi=[]
k=1
l=1
r=fun(0,0,0)
print(r)'''



