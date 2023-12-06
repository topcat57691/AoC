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

    def map_seed_range(self, seeds, seed_lower, seed_upper):
        for map in self.__mapping_ranges:
            src = map["source"]
            dest = map["destination"]
            rng = map["range"]
            print("range: ", src, dest, rng)
            print("seed: ", seed_lower, seed_upper)

            if (seed_upper < src) or (seed_lower > src + rng):
                print("Seed not in this range")
                continue

            if src <= seed_lower <= src + rng:
                print("Seed range starts within map")

                if src <= seed_upper <= src + rng:
                    print("And is completely contained within this map")
                    seeds.append((seed_lower, seed_upper))
                else:
                    print("But overlaps the upper bound")
                continue

            print("Seed starts before the map range and overlaps the lower bound")

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

    seed_pairs = []
    for i_seed in range(0, len(seeds), 2):
        seed_pairs.append(
            (int(seeds[i_seed]), int(seeds[i_seed]) + int(seeds[i_seed + 1]) - 1)
        )

    return seed_pairs


def parse(problem_input, seed_parser):
    start = False
    seeds = None
    current_mapping = None
    mapping_list = []
    # m = []
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
            # m.append((int(dest), int(source), int(range)))

    mapping_list.append(current_mapping)

    return seeds, mapping_list  # , m


# def parse(problem_input, seed_parser):


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


def test(mlist):
    mlist.append(3)


def thing(list):
    print(list)


def solution_two(problem_input):
    seeds, mappings = parse(text_to_list(problem_input), get_seeds_pairs)
    lowest = None

    while seeds:
        seed_lower, seed_upper = seeds.pop()
        for map in mappings:
            map.map_seed_range(seeds, seed_lower, seed_upper)
            pass
    print(seeds)
    
    # typescript solution here:
    # https://www.typescriptlang.org/play?#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-PzK2eeIHgmgcKPJtFZQh+svAEnhF4-MpX3O8uSM4eg-d2XgocySdkqjWD7WrxIxJR24WMvrHYHEuIuAhX9HryxMe8mjHukuFx9DRJsEsSHEZlwiuGylCBKU0heGjF4iDnUG5T8VOAYB80LHSCCDMAsQdHQlhEtRsnx08RylOHlDtxlXdUdjYADENUF0bhcH0CQS6E6Fp3p0ZxZxigQBAGAASlGHADZ2BCYBND8H9CHA1j5XJiDkSAKWzDensS+ilUDisAzScHxxqU31vUsEoEIzUF3FLjzycH5AEKsBNBFCWjL1qDxFd1kDBgKSOStWsG+VgQugWE80BlV3ywBgax0FUgyhszjhPC4xBx63VBJnuUEnoCkGVG1gTn2DJC4ysHJXRS9XpGYluFVQLhsIynzijETEAnfDAVaDGgoUNB-AD2MEpH4BYWQKHA8Fww0DxB5H7Go0w1bGPHMGsC7AWhJm+WYx4l4CtHakKHUGZi1X+E+WUjjjn1RVwlV1llTy6xhE4h6i2GAXsieANECSdRxS+BFRuCMFKIUAJFaC8g6kLEJEUFRG6l4CUEtB7HiQo1+CvlVBd2FF2DRhDg2GDB7C2Dejrl3mdQaA6GUieCHGYhxCTCDQkGOGuGqgyn+EHzbF139BVBgnoE4DcQGkBPmOdCqN+NIgHFW2SEpBOBcFfkX373QMFl2SIReFw0pBAjwn+FoJ-BgBIn4yaBFCcE7ESE6A+GfHYXymtx8g+FsA4yKLIWoE8CLnEHpn4yQMDDwXaxNCBGRB6gunuSNHzAbVhDtEkCtC8hkKdn+PHkcAwgNzYQ0SVngIhAWDgQEEUDBLxG6k0CeBAwrmujZEbwWiJne3AimMHDJhpECAyIyheFsEpD0BUkc14DEWUjESylDRfw-DH0uQdERCCELQeBTSz08H1iqDrFrDlzCBxDVk5A4k0JwTvxh0BT5TjL3SFB2yLWo1fg5VaPbFWFlDUEuBkn+j5idMrDclyHrAaEZESz+mylVHBG5LSHsg6lMA4HNgXgegkBLWxS0EOPdCrGiQVD0l8L2AOjEwDF0FjOtycQ0BVUwydyBg9UWHoCrF9C0DjVqFMB9mdDlCLBvO0ld0NAkGQK63aSLAJF5G0VZi8SLVfBsRAkiG0QNkRiekDF-hZQ6I6CynfC4StHLlgnw1NU4j1V-0zkNEDG5MDGEw7G4BLR5GWDGPoCzWsBqXjGwkxRUEJMKC8G+W6z5QOESKvAaztHaFNQkgcHBBwG6FAEgBAAQHwAADpgBxK4BpwAAKAASk6BEugBgF6BICwHgGQFQHQAkogCmB7igDkpwAAB0wAzKcAFKABtKgAAXT0oMqZzkoAHJSBnLrKKB7KoBpxRgkBFKHLDK5KAAiGAIKpSsnZnN9GAAAZUICIAAAU4BRhpxNKrKwA6cAAjGcAAGhgHSqQCyunFsvvXwFgHUoACVUBe58AyAYArLYriBErkqAB+Wy1K4qicEAFKuS8S2AUYTSqgAAbhgH6oAB41K4qIAJLxKwBe4oB+5hr+qABqbAdgBSmAAAb06BgB2omuIEqtmpqokqmA-QgH7jkqsoADlMqZw5L1KIArLRhbKFLcrrqCrbr7rHrnqYAlqYA3rCq7rJrHqfrKBvq+hQalKABfToAAehhpgBUrEskvYN7kBv2qqpqvCpUqHlXCmFGFmoACF2DgAABrCATSxAFANAYAAKpy0y8ysASyvSnuYAfAOSigBSiS6YOSjK4mkmrAAAPhgF5o4JJtpqMpwFIAso8vsv0sCvpssqUrhoRvABGHEumpAFRumDxsJr5ogHCs6E6u6uxuFr5pgBAAnF-R1t7iJtFv1s2u2t2pNumAOuqvJuwBFtJoku-SIA-VZtGo2pgCIBqrnDQDnHAHIHysKtypGC-VZsjpuunFysp0OoTvepSshqstsoFrkrkuAFyrAHWswCFq2t2rLpVsgDKs0rAHFuCtCs5u5v+pnCUvLqduOtOvOtLtbvLuDugHxq4IjrUpstsuysdu7t2tjunHjqHs8tHvHrLpTuqvIAevYGKvHshvCvHu-SgC-TAARrHpgEhtyqzoNrLt6pgG-W1uIAaqIFdpqvIHqriqaunFavaoPtin7nGB-TRtvoxqmpmrmv7nWq7tbpNqsvUoABkQBYocq9qiAABVKYCnNq7ACqv+46kAKYRS7oce8+lAKAYAfuYgTSicRAAgA+suo2mAPO1W2AQO3u0OgesAGOkAOO-AZOjGw+82y2l2v+4Bih7uk2kAAANxnAQFXCgZgZSuwAAFkEp+4ua4AAAPH+yR2Bye1mlu+enaoR0R6ccRqYRBinTSuR+arm-Gn+ox9R1hqen9X6xe-ALR7R5WxG9WlGuSkB+e5WsuyB6B9RuKqxpOtSmx1mlhthu+5ekJuxi+jG3KkRsRiRvxoJ+J-R1cQJgR1u5WjejJ8u0YS2uSlJgxtRlK8awptJpB5uh27R0B2h39AAETyfCnwDAFZs0oYf7vDr3vBo0fwBya3vwCvqIBvrvqmpOrOourKamGKZBumAaYnCaZafYfNr0YMcCZmdXDmYWdZuepweqbLryeocmemaFt8akfWrQcOtGY7outOdgaOaSZ2b2f2fycmbWfGvUsCfObipGfbvGasteYqaCY+cBceaeZ2vwcIeIewG8o-V6bBZ2oyu-TgBJr6d2uhvXt2dboObkoAEIIWiGiB+G9nL7cbr7vn0GxnzrwG4rimY6AmQWnHy70W0XMW4GRnNKSWKmhnyXLnOhoblLVakaNbUaD6Lm3bvbiA-a2a86v0C78AlGoAi6hbTGFH6cwAZWgmwB5WoBh6XqYAABJMACcfGpnZnJShSoAA
    return lowest
    # return -1
    # print(seeds)
    # # for m in mappings:
    # #     m.print_vars()
    # blah = []
    # while len(seeds):
    #     seed_start, seed_end = seeds.pop()

    #     for dest, src, rng in m:
    #         overlap_start = max(seed_start, src)
    #         overlap_end = min(seed_end, src + rng)

    #         if overlap_start < overlap_end:
    #             blah.append((overlap_start - src + dest, overlap_end - src + dest))
    #             if overlap_start > seed_start:
    #                 seeds.append((seed_start, overlap_start))
    #             if seed_end > overlap_end:
    #                 seeds.append((overlap_end, seed_end))
    #             break
    #     else:
    #         blah.append((seed_start, seed_end))

    # seeds = blah

    for seed_start, seed_stop in seeds.items():
        for seed in range(int(seed_start), int(seed_start) + int(seed_stop)):
            location = seed
            for map in mappings:
                location = map.get_mapped_location(location)

    print(min(seeds))
    return lowest
