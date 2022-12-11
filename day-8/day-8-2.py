
puzzle_input_file = open('input.txt', 'r')

puzzle_input = puzzle_input_file.read()

horizontal_trees = puzzle_input.split('\n')

forest = [[int(tree) for tree in tree_row] for tree_row in horizontal_trees]


def check_left_visibility(row_index, tree_index, tree):
    visibility = 0

    for index in range(tree_index - 1, -1, -1):
        visibility += 1

        if forest[row_index][index] >= tree:
            break

    return visibility


def check_right_visibility(row_index, tree_index, tree):
    visibility = 0

    for index in range(tree_index + 1, len(forest)):
        visibility += 1

        if forest[row_index][index] >= tree:
            break

    return visibility


def check_top_visibility(row_index, tree_index, tree):
    visibility = 0

    for index in range(row_index - 1, -1, -1):
        visibility += 1

        if forest[index][tree_index] >= tree:
            break

    return visibility


def check_bottom_visibility(row_index, tree_index, tree):
    visibility = 0

    for index in range(row_index + 1, len(forest)):
        visibility += 1

        if forest[index][tree_index] >= tree:
            break

    return visibility


highest_visibility = 0

for row_index in range(len(forest)):
    for tree_index in range(len(forest)):
        tree = forest[row_index][tree_index]

        left_visibility = check_left_visibility(row_index, tree_index, tree)

        right_visibility = check_right_visibility(row_index, tree_index, tree)

        top_visibility = check_top_visibility(row_index, tree_index, tree)

        bottom_visibility = check_bottom_visibility(
            row_index, tree_index, tree)

        visibility = left_visibility * right_visibility * \
            top_visibility * bottom_visibility

        if visibility > highest_visibility:
            print(left_visibility, right_visibility,
                  top_visibility, bottom_visibility)
            highest_visibility = visibility


print(highest_visibility)
