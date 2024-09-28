a = input()

arr = []
numarr = []
che = {}
che["H"] = 1
che["C"] = 12
che["O"] = 16

temp = 0

for el in a:
    if el == "(":
      arr.append(el)
    elif el == "H" or el == "C" or el == "O":
      arr.append(che[el])
    elif el == ")":
      temp = 0
      while True:
        if arr[-1] == '(':
            arr.pop()
            arr.append(temp)
            break
        else:
            temp += arr.pop()
    else:
        arr.append(arr.pop() * int(el))
        
print(sum(arr))