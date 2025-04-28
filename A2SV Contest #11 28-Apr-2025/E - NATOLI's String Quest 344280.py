# Problem: E - NATOLI's String Quest - https://codeforces.com/gym/605795/problem/E

s = input().strip()
n = len(s)

min_char = [''] * n
min_char[-1] = s[-1]
for i in range(n - 2, -1, -1):
    min_char[i] = min(s[i], min_char[i + 1])

t = []
u = []
i = 0

while i < n or t:
    if t and (i == n or t[-1] <= min_char[i]):
        u.append(t.pop())
    else:
        t.append(s[i])
        i += 1

print(''.join(u))
