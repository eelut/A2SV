# Problem: D - Electric Mayhem - https://codeforces.com/gym/605795/problem/D

s=input()
stack=[]
for i in range(len(s)):
    if stack and stack[-1]==s[i]:
        stack.pop()
    else:
        stack.append(s[i])
print("Yes"if len(stack)==0 else "No")