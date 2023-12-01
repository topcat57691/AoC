def file_exists(file_name):
    try:
        f = open(file_name, "r")
    except:
        return False
    f.close()
    return True


def write_file(file_name, contents):
    if file_exists(file_name):
        f = open(file_name, "w")
    else:
        f = open(file_name, "x")

    f.write(contents)
    f.close()


def read_file(file_name):
    if not file_exists(file_name):
        raise Exception(f"Could not find {file_name}")

    f = open(file_name, "r")
    contents = f.read()
    return contents
