lines = []

while True:
    try:
        line = input()
        lines.append(line)
    except EOFError:
        break

def works(s):
    for i in range(len(s)):
        newS = s[:i] + s[i+1:]
        if s[i] in newS: return False
    return True

for line in lines:
    for pos in range(14, len(line)+1):
        arr = line[pos-14:pos]
        if works(arr):
            print(pos)
            break
