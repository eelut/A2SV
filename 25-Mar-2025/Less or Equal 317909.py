# Problem: Less or Equal - https://codeforces.com/problemset/problem/977/C

n,k=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()

if k==0:
    print(arr[0] -1 if arr[0] >1 else -1)
elif k==n:
    print(arr[-1])
elif k<n and arr[k-1] !=arr[k]:
    print(arr[k-1])
else:
    print(-1)