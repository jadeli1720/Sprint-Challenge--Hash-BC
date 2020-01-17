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

    
    NOTE: We can hash each ticket such that the starting location is the key and the destination is the value. Then, when constructing the entire route, the i[0] location in the route can be found by checking the hash table for the i-[1] location.

      key   :    value
    [source : destination]

Plan:
1. Loop through tickets list and add to hash table
    for each loop like previous ex
    insert the ticket
2. If the first one has source of None;
    this goes in the first position
    
3. Find a way to use the index to put them in the list in order?
    conditional: if value in previous ticket == key of next ticket, it comes next in the list

    b. hash_table_retrieve(hash_table, key) --> searches for key and return value of found key
    
4. return LIST of values to route
    route = ["PDX", "DCA", "NONE"]

"""

class Ticket:
    def __init__(self, source, destination):
        self.source = source                #starting airport
        self.destination = destination      # next airport

    def __repr__(self):
        return f"(source: {self.source}, dest.: {self.destination})"


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length        # what is route? ---the list we are returning
    
    
    for ticket in tickets:
        source = ticket.source
        destination = ticket.destination
        # print(f"Source:{source}, Dest.: {destination}")

        # insert ticket
        hash_table_insert(hashtable, source, destination )
        # if the source equals the string none:
        if source == "NONE":    
            # place it at index[0] of route == destination
            route[0] = destination
            # print("Route",route[0])
    # need to move to next index by looping and find the link: previous-tickets value = next-tickets key return the value of that key using retrieval
    index = 0
    current_destination = 0

    while True:
        # current destination = rout at current index
        current_destination = route[index]
        # print("Current:", current_destination)
        next_destination = hash_table_retrieve(hashtable, current_destination)
        # print("Next:", next_destination)
        index += 1

        route[index] = next_destination
        # print("Route Index:", route[index])
        # print("\n")
        if next_destination == "NONE":
            break
    

    return route


ticket_1 = Ticket("NONE", "SFO")
ticket_2 = Ticket("SFO", "SJC")
ticket_3 = Ticket("SJC", "DIA")
ticket_4 = Ticket("DIA", "BOS")
ticket_5 = Ticket("DIA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5]



print(reconstruct_trip(tickets, 5))
