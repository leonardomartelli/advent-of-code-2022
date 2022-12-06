puzzle_input_file = open('input.txt', 'r')

puzzle_input = puzzle_input_file.read()

accumulator = ''

start_of_message = 0

marker_size = 14

for entry in puzzle_input:
    if entry in accumulator:
        accumulator = accumulator[accumulator.find(entry) + 1:]

    accumulator += entry

    start_of_message += 1

    if len(accumulator) == marker_size:
        break


print(start_of_message)
