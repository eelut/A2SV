# Problem: D - Maxim’s Gift: Tangle of Letters - https://codeforces.com/gym/629689/problem/D

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    res = len(s)
    if n % 2 == 0:
        v = [[0] * 26 for _ in range(2)]
        for i in range(n):
            v[i % 2][ord(s[i]) - ord('a')] += 1
        for i in range(2):
            mx = max(v[i])
            res -= mx
        print(res)
    else:
        pref = [[0] * 26 for _ in range(2)]
        suf = [[0] * 26 for _ in range(2)]
        for i in range(n - 1, -1, -1):
            suf[i % 2][ord(s[i]) - ord('a')] += 1
        for i in range(n):
            suf[i % 2][ord(s[i]) - ord('a')] -= 1
            ans = n
            for k in range(2):
                mx = 0
                for j in range(26):
                    mx = max(mx, suf[1 - k][j] + pref[k][j])
                ans -= mx
            res = min(res, ans)
            pref[i % 2][ord(s[i]) - ord('a')] += 1
        print(res)