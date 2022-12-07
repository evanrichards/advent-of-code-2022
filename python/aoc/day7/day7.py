from read_input_common import read_input_common


def read_day_input(input: str) -> str:
    return read_input_common(7, input)


def main(part: int, input: str) -> int:
    raw = read_day_input(input)
    instructions = [line.split(" ") for line in raw.splitlines()]
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
        if instruction[0] == "$":
            if instruction[1] == "cd":
                destination = instruction[2]
                if destination == "..":
                    current_node = node_stack.pop()
                elif destination == "/":
                    current_node = tree
                    node_stack = []
                else:
                    node_stack.append(current_node)
                    current_node = current_node["dirs"][destination]
        else:
            if instruction[0] == "dir":
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
            else:
                current_node["files"][instruction[1]] = int(instruction[0])
    return (tree, dirs)
