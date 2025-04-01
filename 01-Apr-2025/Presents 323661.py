# Problem: Presents - https://codeforces.com/problemset/problem/136/A

n=int(input())
p=list(map(int,input().split()))
res=[] 
for i in range (n):
    index=p.index(i+1)
    res.append(index +1)
print (" ".join((map(str,res))))