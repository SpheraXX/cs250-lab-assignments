t, m = map(int, input().split())

ram = [0] * m
idx = 1

for _ in range(t):
    cmd = input().split()

    if cmd[0] == "alloc":
        n = int(cmd[1])
        pos = -1
        free = 0
        for i in range(m):
            if ram[i] == 0:
                free += 1
            else:
                free = 0
            if free == n:
                pos = i - n + 1
                break
        if pos == -1:
            print("NULL")
        else:
            for i in range(pos, pos + n):
                ram[i] = idx
            print(idx)
            idx += 1

    elif cmd[0] == "erase":
        x = int(cmd[1])
        if x <= 0 or x not in ram:
            print("ILLEGAL_ERASE_ARGUMENT")
        else:
            for i in range(m):
                if ram[i] == x:
                    ram[i] = 0

    else:
        newram = []
        for val in ram:
            if val != 0:
                newram.append(val)
        ram = newram + [0] * (m - len(newram))
