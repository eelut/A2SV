# Problem: Books - https://codeforces.com/contest/279/problem/B

n,t=map(int,input().split())
a=list(map(int,input().split()))

l=0
total=0
count=0

for r in range (n):
    total+=a[r]
    while total>t:
        total-=a[l]
        l+=1
    count=max(count,r-l+1)
print (count)
