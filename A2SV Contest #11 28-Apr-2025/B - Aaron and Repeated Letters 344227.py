# Problem: B - Aaron and Repeated Letters - https://codeforces.com/gym/605795/problem/B

s=input()
result = []
for char in s:
    if not result or char != result[-1]:
        result.append(char)
    else:
        result.pop()
print("".join(result)) 