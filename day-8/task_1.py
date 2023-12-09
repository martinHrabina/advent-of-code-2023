from common.tools import read_input

inp = read_input()
test_inp = read_input('task_sample_2.txt')
lines = inp.split('\n')

instructions = lines[0]

cmap = {}
# read map
for i, line in enumerate(lines):
    if i < 2:
        continue
    position, coordinates = line.split('=')
    c1, c2 = coordinates.replace('(', '').replace(')', '').replace(' ','').split(',')
    cmap[position.strip()] = (c1, c2)

position = 'AAA'
step_counter = 0
while position != 'ZZZ':
    instruction_counter = step_counter % len(instructions)
    instruction = instructions[instruction_counter]
    step_counter += 1
    position = cmap[position][0 if instruction == 'L' else 1]

print(step_counter)
