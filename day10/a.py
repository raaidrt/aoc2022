from binary_search import *

DEBUG = False

lines = []

while True:
    try:
        line = input()
        lines.append(line)
    except EOFError:
        break

START = 20
STEP = 40

cycle = 1
X = 1
values = []
for line in lines:
    if line == "noop":
        cycle += 1
    else:
        _, V = line.split()
        V = int(V)
        X += V
        cycle += 2
        values.append((cycle, X))

result = 0

def getSpritePos(c : int) -> int:
    def find(i):
        cyc, xValue = values[i]
        return cyc >= c
    idx = binsearch(find, 0, len(values) - 1)
    if idx == None: return None
    cyc, xValue = values[idx]
    if cyc > c:
        if idx == 0:
            return 1
        else:
            _, x = values[idx - 1]
            return x
    return xValue


for c in range(START, cycle + 1, STEP):
    def find(i):
        cyc, xValue = values[i]
        return cyc >= c
    idx = binsearch(find, 0, len(values) - 1)

    cyc, xValue = values[idx]
    if cyc > c:
        if idx == 0:
            res = c * 1
            if DEBUG:
                print(f"{c} * {1} = {res}")
            result += res
        else:
            _, x = values[idx - 1]
            res = c * x
            if DEBUG:
                print(f"{c} * {x} = {res}")
            result += res
    else:
        res = c * xValue
        if DEBUG:
            print(f"{c} * {xValue} = {res}")
        result += res

if DEBUG:
    for cyc, x in values:
        print(f"Cycle {cyc} has value {x}")

GRIDCOLS = 40
GRIDROWS = 6

grid = [['.' for _ in range(GRIDCOLS)] for _ in range(GRIDROWS)]

for row in range(GRIDROWS):
    for col in range(GRIDCOLS):
        c = row * GRIDCOLS + col + 1
        x = getSpritePos(c)
        if x == None: continue
        if abs(x - col) <= 1:
            grid[row][col] = '#'

for row in grid:
    print(''.join(row))
