from read_input_common import read_input_common


def read_day_input(input: str) -> str:
    return read_input_common(7, input)


def main(part: int, input: str) -> int:
    raw = read_day_input(input)
    instructions = parse_output(raw)
    (tree, dirs) = recreate_tree_from_instructions(instructions)
    if part == 1:
        return sum(filter(lambda x: x < 100000, map(calc_dir_size, dirs.values())))
    used_space = calc_dir_size(tree)
    free_space = 70000000 - used_space
    needed_space = 30000000 - free_space
    return sorted(
        filter(lambda x: x > needed_space, map(calc_dir_size, dirs.values()))
    )[0]


dir_size_cache = {}


def calc_dir_size(dir):
    name = dir["name"]
    if name in dir_size_cache:
        return dir_size_cache[name]
    files = dir["files"]
    dirs = dir["dirs"]
    file_size = sum(files.values())
    dir_size = sum(map(calc_dir_size, dirs.values()))
    total = file_size + dir_size
    dir_size_cache[name] = total
    return total


def recreate_tree_from_instructions(instructions):
    tree = {"files": {}, "dirs": {}, "name": "root"}
    node_stack = []
    dirs = {}
    current_node = tree
    for instruction in instructions:
        if instruction[0] == "cd":
            destination = instruction[1]
            if destination == -1:
                current_node = node_stack.pop()
            else:
                node_stack.append(current_node)
                current_node = current_node["dirs"][destination]
        elif instruction[0] == "home":
            current_node = tree
            node_stack = []
        elif instruction[0] == "file":
            current_node["files"][instruction[1]] = instruction[2]
        elif instruction[0] == "dir":
            dir_name = instruction[1]
            if dir_name not in current_node["dirs"]:
                unique_name = "/".join([current_node["name"], dir_name])
                new_dir = {
                    "files": {},
                    "dirs": {},
                    "name": unique_name,
                }
                current_node["dirs"][dir_name] = new_dir
                dirs[unique_name] = new_dir
    return (tree, dirs)


def parse_output(input: str) -> tuple:
    lines = input.splitlines()
    instructions = []
    for line in lines:
        words = line.split(" ")
        if words[0] == "$":
            instruction = parse_cmd(words)
        else:
            instruction = parse_ls(words)
        instructions.append(instruction)
    return instructions


def parse_cmd(words: list) -> tuple:
    if words[1] == "cd":
        if words[2] == "/":
            return "home"
        if words[2] == "..":
            return ("cd", -1)
        return ("cd", words[2])
    if words[1] == "ls":
        return "ls"


def parse_ls(words: list) -> tuple:
    if words[0] == "dir":
        return ("dir", words[1])
    return ("file", words[1], int(words[0]))
