# Problem: A - Stairway to Goodness - https://codeforces.com/gym/608569/problem/A

def max_good_array_length(l, r):
    low, high = 1, 44722  # sqrt(2e9)
    res = 1
    while low <= high:
        mid = (low + high) // 2
        total = l + (mid - 1) * mid // 2
        if total <= r:
            res = mid
            low = mid + 1
        else:
            high = mid - 1
    return res

t = int(input())
for _ in range(t):
    l, r = map(int, input().split())
    print(max_good_array_length(l, r))
