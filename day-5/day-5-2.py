import re


def pop_multiple(stack, quantity):
    crates = stack[-quantity:]

    return crates, stack[:-quantity]


def pop(stack):
    crate = stack[-1]
    return crate, stack[:-1]


def push(stack, crate):
    return stack + crate


move_pattern = re.compile(r'move (\d+) from (\d+) to (\d+)')

puzzle_input_file = open('input.txt', 'r')
puzzle_input = puzzle_input_file.read()


raw_crates_setup, raw_moves = puzzle_input.split('\n\n')

moves = raw_moves.split('\n')

stacks_count = (raw_crates_setup.find('\n') + 1) // 4

stack_line_pattern = re.compile(
    r'(?:(?:(?:\[(\w)\])|(?:\s{3}))\s?)' * stacks_count)

stack_lines = raw_crates_setup.split('\n')[:-1]

stack_lines.reverse()

stacks = ['' for _ in range(stacks_count)]

for line in stack_lines:
    matched = stack_line_pattern.match(line)

    for stack_number in range(stacks_count):
        crate = matched.groups()[stack_number]

        if crate is not None and crate != '':
            stacks[stack_number] += crate

# print(stacks)

for move in moves:

    print(stacks)
    matched = move_pattern.match(move)

    quantity, source_stack_index, destination_stack_index = int(
        matched.groups()[0]), int(matched.groups()[1]) - 1, int(matched.groups()[2]) - 1

    source_stack, destination_stack = stacks[source_stack_index], stacks[destination_stack_index]

    # if quantity >= 3 or len(source_stack) == quantity:
    crates, source_stack = pop_multiple(source_stack, quantity)
    destination_stack = push(destination_stack, crates)
    # else:
    #     for iteration in range(quantity):
    #         crate, source_stack = pop(source_stack)
    #         destination_stack = push(destination_stack, crate)

    stacks[source_stack_index], stacks[destination_stack_index] = source_stack, destination_stack


crates_on_top = ''

for stack in stacks:
    crates_on_top += stack[-1]


print(crates_on_top)
