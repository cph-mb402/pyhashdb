# pyhashdb
Basic Key Value Database implementation with in memory hashmap indexing coded in python. I have used a python dictionary to portray the hashmap, as it has the same functionality.

There are 3 files of interest in this project.

These files should be runnable with an instalation of python 3.

1. The write_db.py, which is the file in which a hashmap is built (if a database existed previously) a file is opened, bytes are written to it, and a hashmap is update on each write. In the case that we later would like to read from the database in the same context, the in memory hashmap could be reused if desired.

2. The read_db.py in which the hashmap is built and the it is used to read from the database file using the byte offset found in the hashmap.

3. The index_hashmap file which hosts the get_hashmap() function, which reads the database file and generates the hashmap, after which it returns it. In the case of not finding the database file, an empty hashmap is returned.
