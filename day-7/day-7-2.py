# run all the commands and populate the tree
# on the way back, sum up the file sizes + children
# set the size and comapre with the roof, if it is ok, set it as the highest on the tree with the ok size
import re

SIZE_LIMIT = 100_000

CD = 'cd'
LS = 'ls'
OUT = '..'

command_pattern = re.compile(r'\$ (ls|cd)(?: (\.\.|.+))?')
dir_pattern = re.compile(r'dir (\w+)')
file_pattern = re.compile(r'(\d+) (.*)')

FILE_SYSTEM_SIZE = 70_000_000
UPDATE_SIZE = 30_000_000


class File:
    def __init__(self, size, name):
        self.size = int(size)
        self.name = name


class Directory:
    def __init__(self, name):
        self.name = name
        self.directories = dict()
        self.files = dict()
        self.size = 0

    def calculate_size(self):

        for child in self.directories:
            self.size += child.size

        return self.size

    def add_directory(self, directory):
        # print(f'added {directory.name} to {self.name}')

        self.directories[directory.name] = directory

    def add_file(self, file):
        self.files[file.name] = file
        self.size += file.size

    def access(self, name):
        # print(f'accessing {name} from {self.name}')

        return self.directories[name]

    def get_better_directories_to_delete(self, size_needed, candidates):
        if self.size > size_needed:
            candidates.append(self.size)

        for directory in self.directories:
            self.directories[directory].get_better_directories_to_delete(
                size_needed, candidates)


root = Directory('/')

directory_stack = [root]

current_directory = root


def step_out():
    directory_stack.pop()
    return directory_stack[-1]


def step_into(current_directory, dir_name):
    current_directory = current_directory.access(dir_name)

    directory_stack.append(current_directory)

    return current_directory


puzzle_input_file = open('input.txt', 'r')

puzzle_input = puzzle_input_file.read()

console_output = puzzle_input.split('\n')

listing = False

for output in console_output[1:]:
    if listing:
        file_match = file_pattern.match(output)

        if file_match is not None:
            current_directory.add_file(
                File(file_match.group(1), file_match.group(2)))
            continue

        directory_match = dir_pattern.match(output)

        if directory_match is not None:
            current_directory.add_directory(
                Directory(directory_match.group(1)))
            continue

        listing = False

    command = command_pattern.match(output)

    if command.group(1) == CD:
        if command.group(2) == OUT:
            actual_size = current_directory.size
            current_directory = step_out()
            current_directory.size += actual_size
        else:
            current_directory = step_into(
                current_directory, command.group(2))
    else:
        listing = True

print(
    UPDATE_SIZE - (FILE_SYSTEM_SIZE - root.size))

candidates = []

root.get_better_directories_to_delete(
    UPDATE_SIZE - (FILE_SYSTEM_SIZE - root.size), candidates)

candidates.sort()

print(candidates[0])
