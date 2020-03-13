#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    for i in range(len(tickets)):
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)

    for i in range(len(tickets)):
        if hashtable.storage[i] != None:
            if hashtable.storage[i].key == 'NONE':
                route[0] = hash_table_retrieve(
                    hashtable, hashtable.storage[i].key)
            elif hash_table_retrieve(
                    hashtable, hashtable.storage[i].key) == 'NONE':
                route[-1] = hashtable.storage[i].key

    for i in range(len(route) - 1):
        route[i + 1] = hash_table_retrieve(
            hashtable, route[i])

    return route[0: -1]
