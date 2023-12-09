from common.tools import read_input


class Mapping:
    def __init__(self, dest_start, source_start, span):
        """
        :type dest_start: int 
        :type source_start: int 
        :type span: int
        """
        self.dest_start = dest_start
        self.source_start = source_start
        self.source_end = source_start + span

    def belongs(self, input):
        """
        :type input: int
        :rtype: bool
        """
        return self.source_start <= input <= self.source_end

    def transform(self, input):
        """
        :type input: int 
        :rtype: int 
        """
        offset = input - self.source_start
        return self.dest_start + offset


class Map:
    def __init__(self, mappings):
        """
        :type mappings: list[Mapping]
        """
        self.mappings = mappings

    def process(self, input):
        """
        :type input: int 
        :rtype: int
        """
        for mapping in self.mappings:
            if mapping.belongs(input):
                return mapping.transform(input)
        return input


inp = read_input()
test_inp = read_input('task_sample.txt')
lines = inp.split('\n')

seeds = lines[0].split(':')[1]
seeds = [int(r) for r in filter(lambda x: x, seeds.split(' '))]

map_bundle = []
mapping_collection = []
# assemble maps from almanac
for i, line in enumerate(lines):
    if i == len(lines) - 1:
        # append last map
        map_bundle.append(Map(mapping_collection))
        continue
    elif i == 0 or not line:
        # skip seeds and empty lines
        continue
    if line[0].isdigit():
        mapping_collection.append(Mapping(*[int(n) for n in filter(lambda x: x, line.split(' '))]))
        continue
    else:
        map_bundle.append(Map(mapping_collection))
        mapping_collection = []
        continue

locations = []

for seed in seeds:
    intermediate = seed
    for map in map_bundle:
        intermediate = map.process(intermediate)
    locations.append(intermediate)

print(len(locations))
print(min(locations))
