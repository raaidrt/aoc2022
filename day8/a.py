lines = []

while True:
    try:
        line = input()
        lines.append(line)
    except EOFError:
        break

heights = []
for line in lines:
    row = []
    for i in range(len(line)):
        row.append(int(line[i]))
    heights.append(row)

count = 0

scores = [[0 for j in range(len(heights[i]))] for i in range(len(heights))]

for i in range(len(heights)):
    for j in range(len(heights[i])):
        scenic_score = 1
        interm = 0
        for k in range(i - 1, -1, -1):
            if heights[k][j] >= heights[i][j]:
                interm += 1
                break
            interm += 1

        scenic_score *= interm
        interm = 0
        for k in range(i + 1, len(heights)):
            if heights[k][j] >= heights[i][j]:
                interm += 1
                break
            interm += 1

        scenic_score *= interm
        interm = 0
        for k in range(j - 1, -1, -1):
            if heights[i][k] >= heights[i][j]:
                interm += 1
                break
            interm += 1

        scenic_score *= interm
        interm = 0

        for k in range(j + 1, len(heights[i])):
            if heights[i][k] >= heights[i][j]:
                interm += 1
                break
            interm += 1
        scenic_score *= interm
        scores[i][j] = scenic_score

print(max(max(row) for row in scores))
