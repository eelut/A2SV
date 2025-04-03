# Problem: Sereja and Dima - https://codeforces.com/problemset/problem/381/A

n = int(input())  
cards = list(map(int, input().split()))  

sereja = 0  
dima = 0  
turn = 0  

while cards:  
    if cards[0] > cards[-1]:  
        chosen_card = cards.pop(0)  
    else:  
        chosen_card = cards.pop()  

    if turn % 2 == 0:  
        sereja += chosen_card  
    else:  
        dima += chosen_card  

    turn += 1  

print(sereja, dima)  
