import itertools
while True:
    input_lines = input().split()
    if (input_lines[0] == 'exit'):
        break
    for i in itertools.permutations(input_lines):
        print(i)
