half_priority = ord('Z')

A_code = ord('A')
a_code = ord('a')


def get_priority(item_type):
    ascii_code = ord(item_type)

    if ascii_code > half_priority:
        return ascii_code - a_code + 1

    return ascii_code - A_code + 27


puzzle_input_file = open('input.txt', 'r')
puzzle_input = puzzle_input_file.read()

rucksacks = puzzle_input.split('\n')

badges_sum = 0

elf_groups = [[] for _ in range(len(rucksacks) // 3)]

for rucksack_index in range(len(rucksacks)):
    rucksack_as_set = set()

    rucksack = rucksacks[rucksack_index]

    for item_type in rucksack:
        rucksack_as_set.add(item_type)

    elf_groups[rucksack_index // 3].append(rucksack_as_set)

for group in elf_groups:
    badge = group[0].intersection(group[1]).intersection(group[2]).pop()

    badges_sum += get_priority(badge)

print(badges_sum)
