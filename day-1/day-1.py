
puzzle_input_file = open('input.txt', 'r')

puzzle_input = puzzle_input_file.read()

elves_buffer = puzzle_input.split('\n\n')

highest = -1

for buffer in elves_buffer:
    snacks = buffer.split('\n')

    kcal = 0

    for snack in snacks:
        kcal += int(snack)

    if kcal > highest:
        highest = kcal


print(highest)
