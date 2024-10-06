import sys
input = sys.stdin.readline

# n 크레인 개수
n = int(input())

# 크레인의 무게 제한
limit_weight = list(map(int, input().split()))


# 박스의 수
m = int(input())

# 박스의 무게
box_weight = list(map(int, input().split()))

# 가장 큰 중량 제한 크레인 < 최고 박스의 무게 -1 출력

limit_weight.sort(reverse=True)
box_weight.sort(reverse=True)
cnt = 0

if limit_weight[0] < box_weight[0]:
    print(-1)

else:
    while box_weight: # 모든 박스의 값이 -1이 되기 전까지 반복
        for i in range(n): # 크레인
            for j in range(len(box_weight)): # 박스
                if box_weight[j] != -1:
                    if limit_weight[i] >= box_weight[j]: # 크레인이 박스 할당
                        box_weight.remove(box_weight[j])
                        break
        cnt += 1

    print(cnt)