from string import ascii_letters

with open("./day03/ input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

# I'm not using this function, there is an easier way to get the priority of the items
def get_priority(item):
    if item.islower():
        return ord(item) - ord("a") + 1
    return ord(item) - ord("A") + 27

# Part One
total = 0
for line in lines:
    half = len(line) // 2
    left, right = line[:half], line[half:]
    common = set(left).intersection(set(right))
    total += ascii_letters.index(common.pop()) + 1
print(total)

# Part Two
total = 0
for x in range(0, len(lines) - 1, 3):
    group = lines[x:x+3]
    common = set(group[0]).intersection(group[1]).intersection(group[2])
    total += ascii_letters.index(common.pop()) + 1
print(total)
