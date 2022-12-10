lines = []

while True:
    try:
        line = input()
        lines.append(line)
    except EOFError:
        break
count = 0
for line in lines:
    first, second = line.split(',')
    a, b = first.split('-')
    a = int(a)
    b = int(b)
    c, d = second.split('-')
    c = int(c)
    d = int(d)
    if (a <= c and d <= b) or (c <= a and b <= d) or (a <= c and c <= b) or (
        c <= a and a <= d
    ):
        count += 1

print(count)