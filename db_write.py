import sys
import index_hashmap
_hash_map = index_hashmap.get_hashmap()

def to_bytes_line(string):
    return bytes(string + '\n', 'utf-8')

def write_pair(key, value):
    bytesData = to_bytes_line(key + ',' + value)
    file.write(bytesData)
    _hash_map[key] = _hash_map[sorted(_hash_map.keys())[-1]] + sys.getsizeof(bytesData)

file = open("database", "wb")
write_pair('key', 'value')
write_pair('key2', 'value2')
file.close()