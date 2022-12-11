
puzzle_input_file = open('input.txt', 'r')

puzzle_input = puzzle_input_file.read()

horizontal_trees = puzzle_input.split('\n')

forest = [[int(tree) for tree in tree_row] for tree_row in horizontal_trees]


def check_left_visibility(row_index, tree_index, tree):
    for index in range(tree_index):
        if forest[row_index][index] >= tree:
            return False

    return True


def check_right_visibility(row_index, tree_index, tree):
    for index in range(len(forest) - 1, tree_index, -1):
        if forest[row_index][index] >= tree:
            return False

    return True


def check_top_visibility(row_index, tree_index, tree):
    for index in range(row_index):
        if forest[index][tree_index] >= tree:
            return False

    return True


def check_bottom_visibility(row_index, tree_index, tree):
    for index in range(len(forest) - 1, row_index, -1):
        if forest[index][tree_index] >= tree:
            return False

    return True


visible_trees_count = 0

for row_index in range(len(forest)):
    for tree_index in range(len(forest)):
        tree = forest[row_index][tree_index]

        if check_left_visibility(row_index, tree_index, tree) or check_right_visibility(row_index, tree_index, tree) or check_top_visibility(row_index, tree_index, tree) or check_bottom_visibility(row_index, tree_index, tree):
            visible_trees_count += 1


print(visible_trees_count)
