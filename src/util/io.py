from pathlib import Path

def read_input_file(file_name: Path) -> tuple[int, int, list[int]]:
    with open(file_name, 'r') as file:
        km = file.readline().strip()
        
        k, m = km.split(" ")
        k, m = int(k), int(m)

        rm_str = file.readline().strip().split(" ")
        rm = [int(r) for r in rm_str]

    return (k, m, rm)
    
def write_to_file(file_name: str, miss_counts: tuple[int,int,int]):
    fifo, lru, optff = miss_counts
    with open(file_name, "w") as file:
        file.write(f"FIFO   : {fifo}\n")
        file.write(f"LRU    : {lru}\n")
        file.write(f"OPTFF  : {optff}\n")
        
        