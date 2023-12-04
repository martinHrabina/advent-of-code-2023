import re
from collections import defaultdict

from common.tools import read_input

inp = read_input()
test_inp = read_input('task_sample.txt')

parts = {'-', '+', '@', '*', '$', '#', '%', '&', '=', '/'}

lines = inp.split('\n')
# gather part indices
part_indices = defaultdict(list)
possible_gear_indices = defaultdict(list)

for i, line in enumerate(lines):
    indices = [i.start() for i in re.finditer('[' + '|'.join(parts) + ']', line)]
    g_indices = [i.start() for i in re.finditer('\*', line)]
    possible_gear_indices[i].extend(g_indices)
    part_indices[i-1].extend(indices)
    part_indices[i].extend(indices)
    part_indices[i+1].extend(indices)

part_numbers = []
gears = defaultdict(list)
# find out if number is a part number
for i, line in enumerate(lines):
    line_numbers = [(int(i.start()), int(i.end())-1, int(i.group(0))) for i in re.finditer('\d+', line)]
    for num in line_numbers:
        is_part_number = any([(num[0]-1 <= r_i <= num[1]+1) for r_i in part_indices[i]])
        if is_part_number:
            part_numbers.append(num[2])
        for g_i in range(i-1, i+2):
            for r_i in possible_gear_indices[g_i]:
                if num[0]-1 <= r_i <= num[1]+1:
                    gears[(g_i, r_i)].append(num[2])

print(sum(part_numbers))

gear_nums = []
for gear, nums in gears.items():
    if len(nums) == 2:
        gear_nums.append(nums[0] * nums[1])

print(sum(gear_nums))
