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
        self.local_time = 0
        self.update_table = {}
        self.timeout = 10
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
        # if self.name == 'HARV' and self.local_time >= 20:
        #     return 0
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
        link = self.table.get(destination)[1]
        return link
                    

    def update(self, source, table):
        """
        Updates this routing table based on the routing message just
        received from the node whose name is given by source.  The table
        parameter is the current RoutingTable object for the source.
        """
        for node in table.table:
            hop = table.table[node][0]+1
            self.update_table[node] = self.local_time
            if node != self.name:
                if node in self.table:
                    # link = self.table[node][1]
                    if hop <= self.table.get(node)[0]:
                        self.table[node] = (hop, source)
                        self.update_table[node] = self.local_time
                else:
                    # link=table.table[node][1]
                    self.table[node] = (hop, source)
            #print("REG",self.local_time)
            # i want it 
            if self.update_table[source] <= self.local_time-self.timeout:
                print(self.update_table[node])
                print("DEL",self.local_time)
                del self.update_table[source]
                del self.table[source]
        self.local_time+=1
#need something to update the hop if it's better
#need something to 





'''
It seems like Eric's code provides a simple LinkedList interface,
which is fine, but it means that all nodes have to be passed through first by BFS.








'''
        
