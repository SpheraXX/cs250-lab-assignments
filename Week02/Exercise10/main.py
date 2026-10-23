n, k = map(int, input().split())
req = list(map(int, input().split()))

c = (k + 1) // 2
seat = []
for i in range(k + 1):
    seat.append([False] * (k + 1))
freecnt = [k] * (k + 1)
memo = []
for i in range(k + 1):
    memo.append({})

pre = [0] * (k + 1)
for y in range(1, k + 1):
    pre[y] = pre[y - 1] + abs(y - c)

rows = [c]
for d in range(1, c):
    rows.append(c - d)
    rows.append(c + d)

out = []
for m in req:
    l = c - m // 2
    mincost = pre[l + m - 1] - pre[l - 1]
    best = int(1e18)
    bx = -1
    by = -1
    for x in rows:
        if m * abs(x - c) + mincost > best:
            break
        if freecnt[x] < m:
            continue
        if m not in memo[x]:
            row = seat[x]
            rbest = int(1e18)
            ry = -1
            free = 0
            for y in range(1, k + 1):
                if row[y]:
                    free = 0
                else:
                    free += 1
                if free >= m:
                    yl = y - m + 1
                    cost = pre[y] - pre[yl - 1]
                    if cost < rbest:
                        rbest = cost
                        ry = yl
            memo[x][m] = (rbest, ry)
        rbest, ry = memo[x][m]
        if ry == -1:
            continue
        cost = rbest + m * abs(x - c)
        if cost < best or (cost == best and x < bx):
            best = cost
            bx = x
            by = ry
    if bx == -1:
        out.append("-1")
    else:
        for y in range(by, by + m):
            seat[bx][y] = True
        freecnt[bx] -= m
        memo[bx] = {}
        out.append(str(bx) + " " + str(by) + " " + str(by + m - 1))

print("\n".join(out))
