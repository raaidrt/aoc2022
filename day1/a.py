import sys

L = []
s = 0
for line in sys.stdin:
    if line != "":
        n = int(line)
        s += n
    else:
        L.append(s)
        s = 0
L.append(s)
L.sort()
print(L[-3:])
print(sum(L[-3:]))