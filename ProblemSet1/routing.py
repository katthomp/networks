# File: routing.py

"""
This module defines a routing table for the ARPANET routing assignment.
Your job in this assignment is to implement the RoutingTable class so
its methods implement the functionality described in the comments.
"""

#this is a table that contains only the 



class RoutingTable:

    """
    This class implements a routing table, which keeps track of
    two data values for each destination node discovered so far:
    (1) the hop count between this node and the destination, and
    (2) the name of the first node along the minimal path.
    """

    def __init__(self, name):
        """
        Creates a new routing table with a single entry indicating
        that this node can reach itself in zero hops.
        """
        self.name=name
        self.table={self.name:(0, self.name)}
    def getNodeNames(self):
        """
        Returns an alphabetized list of the known destination nodes.
        """
        return sorted(self.table.keys())

    def getHopCount(self, destination):
        """
        Returns the hop count from this node to the destination node.
        """
        # You complete this implementation
        if destination == self.name:
            return 0
        elif self.table.get(destination) is not None:
            return self.table.get(destination)[0]
        else:
            return None
                

    def getBestLink(self, destination): #destination is a string
        """
        Returns the name of the first node on the path to destination.
        """
        hop = self.table.get(destination)[0]
        link = self.table.get(destination)[1]
        print("!!!!!", self.name, link)
        # for node in self.table:
        #     if self.table.get(node) is not None and node != self.name:
        #         new_hop = self.table.get(node)[0]
        #         new_link = self.table.get(node)[1]
        #         if new_hop < hop:
        #             hop = new_hop
        #             link = new_link
        return link
                    

    def update(self, source, table):
        """
        Updates this routing table based on the routing message just
        received from the node whose name is given by source.  The table
        parameter is the current RoutingTable object for the source.
        """
        for node in table.table:
            hop = table.table[node][0]+1
            if node != self.name:
                if node in self.table:
                    # link = self.table[node][1]
                    if hop <= self.table.get(node)[0]:
                        self.table[node] = (hop, source)
                else:
                    # link=table.table[node][1]
                    self.table[node] = (hop, source)
#need something to update the hop if it's better
#need something to 





'''
It seems like Eric's code provides a simple LinkedList interface,
which is fine, but it means that all nodes have to be passed through first by BFS.








'''
        
