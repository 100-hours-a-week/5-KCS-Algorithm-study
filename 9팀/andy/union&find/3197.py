r, c = map(int, input().split())

board = [list(input()) for _ in range(r)]
root = [[(i, j) for j in range(c)] for i in range(r)]
rank = [[0 for _ in range(c)] for _ in range(r)]
visit = [[0 for _ in range(c)] for _ in range(r)]
swan = []

for i in range(r):
    for j in range(c):
        if board[i][j] == "L":
            swan.append((i, j))
            board[i][j] = "."
            if len(swan) == 2:
                break