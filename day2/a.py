lines = []

while True:
    try:
        line = input()
        lines.append(line)
    except EOFError:
        break

winscore = {
    "A" : 2,
    "B" : 3,
    "C" : 1
}

drawscore = {
    "A" : 1,
    "B" : 2, 
    "C" : 3
}

losescore = {
    "A" : 3, 
    "B" : 1,
    "C" : 2
}

s = 0
for line in lines:
    if line[2] == "X":
        s += 0
        s += losescore[line[0]]
    elif line[2] == "Y":
        s += 3
        s += drawscore[line[0]]
    else:
        s += 6
        s += winscore[line[0]]
print(s)
