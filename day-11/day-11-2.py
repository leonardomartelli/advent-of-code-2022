class Monkey:
    def __init__(self, raw):
        lines = raw.split('\n')[1:]

        self.items = [int(item)
                      for item in lines[0].split(':')[1].split(',')]

        self.operator = lines[1].split(':')[1].split()[3]
        self.second_operand = lines[1].split(':')[1].split()[4]

        self.condition = int(lines[2].split()[-1])
        self.first_option = int(lines[3].split()[-1])
        self.second_option = int(lines[4].split()[-1])

        self.inspections = 0

    def resolve_operation(self, old):
        second_operand = self.second_operand

        if second_operand == 'old':
            second_operand = old
        else:
            second_operand = int(second_operand)

        if self.operator == '+':
            return old + second_operand
        else:
            return old * second_operand

    def test(self, worriness):
        return worriness % self.condition == 0

    def inspect(self):
        for item in self.items:
            item = self.resolve_operation(item)

            item = item % 9699690

            # the key here is to do the math comparsion using modular arithmetic

            option = self.second_option

            if self.test(item):
                option = self.first_option

            self.inspections = self.inspections + 1

            yield (option, item)

        self.items.clear()

    def receive(self, item):
        self.items.append(item)

    def can_inspect(self):
        return len(self.items) > 0


puzzle_input_file = open('input.txt', 'r')

puzzle_input = puzzle_input_file.read()


monkeys = [Monkey(raw_monkey) for raw_monkey in puzzle_input.split('\n\n')]

rounds = 10000

for inspection_round in range(rounds):
    for monkey in monkeys:
        for to_monkey, item in monkey.inspect():
            monkeys[to_monkey].receive(item)


inspection_ranking = [monkey.inspections for monkey in monkeys]

inspection_ranking.sort()
print(inspection_ranking)

print(inspection_ranking[-2] * inspection_ranking[-1])
