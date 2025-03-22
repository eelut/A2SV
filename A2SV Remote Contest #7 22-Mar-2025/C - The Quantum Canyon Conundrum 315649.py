# Problem: C - The Quantum Canyon Conundrum - https://codeforces.com/gym/596004/problem/C

import sys 
input = sys.stdin.readline 
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int, input().split()))
 
    if n==1:
        print("YES")
        continue
    c=0
    i=0
    while i<n:
        l=i
        while i<n and a[i]==a[l]:
            i+=1
        r=i-1
        g=True
        if l>0 and a[l-1] <=a[l]:
            g=False
        if r < n-1 and a[r] >= a[r+1]:
            g=False
        if g:
            c+=1
        if c>1:
            print("NO")
            break
    if c==1:
        print("YES")