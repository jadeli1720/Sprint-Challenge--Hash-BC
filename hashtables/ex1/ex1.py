#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)

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
3. Compare weight.value in weight list to ht difference --> Within for loop
    hash_table_retrieve(hash_table, key) ?
                        (ht, ?)
    if weight = difference return indice in tuple (highest, smallest)

The hash_table_retrieve(hash_table, key) helps!!!
for each loop lets us get the difference between limit and we

"""


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16) #limit size of hash table and this is what we are inserting into
    
    # Keeping track of what index we are at during for each
    index = 0 #
    # for each weight in weights:
    for weight in weights: 
        # Find the difference of limit - weight
        difference = limit - weight
        # print("Index:", index,"Weight = ",weight,":" , "Difference = ",difference)
        
        # find the key to see if it is in ht: key = difference 
        # hash_table_retrieve(hash_table, key)
        htRetrieval = hash_table_retrieve(ht, difference)
        # retrieval will return the value of the key. That value is the stored index
        # {[4, 0], [6, 1], [10, 2], [15, 3]}
        
        # if the the key(difference)ht is not None (if the key is there)
        if htRetrieval is not None:
            # and if the key is smaller than the current index
            if htRetrieval < index:
                print("inside if", index, htRetrieval )
                # return the current index of for each and the value of the key:value pair. Remember, the value of key:value pair is the index of weight at time of insertion. line 83 below
                return(index, htRetrieval)
                

        # Insert the current weight and it's  index
                #hash_table_insert(hash_table, key, value)
        result = hash_table_insert(ht, weight, index)

        # iterating and moving through each index
        index += 1
        # print("HT",ht)
    # Else return none
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
