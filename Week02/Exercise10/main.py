n, k = map(int, input().split())
req = list(map(int, input().split()))

c = (k + 1) // 2
seat = []
for i in range(k + 1):
    seat.append([False] * (k + 1))

pre = [0] * (k + 1)
for y in range(1, k + 1):
    pre[y] = pre[y - 1] + abs(y - c)

for m in req:
    best = int(1e18)
    bx = -1
    by = -1
    for x in range(1, k + 1):
        free = 0
        for y in range(1, k + 1):
            if seat[x][y]:
                free = 0
            else:
                free += 1
            if free >= m:
                yl = y - m + 1
                cost = pre[y] - pre[yl - 1] + m * abs(x - c)
                if cost < best:
                    best = cost
                    bx = x
                    by = yl
    if bx == -1:
        print(-1)
    else:
        for y in range(by, by + m):
            seat[bx][y] = True
        print(bx, by, by + m - 1)
