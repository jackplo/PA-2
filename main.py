from src.util.io import read_input_file, write_to_file
from src.policies import BaseCache, LRUCache, FIFOCache, OPTFFCache
import sys
from pathlib import Path
def main():
    if len(sys.argv) != 2:
        return
    
    input_file = Path(sys.argv[1])
    output_file = input_file.with_suffix(".out")
    
    k, m, rm = read_input_file(input_file)

    fifo = FIFOCache(k)
    lru = LRUCache(k)
    optff = OPTFFCache(k, rm)

    for i in range(m):
        fifo.get(rm[i])
        lru.get(rm[i])
        optff.get(rm[i])

    #print(f"FIFO  :  {fifo.get_miss_count()}")
    #print(f"LRU   :  {lru.get_miss_count()}")
    #print(f"OPTFF :  {optff.get_miss_count()}")

    fifo_misses = fifo.get_miss_count()
    lru_misses = lru.get_miss_count()
    optff_misses = optff.get_miss_count()
    misses = (fifo_misses, lru_misses, optff_misses)
    write_to_file(str(output_file),misses)
    
if __name__ == "__main__":
    main()
