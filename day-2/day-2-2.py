LOSE = 'X'
DRAW = 'Y'
WIN = 'Z'

ROCK = 'X'
PAPER = 'Y'
SCISSORS = 'Z'

OPPONENT_ROCK = 'A'
OPPONENT_PAPER = 'B'
OPPONENT_SCISSORS = 'C'

decision = {OPPONENT_ROCK: {WIN: PAPER, DRAW: ROCK, LOSE: SCISSORS},
            OPPONENT_PAPER: {WIN: SCISSORS, DRAW: PAPER, LOSE: ROCK},
            OPPONENT_SCISSORS: {WIN: ROCK, DRAW: SCISSORS, LOSE: PAPER}}

choice_score_weight = {ROCK: 1, PAPER: 2, SCISSORS: 3}
result_score_weight = {WIN: 6, LOSE: 0, DRAW: 3}

puzzle_input_file = open('input.txt', 'r')

puzzle_input = puzzle_input_file.read()

plays = puzzle_input.split('\n')

total_score = 0

for play in plays:
    opponent, mine = play.split(' ')

    choice = decision[opponent][mine]

    total_score += choice_score_weight[choice]

    total_score += result_score_weight[mine]

print(total_score)
