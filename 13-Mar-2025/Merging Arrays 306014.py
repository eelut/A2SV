# Problem: Merging Arrays - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

n,m=map(int,input().split(" "))
a=list(map(int,input().split(" ")))
b=list(map(int,input().split(" ")))

ans=[]
i ,j =0,0
while i<len(a) and j<len(b):
    if a[i]<b[j]:
        ans.append(a[i])
        i +=1
    else:
        ans.append(b[j])
        j +=1
ans.extend(a[i:])
ans.extend(b[j:]) 
print (*ans)

 
