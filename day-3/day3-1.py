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

mistaken_sum = 0

for rucksack in rucksacks:
    rucksack_size = len(rucksack)

    first_compartment = set()
    second_compartment = set()

    raw_first_compartment = rucksack[:rucksack_size // 2]

    for item_type in raw_first_compartment:
        first_compartment.add(item_type)

    raw_second_compartment = rucksack[rucksack_size // 2:]

    for item_type in raw_second_compartment:
        second_compartment.add(item_type)

    mistaken_item_types = first_compartment.intersection(second_compartment)

    for mistaken in mistaken_item_types:
        priority = get_priority(mistaken)

        print(priority, mistaken_sum)

        mistaken_sum += priority

print(mistaken_sum)
