from io import StringIO

with open("input.txt", "r") as f:
    f = StringIO(f.read())
    count, highest, second, third = 0, 0, 0, 0
    for x in f.readlines():
        if x == '\n':
            if count > highest:
                second = highest
                highest = count
            elif count > second:
                third = second
                second = count
            elif count > third:
                third = count
            count = 0
        else:
            count += int(x.split('\n')[0])
print(highest, second, third)
print(highest + second + third)