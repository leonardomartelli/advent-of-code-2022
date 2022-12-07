DRAW = 'draw'
LOSE = 'lose'

rules = {'A': {DRAW: 'X', LOSE: 'Y'}, 'B': {
    DRAW: 'Y', LOSE: 'Z'}, 'C': {DRAW: 'Z', LOSE: 'X'}}

score_weight = {'X': 1, 'Y': 2, 'Z': 3}

puzzle_input_file = open('input.txt', 'r')

puzzle_input = puzzle_input_file.read()

plays = puzzle_input.split('\n')

total_score = 0

for play in plays:
    opponent, mine = play.split(' ')

    total_score += score_weight[mine]

    if rules[opponent][LOSE] is mine:
        total_score += 6
    elif rules[opponent][DRAW] is mine:
        total_score += 3

print(total_score)
