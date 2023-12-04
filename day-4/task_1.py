from common.tools import read_input

inp = read_input()
test_inp = read_input('task_sample.txt')

lines = inp.split('\n')
card_scores = []
for i, line in enumerate(lines):
    numbers = line.split(':')[1]
    winning_numbers = [r for r in filter(lambda x: x, numbers.split('|')[0].split(' '))]
    my_numbers = [r for r in filter(lambda x: x, numbers.split('|')[1].split(' '))]
    my_wins = len([m for m in my_numbers if m in winning_numbers])
    score = my_wins if my_wins < 2 else 2**(my_wins-1)
    card_scores.append(score)

print(sum(card_scores))
