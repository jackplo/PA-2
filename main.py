from src.util.io import read_input_file
from src.policies import BaseCache, LRUCache, FIFOCache, OPTFFCache

def main():
    k, m, rm = read_input_file("data/1.in")

    fifo = FIFOCache(k)
    lru = LRUCache(k)
    optff = OPTFFCache(k, rm)

    for i in range(m):
        fifo.get(rm[i])
        lru.get(rm[i])
        optff.get(rm[i])

    print(f"FIFO  :  {fifo.get_miss_count()}")
    print(f"LRU   :  {lru.get_miss_count()}")
    print(f"OPTFF :  {optff.get_miss_count()}")

if __name__ == "__main__":
    main()
