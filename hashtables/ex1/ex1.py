#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)

"""
UNDERSTANDING:
limit = weight limit
weights = [item weights list]

get the 2 INDICES of the above weights list that = sum of limit

answer is a (tuple)
(higher, smallest)
higher value indice
smallest value indice

Input: list of weights and the limit
Output: tuple of two numbers

**NOTE:  if such a pair does not exist, RETURN NONE

Solution should run in linear time

EXAMPlE:
        Indices    0| 1| 2 | 3 | 4
input: weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21

output: [ 3, 1 ]  
# since these are the indices of weights 15 + 6 = 21

PLAN:

1. iterate through the weights --> for loop
    a. limit - weight[i] = difference
    b. find index
2. insert into the ht
    hash_table_insert(hash_table, key, value)
                        (ht,)
    hash_table = ht                    
    key = weight.value
    value = (index, difference)
3. Compare weight.value in weight list to ht difference
    hash_table_retrieve(hash_table, key) ?
                        (ht, ?)
    if weight = difference return indice in tuple (highest, smallest)


"""


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16) #limit size of hash table and this is what we are inserting into
    
    index = 0
    for weight in weights:
        difference = limit - weight
        print("Index:", index,"Weight = ",weight,":" , "Difference = ",difference)
        index += 1

        result = hash_table_insert(ht, weight, (index, difference))
        # htResult = hash_table_retrieve(ht, difference)

        print("HT",ht)
        

    

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

weights = [4, 6, 10, 15, 16 ]
length = 5
limit = 21

print(get_indices_of_item_weights(weights, length, limit))
