# order of moves is rock, paper, scissors
elf_moves = ["A", "B", "C"]
your_moves = ["X", "Y", "Z"]


def round_score(elf, you):
    diff = elf_moves.index(elf) - your_moves.index(you)
    score = 0
    if diff == -1 or diff == 2:
        score = 6
    elif diff == 0:
        score = 3

    return score + your_moves.index(you) + 1


def pick_your_move(elf, outcome):
    if outcome == "X":  # lose
        if elf_moves.index(elf) == 0:
            return your_moves[-1]
        return your_moves[elf_moves.index(elf) - 1]
    elif outcome == "Z":  # win
        if elf_moves.index(elf) == len(elf_moves) - 1:
            return your_moves[0]
        return your_moves[elf_moves.index(elf) + 1]
    else:  # draw
        return your_moves[elf_moves.index(elf)]


with open("./day02/input.txt", "r") as f:
    lines = f.readlines()

total = 0
for item in lines:
    elf, you = item.strip().split(" ")
    total += round_score(elf, you)
print(total)

total = 0
for item in lines:
    elf, outcome = item.strip().split(" ")
    total += round_score(elf, pick_your_move(elf, outcome))
print(total)
