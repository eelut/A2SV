# Problem: A - Modern Name Generator - https://codeforces.com/gym/605795/problem/A

t=int(input())
for _ in range(t):
    old_name=input()
    words=old_name.split()
    modern="".join(word[0]for word in words)
    print(modern)
                   
