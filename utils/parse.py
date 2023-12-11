def text_to_list(text):
    return text.split("\n")


def text_to_int_list(text):
    return [list(map(int, line.split())) for line in text.split("\n") if line.strip()]


def text_to_grid(text):
    # print(text, text.split("\n"))
    return [[*line] for line in text.split("\n")]
