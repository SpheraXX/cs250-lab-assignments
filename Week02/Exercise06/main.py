n, m, c = input().split()
n = int(n)
m = int(m)

room = []
for i in range(n):
    room.append(input())

desks = {}
for i in range(n):
    for j in range(m):
        if room[i][j] != '.' and room[i][j] != c:
            desks[room[i][j]] = False

start = None
for i in range(n):
    for j in range(m):
        if room[i][j] == c and start == None:
            start = (i, j)

visited = set()
visited.add(start)
q = [start]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while len(q) > 0:
    x, y = q.pop()
    for k in range(4):
        u = x + dx[k]
        v = y + dy[k]
        if u < 0 or u >= n or v < 0 or v >= m:
            continue
        if room[u][v] == c and (u, v) not in visited:
            visited.add((u, v))
            q.append((u, v))
        elif room[u][v] != '.' and room[u][v] != c:
            desks[room[u][v]] = True

counter = 0
for key in desks:
    if desks[key]:
        counter += 1

print(counter)
