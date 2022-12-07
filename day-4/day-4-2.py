puzzle_input_file = open('input.txt', 'r')
puzzle_input = puzzle_input_file.read()

assignments = puzzle_input.split('\n')

overlapping_ranges = 0

for assignment in assignments:
    print(assignment)
    elf_one, elf_two = assignment.split(',')

    elf_one_start, elf_one_end = elf_one.split('-')
    elf_two_start, elf_two_end = elf_two.split('-')

    elf_one_start, elf_one_end = int(elf_one_start), int(elf_one_end)
    elf_two_start, elf_two_end = int(elf_two_start), int(elf_two_end)

    elf_one_range = set(range(elf_one_start, elf_one_end + 1))
    elf_two_range = set(range(elf_two_start, elf_two_end + 1))

    interception = elf_one_range.intersection(elf_two_range)
    print(elf_one_range, elf_two_range)

    if len(interception) > 0:
        print()
        print(interception)
        overlapping_ranges += 1

    else:
        print('x'*50)

print(overlapping_ranges)
