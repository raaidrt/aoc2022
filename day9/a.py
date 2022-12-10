DEBUG = True

lines = []

while True:
    try:
        line = input()
        lines.append(line)
    except EOFError:
        break

movements = [(direction, int(magnitude)) 
             for direction, magnitude in [line.split() for line in lines]]

NUMTAILS = 9
head = (0, 0)
tails = [(0, 0) for _ in range(NUMTAILS)]
visited = { tails[-1] }

def isAdjacent(head, tail):
    headR, headC = head
    tailR, tailC = tail
    return abs(headR - tailR) <= 1 and abs(headC - tailC) <= 1

translation = {
    "R" : (1, 0),
    "L" : (-1, 0),
    "U" : (0, -1),
    "D" : (0, 1)
}

def moveTail(head, tail):
    headR, headC = head
    tailR, tailC = tail

    drow = headR - tailR
    dcol = headC - tailC
    
    
    return \
        tailR + (0 if drow == 0 else (drow // abs(drow))),\
        tailC + (0 if dcol == 0 else (dcol // abs(dcol)))

maxRow, maxCol = 0, 0

sequence = []
for direction, magnitude in movements:
    drow, dcol = translation[direction]
    for i in range(magnitude):
        head = head[0] + drow, head[1] + dcol
    
        sequence.append({})
        if not isAdjacent(head, tails[0]):
            tails[0] = moveTail(head, tails[0])
            maxRow = max(maxRow, abs(tails[0][0]))
            maxCol = max(maxCol, abs(tails[0][1]))
        sequence[-1][1] = tails[0]
        
        for j in range(NUMTAILS - 1):
            if not isAdjacent(tails[j], tails[j + 1]):
                tails[j + 1] = moveTail(tails[j], tails[j + 1])
                maxRow = max(maxRow, abs(tails[j + 1][0]))
                maxCol = max(maxCol, abs(tails[j + 1][1]))
            sequence[-1][j + 2] = tails[j + 1]

        sequence[-1]['H'] = head
        
        visited.add(tails[-1])

if DEBUG:
    for i, d in enumerate(sequence):
        print(f"Round {i + 1}")
        grid = [['#' for _ in range(-maxCol + 1, maxCol)] for _ in range(-maxRow + 1, maxRow)]

        for k in sorted(r for r in list(d.keys()) if r != 'H'):
            row, col = d[k]
            grid[row][col] = str(k)
        row, col = d['H']
        grid[row][col] = 'H'

        for row in grid:
            print(''.join(row))

print(len(visited))
