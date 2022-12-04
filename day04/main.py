with open("./day04/input.txt", "r") as f:
    data = [line.strip().split(",") for line in f.readlines()]

total = 0
for section_pair in data:
    section_1_start, section_1_end = [
        int(x) for x in section_pair[0].split("-")]
    section_2_start, section_2_end = [
        int(x) for x in section_pair[1].split("-")]

    if section_1_start > section_2_start:
        section_1_start, section_1_end = [
            int(x) for x in section_pair[1].split("-")]
        section_2_start, section_2_end = [
            int(x) for x in section_pair[0].split("-")]

    if section_1_start <= section_2_start and section_1_end >= section_2_end:
        total += 1
    elif section_1_start == section_2_start:
        total += 1
print(total)

total = 0
for section_pair in data:
    section_1_start, section_1_end = [
        int(x) for x in section_pair[0].split("-")]
    section_2_start, section_2_end = [
        int(x) for x in section_pair[1].split("-")]

    if section_1_start > section_2_start:
        section_1_start, section_1_end = [
            int(x) for x in section_pair[1].split("-")]
        section_2_start, section_2_end = [
            int(x) for x in section_pair[0].split("-")]

    if section_1_end < section_2_start:
        total += 1
print(len(data) - total)
