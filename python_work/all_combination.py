import itertools
input_lines = input().split()
result = 0
for i in itertools.permutations(input_lines):
    print(i)
    