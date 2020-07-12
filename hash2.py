
# big ideas: use all the info you can to scramble stuff, even the bits
## use bit shifting to get a new weird sort-of-random number
def djb2(key):
    hash = 5381

    for char in key:
        hash = (( hash << 5) + hash) + ord(char)
        # hash = (( hash * 33) + hash) + ord(char)
    return hash

# s1
hash_table = [None] * 8

#s8 create class HashTable
class HashTableItem:
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next
        
# s2 create hash function
def my_hash(s):
    s_utf8 = s.encode()

    total = 0

    for c in s_utf8:
        total += c

    return total

# s3 insert value into our hash table
def put(key, value):
    #s3a hash the key(string) returns some number 
    hashed_key = my_hash(key)

    #s3b make it module to ensure it a valid index within our hash table
    index = hashed_key % len(hash_table)

    #7 print a warning if we are going to overwrite
    if hash_table[index] != None:
        print('omg think of the data!')

    #s3c then go to hash_table go to index and insert value
    # hash_table[index] = value
    #s8a
    hash_table[index] = HashTableItem(key, value)

    #s3d test  # [None, None, None, None, 'hello world', None, None, None]
    # put("hello", "hello world")
    
# s4 take in a key & responsible for finding that key & returning it to us
def get(key):
    #s4a hash it so we can compare hashes
    hashed_key = my_hash(key)
    #s4b hash will fit in the confine of hash_table
    index = hashed_key % len(hash_table)

    #s8b return value 
    table_item = hash_table[index]

    #s8c
    return table_item.value
    #s4c return value
    # return table_item[index]

    #s4d test 
    # print(get("hello"))

# s5 delete 
def delete(key):
    #s5a hash the key
    hashed_key = my_hash(key)
    #s5b find the index by taking th modulo 
    index = hashed_key % len(hash_table)
    #s5c and set it to None
    hash_table[index] = None

put("hello", "hello world")

#6 caused a collision
put("olleh", "we didnt start the fire")

print('GET', get("hello"))

print(hash_table)

#s5d test
# delete("hello")
print(hash_table)

# [None, None, None, None, 'hello world', 'we didnt start the fire', None, None]
# [None, None, None, None, None, None, None, None]

#8 What to do inside of put() to handle overwriting
# open addressing
## put in a surrounding/different index
## linear probing: find the next available index and put it there
## cuckoo probing: if you find something there already, kick it out, it goes to next index
# double hashing: hash the hash
# disallow it!
# chaining using link list

# Chaining example
'''
Index  Chain (linked list)
----   ---------------
0      ("qux", 54)  -> None
# 1      38 -> 42 -> None
1      ('baz', 38) -> ("foo", 29)  -> None
2      ("bar", 99)  -> None
3      LL[self.head = Node(self.key = "fox", self.value = 101) -> Node("tree", 209) -> None]
4      -> None

put("foo", 42)   # hashed to index 1
put("foo", 29)   
put("bar", 99)   # hashes to index 2
put("baz", 38)   # hashes to index 1! collision!
put("qux", 54)   # hashes to 0
put("fox", 101)  # hashes 3
put("tree", 209) # hashes 3

get("qux") return 54
get("foo") # iterate through LL find 42
get("fred")  # hashes to 0 --> return None


delete("baz")

'''

# Insert a LL into the hash table, when you put something in
# hash table main data structure: [LL, LL, LL, None, LL, None, None]

# how to make the LL work with our hash table?
## ensure each node has a key as well as a value
## change methods to use keys, not just values, where necessary
## write a new method, maybe insert_or_overwrite
### search for the key, if found, overwrite
### otherwise, add a new node


#9 generic ListNode and LinkedList
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def find(self, value):
        current = self.head

        while current is not None:
            if current.value == value:
                return current
        
            current = current.next

        return None

    def insert_at_tail(self, value):
        node = ListNode(value)

        # if there is no head
        if self.head is None:
            self.head = node
        else:
            current = self.head

            while current.next is not None:
                current = current.next
            current.next = node

    def delete(self, value):
        current = self.head

        # if there is nothing to delete
        if current is None:
            return None

        # when deleting head
        if current.value == value:
            self.head = current.next
            return current

        # when deleting something else
        else:
            previous = current
            current = current.next

            while current is not None:
                if current.value == value: # found it!
                    previous.next = current.next  # cut current out!
                    return current # return our deleted node

                else:
                    previous = current
                    current = current.next

            return None # if we got here, nothing was found!




'''

0   A  ->  E  -> O -> P
1   B  ->  F  -> I -> J -> K -> L
2   C  ->  G  -> M
3   D  ->  H  -> N -> Q -> R

get(A)
get(H)


Hash Table Load Factor
number of things / length of array (number of buckets)

18/4 = 9/2 = 4.5

Load factor < 0.7, aka 70%

0  A
1  B -> C
2 
3  


# How to resize??
make a new array, with double the capacity, to reduce how much often we need to do this

0
1
2  B
3
4  A -> D
5
6  C
7

# How to keep track of how many things we've inserted?
## keep a counter, every time you insert
### if you overwrite, that's not a new thing


# Shrinking, based on the load factor
When you delete, also update your tracker
if load factor < 0.2, rehash! 
Make a new array, half the size

Minimum size 8, don't halve below 8

STRETCH GOAL

'''