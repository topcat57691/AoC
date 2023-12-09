def text_to_list(text):
    return text.split("\n")


def text_to_int_list(text):
    return [list(map(int, line.split())) for line in text.split("\n") if line.strip()]
