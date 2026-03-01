def read_input_file(file_name: str) -> tuple[int, int, list[int]]:
    with open(file_name, 'r') as file:
        km = file.readline().strip()

        k, m = int(km[0]), int(km[2])

        rm_str = file.readline().strip().split(" ")
        rm = [int(r) for r in rm_str]

    return (k, m, rm)
    
