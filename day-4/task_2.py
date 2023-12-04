from common.tools import read_input

inp = read_input()
test_inp = read_input('task_sample.txt')

lines = inp.split('\n')
card_counts = {k: 1 for k in range(1, len(lines) + 1)}
for i, line in enumerate(lines):
    card_index = i+1
    numbers = line.split(':')[1]
    winning_numbers = [r for r in filter(lambda x: x, numbers.split('|')[0].split(' '))]
    my_numbers = [r for r in filter(lambda x: x, numbers.split('|')[1].split(' '))]
    my_wins = len([m for m in my_numbers if m in winning_numbers])
    for j in range(1, my_wins+1):
        try:
            card_counts[card_index + j] += card_counts[card_index]
        except KeyError:
            pass

print(card_counts)
print(sum(card_counts.values()))
