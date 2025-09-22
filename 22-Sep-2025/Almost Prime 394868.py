# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

def solve():
    n = int(input())
    
    prime_factors_count = [0] * (n + 1)
    
    for i in range(2, n + 1):
        if prime_factors_count[i] == 0:  
            for j in range(i, n + 1, i):
                prime_factors_count[j] += 1
    
    result = sum(1 for x in prime_factors_count if x == 2)
    
    print(result)


if __name__ == "__main__":
    solve()
