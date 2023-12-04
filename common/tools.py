
def read_input(file_path=None):
    default_path = './puzzle_input.txt'
    file_path = file_path or default_path

    with open(file_path, 'r') as f:
        file_contents = f.read()

    return file_contents
