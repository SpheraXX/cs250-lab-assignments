n = int(input())
names = []
scores = []
score = {}

for i in range(n):
    name, s = input().split()
    s = int(s)
    names.append(name)
    scores.append(s)
    if name in score:
        score[name] += s
    else:
        score[name] = s

m = max(score.values())
winners = set()
for name in score:
    if score[name] == m:
        winners.add(name)

cur = {}
for i in range(n):
    name = names[i]
    if name in cur:
        cur[name] += scores[i]
    else:
        cur[name] = scores[i]
    if name in winners and cur[name] >= m:
        print(name)
        break
