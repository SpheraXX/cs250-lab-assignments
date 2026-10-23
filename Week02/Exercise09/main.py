import math

n, vb, vs = map(int, input().split())
stoplists = list(map(int, input().split()))
xu, yu = map(int, input().split())

idx = 1
maxcheck = int(1e18)
mindist = int(1e18)
counter = -1

for val in stoplists:
    dist = math.sqrt((xu - val)**2 + yu**2)
    timecheck = val/vb + dist/vs
    counter += 1
    if counter == 0:
        continue
    if timecheck < maxcheck - 1e-9 or (abs(timecheck - maxcheck) < 1e-9 and dist < mindist):
        maxcheck = timecheck
        mindist = dist
        idx = counter+1

print(idx)