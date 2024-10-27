#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findMinWeight' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY weights
#  2. INTEGER d
#
import heapq


def findMinWeight(weights, d):
    # 1. 최대 힙 구성 (heapq는 최소 힙이므로, 음수로 변환)
    max_heap = [-w for w in weights]
    heapq.heapify(max_heap)

    # 2. d일 동안 반복하여 가장 무거운 초콜릿을 절반으로 줄임
    for day in range(d):
        if not max_heap:
            break  # 더 이상 줄일 초콜릿이 없음

        # 가장 무거운 초콜릿 꺼내기
        current = -heapq.heappop(max_heap)

        # 절반으로 줄인 무게 계산 (floor(weight / 2)만큼 먹음)
        eaten = current // 2
        remaining = current - eaten  # 남은 무게는 weight - floor(weight / 2)

        # 남은 무게가 0보다 크면 다시 힙에 삽입
        if remaining > 0:
            heapq.heappush(max_heap, -remaining)

    # 3. 남은 초콜릿의 총 무게 계산
    total_weight = -sum(max_heap)

    return total_weight


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    weights_count = int(input().strip())
    weights = []
    for _ in range(weights_count):
        weights_item = int(input().strip())
        weights.append(weights_item)
    d = int(input().strip())
    result = findMinWeight(weights, d)

    fptr.write(str(result) + '\n')

    fptr.close()
