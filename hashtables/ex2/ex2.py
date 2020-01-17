#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)
"""
UNDERSTANDING:

    Reconstruct you trip from the jumbled up mass of flight tickets.
    Each Ticket has a source and destination which are STRINGS

    source = starting airport
    destination = next airport

    First Flight Ticket: {source: "NONE", destination: "airport"}
    Last Flight Ticket: {source: "airport", destination: "NONE"}

    None's a string? Yes

    EXAMPLE:

    tickets = [
        Ticket{ source: "NONE", destination: "PDX" },
        Ticket{ source: "PDX", destination: "DCA" },
        Ticket{ source: "DCA", destination: "NONE" },
        ]

    Result = ["PDX", "DCA", "NONE"]

    The Link is between the DESTINATION of PREVIOUS ticket and the SOURCE of NEXT ticket

input = [tickets] and length
output = an array of strings with the route of trip in order

Solution should run in linear time
assume function will always be handed a valid ticket chain as input

HINTS:
    NOTE: The crux of this problem requires us to 'link' tickets together to reconstruct the entire trip. For example, if we have a ticket ('SJC', 'BOS') that has us flying from San Jose to Boston, then there exists another ticket where Boston is the starting location, ('BOS', 'JFK').

                   LINK               LINK               LINK
                     |                  |                  |
               _____________      _____________      _____________
               |           |      |           |      |           |
        s      d           s      d           s      d           s      d
    ('NONE', 'SJC') --> ('SJC', 'BOS') --> ('BOS', 'JFK') --> ('JFK', 'NONE')

    
    NOTE: We can hash each ticket such that the starting location is the key and the destination is the value. Then, when constructing the entire route, the ith location in the route can be found by checking the hash table for the i-1th location.

      key   :    value
    [source : destination]
"""

class Ticket:
    def __init__(self, source, destination):
        self.source = source                #starting airport
        self.destination = destination      # next airport


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """

    return route


ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]



print(reconstruct_trip(tickets, 3))
