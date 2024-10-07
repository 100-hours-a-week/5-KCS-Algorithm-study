# 1. HH:MM:SS 형식을 초 단위로 변환하는 함수
def time_to_seconds(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds

# 2. 초 단위를 HH:MM:SS 형식으로 변환하는 함수
def seconds_to_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"

# 3. HH:MM:SS 문자열에서 숫자의 종류를 계산하는 함수
def count_unique_digits(time_str):
    digits = set(time_str.replace(':', ''))  # 콜론 제외하고 숫자만 추출
    return len(digits)

def solution(a, b):
    for i in range(time_to_seconds(a), time_to_seconds(b)):
        count_unique_digits(seconds_to_time(i))