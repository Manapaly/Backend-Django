import math
a = input()
b = len(a) - 1
ans = 0
for i in a[::-1]:
    ans += (ord(i)-48) * math.pow(2, b)
    b -= 1
print(ans)