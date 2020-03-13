#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    if length == 1:
        return None

    for i in range(length):
        hash_table_insert(ht, weights[i], i)

    for i in range(len(ht.storage)):
        if ht.storage[i]:
            rt = limit - ht.storage[i].key
            if hash_table_retrieve(ht, rt) != None:
                if hash_table_retrieve(ht, rt) > ht.storage[i].value:
                    return (hash_table_retrieve(ht, rt), ht.storage[i].value)
                else:
                    if hash_table_retrieve(ht, rt) == ht.storage[i].value:
                        return (hash_table_retrieve(ht, rt), ht.storage[i].value - 1)
                    else:
                        return (ht.storage[i].value, hash_table_retrieve(ht, rt))


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
