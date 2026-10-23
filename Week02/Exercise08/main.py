s = input()

x = 0
y = 0
path = [(0, 0)]

for ch in s:
    if ch == 'L':
        x -= 1
    elif ch == 'R':
        x += 1
    elif ch == 'U':
        y += 1
    else:
        y -= 1
    path.append((x, y))

bug = False
for i in range(len(path)):
    for j in range(i + 1, len(path)):
        dist = abs(path[i][0] - path[j][0]) + abs(path[i][1] - path[j][1])
        if dist == 0 or (dist == 1 and j - i > 1):
            bug = True

if bug:
    print("BUG")
else:
    print("OK")
