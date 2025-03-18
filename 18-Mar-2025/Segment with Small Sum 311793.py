# Problem: Segment with Small Sum - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/A

n,s=map(int,input().split())
a=list(map(int,input().split()))
max_length=0
left=0
current_sum=0
for right in range(n):
    current_sum += a[right]
    while current_sum >s and left <=right:
        current_sum -=a[left]
        left += 1
    max_length=max(max_length,right-left+1)
print(max_length)
