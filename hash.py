my_arr = ["hello", "world", 'how', "are", 'you']
# O(1) with an array?
# append, pop 
# look up from index 
my_arr[4]

# hashing or hash functions: that will give us the index of the word we're looking for
## 'you' --> 4


# to make a hash of something

# take a string 
# give us a number 

# def my_hash(s):
#     return len(s)

# my_hash('you') # return 3

# my_alphabet = {'a': 0, 'b': 1}
# def my_hash(s):
#     total = 0
#     for char in s:
#         total += my_alphabet[char]
#     return total

# ASCII: assigns letters to numbers
## ord()

# UTF-8
# how to make the output more unique?
## could use a random number? but make sure we get back same index every time?

# def my_hash(s):
#     s_utf8 = s.encode()

#     for c in s_utf8:
#         print(c)

# my_hash("hello")

def my_hash(s):
    s_utf8 = s.encode()

    total = 0
    for c in s_utf8:
        total += c

    return total

hello_index = my_hash("hello") # 532

my_arr = [None] * 5 

hello_index = hello_index % len(my_arr)

my_arr[hello_index] = 'hello'

# print(my_arr)

world_index = my_hash("world") # 552
print(world_index)  

world_index = world_index % len(my_arr)

my_arr[world_index] = 'world value'

print(my_arr)
print(my_arr[world_index])

# my_dict[key]

# hash table, dictionary, object, hash map: array paired up with hash function

# inserted into our hash map
key = 'key'
key_index = my_hash(key) % len(my_arr)
my_arr[key_index] = 'value'
print(my_arr)

# access the value
key_index = my_hash(key) % len(my_arr)
print(my_arr[key_index])


# steps to put 
## say you have a hash function, and you have an array, and key-value to put in the array
## 1. hash the word, get some number back from hash function
## 2. module this number with array length to find the index
## 3. use index to insert word into

# steps to get
## 1. hash the key/word, get number back from hash function
## 2. module this number with array length to find the index
## 3. look up value at that index, return it

## dynamic programming

# hash function ideal speeds
## in a hash table: fast! we want to look stuff up FAST!
## to hash passwords and store hashes insteal of plaintext passwords: relatively SLOW

# output of hash function: hash, or digest of

# a good hash function like SHA256 gives a totally unique output
# can use as id aka fingerprint of a document (document == big string)

## import hashlib
## hashlib.sha256('hello'.encode())

# Can you reverse the output of a hash function? Can you go from 532 --> 'hello'?
## a good has function is non-reversible

## hashlib.sha256('hello'.encode()).hexdigest()



