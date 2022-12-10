lines = []

while True:
    try:
        line = input()
        lines.append(line)
    except EOFError:
        break

def score(c):
    if c.islower():
        return ord(c) - ord('a') + 1
    else:
        return ord(c) - ord('A') + 1 + 26
"""
s = 0
for line in lines:
    n = len(line)
    first, second = line[ : (n // 2)], line[(n // 2) : ]
    both = set()
    for c in first:
        if c in second:
            both.add(c)
    for c in both:
        s += score(c)"""

s = 0
for i in range(0, len(lines), 3):
    for c in lines[i] + lines[i + 1] + lines[i + 2]:
        if c in lines[i] and c in lines[i + 1] and c in lines[i + 2]:
            s += score(c)
            break
        

print(s)