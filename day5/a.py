lines = []

while True:
    try:
        line = input()
        lines.append(line)
    except EOFError:
        break

stacks = []
stackRepr = []
modifs = []
found = False
for i, line in enumerate(lines):
    if not found:
        if line.strip()[0] != "[": 
            found = True
            continue
        crates = []
        i = -1
        while i < len(line):
            i += 1
            if line[i+1] == " ":
                crates.append(None)
            else:
                crates.append(line[i+1])
            i += 3
        stackRepr.append(crates)
    else:
        tokens = line.split()
        if len(tokens) == 0: 
            continue
        modifs.append((int(tokens[1]), int(tokens[3]), int(tokens[5])))
stacks = [[] for _ in range(len(stackRepr[0]))]
for s in stackRepr:
    for i, v in enumerate(s):
        if v != None:
            stacks[i].append(v)
for i, s in enumerate(stacks):
    stacks[i] = list(reversed(s))
print(stacks)
for i, (num, fr, to) in enumerate(modifs):
    interm = []
    for _ in range(num):
        interm.append(stacks[fr - 1].pop())
    for _ in range(num):
        stacks[to - 1].append(interm.pop())
    interm = []
result = ""
for s in stacks:
    result += s[-1]
print(f"Result = {result}")
    