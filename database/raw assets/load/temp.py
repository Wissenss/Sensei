
lines = []

with open("cards.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    # print(line)
    splitline = tuple(line.split("-"))
    last = splitline[4].replace('\n', '')
    print(f"({int(splitline[0])}, '{splitline[1]}', '{splitline[2]}', {int(splitline[3])}, '{last}'),")