import index_hashmap

_hashmap = index_hashmap.get_hashmap()
# print(_hashmap)

def getPair(index):
    file = open("database", "rb")
    # print(file.read())
    file.seek(_hashmap[index], 0)
    pair = file.readline().decode('utf-8')
    file.close()

    return pair

def getValue(index):
    return getPair(index).split(",")[1]

print(getValue("key2"))