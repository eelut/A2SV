# Problem: Petya and Strings - https://codeforces.com/problemset/problem/112/A

first_string=input().lower()
second_string=input().lower()

if first_string == second_string:
    print(0)
elif first_string < second_string:
    print(-1)
elif first_string > second_string:
    print(1)
