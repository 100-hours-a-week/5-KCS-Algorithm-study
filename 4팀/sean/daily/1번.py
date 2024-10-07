from collections import deque


def in_range(nx, ny, n):
    return 0 <= nx < n and 0 <= ny < n


def find_chicken_breast(store_map, entrance_point):
    n = len(store_map)  # 행과 열의 크기 (n x n)

    directions = [
        [(0, 1), (0, -1)],
        [(-1, 0), (1, 0)]
    ]

    q = deque([(entrance_point[0], entrance_point[1], 0)])

    visited = [[[False, False] for _ in range(n)] for _ in range(n)]
    visited[entrance_point[0]][entrance_point[1]][0] = True
    while q:
        x, y, direction = q.popleft()

        # 현재 위치가 닭가슴살이면 True 반환
        if store_map[x][y] == 7:
            return True

        # 현재 위치가 이동 불가능한 경우 넘어감
        if store_map[x][y] == 0 or store_map[x][y] == 8:
            continue

        # 좌우, 상하 번갈아가며 이동
        for dx, dy in directions[direction]:
            nx = x + dx * store_map[x][y]
            ny = y + dy * store_map[x][y]

            # 지도 범위 내에서 이동
            if in_range(nx, ny, n) and store_map[nx][ny] != 0 and store_map[nx][ny] != 8 and not visited[nx][ny][
                1 - direction]:
                visited[nx][ny][1 - direction] = True  # 다음 방향으로 전환
                q.append((nx, ny, 1 - direction))

    # 큐가 다 비었음에도 닭가슴살을 못찾으면 False 반환
    return False

ConvenienceStoreMap = [
    [1, 2, 1],
    [8, 2, 0],
    [1, 7, 2]
]

entrancePoint = [0, 0]

print(find_chicken_breast(ConvenienceStoreMap, entrancePoint))