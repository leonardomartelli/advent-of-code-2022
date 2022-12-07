
puzzle_input_file = open('input.txt', 'r')

puzzle_input = puzzle_input_file.read()

elves_buffer = puzzle_input.split('\n\n')

ranking = []

for buffer in elves_buffer:
    snacks = buffer.split('\n')

    kcal = 0

    for snack in snacks:
        kcal += int(snack)

    ranking.append(kcal)


ranking.sort()

print(ranking[-3] + ranking[-2] + ranking[-1])
