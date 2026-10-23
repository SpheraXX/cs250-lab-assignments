people = 0
traffic = 0

while True:
    try:
        line = input()
    except EOFError:
        break
    if line == "":
        continue
    if line[0] == '+':
        people += 1
    elif line[0] == '-':
        people -= 1
    else:
        msg = line[line.index(':') + 1:]
        traffic += len(msg) * people

print(traffic)
