# Problem: Way Too Long Words - https://codeforces.com/problemset/problem/71/A

n = int(input())

a = [input().strip() for _ in range(n)]

for i in a:
    if len(i) <= 10:
        print(i)
    else:
        print(i[0]+str(len(i)-2)+i[-1])
