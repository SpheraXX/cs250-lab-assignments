s = input()
t = input()

x1 = ord(s[0]) - ord('a')
y1 = int(s[1])
x2 = ord(t[0]) - ord('a')
y2 = int(t[1])

print(max(abs(x1 - x2), abs(y1 - y2)))

check = False
while not check:
    move = ""
    check = True
    if x1 < x2:
        move += "R"
        x1 += 1
        check = False
    elif x1 > x2:
        move += "L"
        x1 -= 1
        check = False
    if y1 < y2:
        move += "U"
        y1 += 1
        check = False
    elif y1 > y2:
        move += "D"
        y1 -= 1
        check = False
    if move != "":
        print(move)
