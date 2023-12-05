from utils.parse import text_to_list


class MappingClass:
    def __init__(self):
        self.__mapping_ranges = []

    def add_mapped_range(self, destination, source, range):
        self.__mapping_ranges.append(
            {
                "destination": int(destination),
                "source": int(source),
                "range": int(range),
            }
        )

    def get_mapped_location(self, source):
        source = int(source)
        for map in self.__mapping_ranges:
            src = map["source"]
            dest = map["destination"]
            rng = map["range"]
            if src <= source <= src + rng:
                return dest + source - src

        return source

    def get_values(self):
        return dest, src, rng

    # DELETE ME
    def print_vars(self):
        print(
            self.__mapping_ranges
            # self.__mapping_ranges["destination"],
            # self.__mapping_ranges["source"],
            # self.__mapping_ranges["range"],
        )


def get_seeds(seed_line):
    seeds = seed_line[seed_line.index(":") + 1 :].split()
    return seeds


def get_seeds_pairs(seed_line):
    seeds = seed_line[seed_line.index(":") + 1 :].split()

    # seed_pairs = {}
    seed_pairs = []
    for i_seed in range(0, len(seeds), 2):
        seed_pairs.append(
            (int(seeds[i_seed]), int(seeds[i_seed]) + int(seeds[i_seed + 1]))
        )  # [seeds[i_seed]] = seeds[i_seed + 1]
        # seed_pairs[seeds[i_seed]] = seeds[i_seed + 1]

    return seed_pairs


def parse(problem_input, seed_parser):
    start = False
    seeds = None
    current_mapping = None
    mapping_list = []
    m = []
    for line in problem_input:
        if line.startswith("seeds: "):
            seeds = seed_parser(line)

        if line.find("map:") >= 0:
            start = True
            current_mapping = MappingClass()
            continue

        if line == "":
            if start:
                mapping_list.append(current_mapping)
            start = False
            current_mapping = None
            continue

        if start:
            dest, source, range = line.split()
            current_mapping.add_mapped_range(dest, source, range)
            m.append((int(dest), int(source), int(range)))

    mapping_list.append(current_mapping)

    return seeds, mapping_list, m


def solution_one(problem_input):
    seeds, mappings = parse(text_to_list(problem_input), get_seeds)
    lowest = None

    for seed in seeds:
        location = seed
        for map in mappings:
            location = map.get_mapped_location(location)

        if not lowest:
            lowest = location
        else:
            lowest = min(lowest, location)
    return lowest


def solution_two(problem_input):
    seeds, _, m = parse(text_to_list(problem_input), get_seeds_pairs)
    lowest = None
    print(seeds)
    # for m in mappings:
    #     m.print_vars()
    blah = []
    while len(seeds):
        seed_start, seed_end = seeds.pop()

        for dest, src, rng in m:
            overlap_start = max(seed_start, src)
            overlap_end = min(seed_end, src + rng)

            if overlap_start < overlap_end:
                blah.append((overlap_start - src + dest, overlap_start - src + dest))
                if overlap_start > seed_start:
                    seeds.append((seed_start, overlap_start))
                if seed_end > overlap_end:
                    seeds.append((overlap_end, seed_end))
                break
        else:
            blah.append((seed_start, seed_end))

    seeds = blah

    # for seed_start, seed_stop in seeds.items():
    #     for seed in range(int(seed_start), int(seed_start) + int(seed_stop)):
    #         location = seed
    #         for map in mappings:
    #             location = map.get_mapped_location(location)

    #         if not lowest:
    #             lowest = location
    #         else:
    #             lowest = min(lowest, location)
    print(min(seeds))
    return lowest
