import numpy as np

from common.tools import read_input

inp = read_input()
test_inp = read_input('task_sample_1.txt')
lines = inp.split('\n')


def predict_value(values):
    """
    :type values: list[int]
    :rtype: int
    """
    diff = np.diff(values)
    levels = [values, diff]
    while not np.all(diff == 0):
        diff = np.diff(diff)
        levels.append(diff)
    rev_levels = list(reversed(levels))
    predicted = 0
    for i, lev in enumerate(rev_levels[1:]):
        predicted = lev[0] - predicted
    return predicted


predicted_values = []
for line in lines:
    values = [int(v.strip()) for v in line.split(' ')]
    predicted = predict_value(values)
    predicted_values.append(predicted)

print(sum(predicted_values))
