# Problem: D - The Snap of Fury - https://codeforces.com/gym/596004/problem/D

n=int(input())
w=list(map(int,input().split()))
survivors=[True] * n
destroy_range=0
for right in range(n-1,-1,-1):
    if destroy_range >0:
        survivors[right]=False
        destroy_range -=1
    destroy_range=max(destroy_range,w[right])

print(survivors.count(True))   
 