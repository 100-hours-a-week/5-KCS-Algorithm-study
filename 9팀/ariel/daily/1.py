import sys
input = sys.stdin.readline

n = int(input())

def count_trailing_zeros(n):
    count = 0
    i = 5
    while n >= i:
        count += n // i
        i *= 5
    return count

print(count_trailing_zeros(n))