import sys
from collections import deque

def find_total_score(score, guilder_count, k):
    total_score = 0

    for _ in range(guilder_count):
        front = score[:k]
        back = score[-k:]

        max_front = max(front)
        max_back = max(back)

        if max_front >= max_back:
            idx = front.index(max_front)
        else:
            # 뒤쪽에서 선택 (같은 값이면 인덱스가 낮은 값 선택)
            idx = len(score) - k + back.index(max_back)

        total_score += score[idx]
        score.pop(idx)

    return total_score

score = [-10, -5, -30, -1, -20]
guilder_count = 2
k = 3

print(find_total_score(score, guilder_count, k))