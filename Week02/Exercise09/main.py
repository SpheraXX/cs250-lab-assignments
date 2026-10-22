import math

n, vb, vs = map(int, input().split())
stoplists = list(map(int, input().split()))
xu, yu = map(int, input().split())

idx = 1
maxcheck = int(1e18)
counter = -1

for val in stoplists:
    timecheck = val/vb + math.sqrt((xu - val)**2 + yu**2)/vs
    counter += 1
    if counter != 0 and timecheck < maxcheck:
        maxcheck = timecheck
        idx = counter+1

print(idx)