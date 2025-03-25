# Problem: Helpful Maths - https://codeforces.com/problemset/problem/339/A

s=input()
s_without_plus=s.replace("+","")
s_int = list(map(int, s_without_plus))
s_int.sort()
s_str=[str(i) for i in s_int]
s_complete="+".join(s_str)
print(s_complete)
