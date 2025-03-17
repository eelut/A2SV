# Problem: B - The Time Heist’s Single-Shot Maneuver - https://codeforces.com/gym/596004/problem/B


t=int(input())
for _ in range (t):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b1=int(input())
    
    prev=float('-inf')
    possible=True

    for i in range(n):
        original=a[i]
        transformed=b1-a[i]

        if original >= prev and transformed >= prev:
            prev=min(original,transformed)
        elif original >= prev:
            prev=original
        elif transformed >= prev:
            prev=transformed
        else:
            possible=False
            break
    print("YES" if possible else "NO")    

