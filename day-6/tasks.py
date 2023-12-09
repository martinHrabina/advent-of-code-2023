from common.tools import read_input

inp = read_input()
test_inp = read_input('task_sample.txt')


def is_feasible(time, distance):
    feasible = 0
    for charging_time in range(time):
        # print((charging_time, time))
        speed = charging_time
        race_time = time - charging_time
        my_distance = speed * race_time
        if my_distance > distance:
            feasible += 1
    return feasible


lines = inp.split('\n')
times = [r for r in filter(lambda x: x, lines[0].split(':')[1].split(' '))]
distances = [r for r in filter(lambda x: x, lines[1].split(':')[1].split(' '))]

# task 1
d_times = [int(t) for t in times]
d_distances = [int(d) for d in distances]
res = 1
for i in range(len(d_times)):
    num_feasible = is_feasible(d_times[i], d_distances[i])
    res *= num_feasible
print(res)

# task 2
times = int(''.join(times))
distances = int(''.join(distances))
res = is_feasible(times, distances)
print(res)
