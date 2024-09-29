D, N = map(int, input().split())
diameter = list(map(int, input().split()))
pizza = list(map(int, input().split()))

# 오븐 지름을 위에서부터 아래로 축소
for i in range(1, D):
    diameter[i] = min(diameter[i], diameter[i - 1])

location = D - 1  # 오븐의 가장 아래부터 피자를 넣을 수 있는지 확인

for p in pizza:
    # 피자를 넣을 수 없다면
    while location >= 0 and diameter[location] < p:
        location -= 1  # 위로 올라가면서 확인
    
    if location < 0:  # 만약 피자가 모두 오븐에 들어가지 못한다면
        print(0)
        exit()

    location -= 1  # 피자를 넣었으므로 한 칸 위로 올라감

print(location + 2)
