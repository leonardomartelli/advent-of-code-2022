puzzle_input_file = open('input.txt', 'r')
puzzle_input = puzzle_input_file.read()

assignments = puzzle_input.split('\n')

self_contained_count = 0

for assignment in assignments:
    elf_one, elf_two = assignment.split(',')

    elf_one_start, elf_one_end = elf_one.split('-')
    elf_two_start, elf_two_end = elf_two.split('-')

    elf_one_start, elf_one_end = int(elf_one_start), int(elf_one_end)
    elf_two_start, elf_two_end = int(elf_two_start), int(elf_two_end)

    if (elf_one_start >= elf_two_start and elf_one_end <= elf_two_end) or (elf_one_start <= elf_two_start and elf_one_end >= elf_two_end):
        self_contained_count += 1

print(self_contained_count)
