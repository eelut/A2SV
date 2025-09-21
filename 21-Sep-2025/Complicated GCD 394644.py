# Problem: Complicated GCD - https://codeforces.com/contest/664/problem/A

import sys

tokens = sys.stdin.read().strip().split()
if not tokens:
    sys.exit(0)

a_raw, b_raw = tokens[0], tokens[1]

a = a_raw.lstrip('0') or '0'
b = b_raw.lstrip('0') or '0'

if a == b:
    print(a)
else:
    print(1)
