n = int(input())

def check(num):
    length = len(num)
    for i in range(1, length//2 + 1):
        if num[-i:] == num[-(i*2):-i]:
            return False
    else:
        return True

def recur(num):
    global n, res
    if len(num) == n:
        print(num)
        exit()
    for i in '123':
        if check(num + str(i)):
            recur(num + str(i))
    return

recur('1')