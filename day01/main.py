with open("./day01/input.txt", "r") as f:
    lines = f.readlines()

calories = []
current = []

for line in lines:
    if line == "\n":
        calories.append(sum(current))
        current = []
    else:
        current.append(int(line.strip()))
calories.append(sum(current))

print(max(calories))

sort_cals = sorted(calories, reverse=True)
print(sum(sort_cals[:3]))