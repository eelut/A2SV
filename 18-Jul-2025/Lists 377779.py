# Problem: Lists - https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

if __name__ == '__main__':
    N = int(input())  # Number of commands
    lst = []          # Initialize empty list

    for _ in range(N):
        command = input().strip().split()
        cmd = command[0]

        if cmd == "insert":
            i, e = int(command[1]), int(command[2])
            lst.insert(i, e)
        elif cmd == "print":
            print(lst)
        elif cmd == "remove":
            e = int(command[1])
            lst.remove(e)
        elif cmd == "append":
            e = int(command[1])
            lst.append(e)
        elif cmd == "sort":
            lst.sort()
        elif cmd == "pop":
            lst.pop()
        elif cmd == "reverse":
            lst.reverse()
