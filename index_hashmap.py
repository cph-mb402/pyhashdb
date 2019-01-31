import sys
import os.path

def get_hashmap():
        if os.stat("database").st_size==0:
                return {}

        file = open("database", "rb")

        data = file.read()

        data = data.decode('utf-8').split('\n')
        data.pop()

        hash_map = {}
        byte_offset = 0

        for pair in data:
                key = pair.split(',', 1)[0]
                hash_map[key] = byte_offset
                byte_offset = byte_offset + len(pair) + 1
                # print(pair)
        
        file.close()
        # print(hash_map)
        return hash_map

# get_hashmap()