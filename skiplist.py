# Assignment information
# ---
# Class : COSC 301 - Data structures and algorithms 2
# Assignment : Skiplists - Home Work Assignment 4
# Student : Nirman Dave

# Program information
# ---
# Name : skiplist.py
# Description : A program that creates and edits a skiplist.
# Language : Python 3

# importing modules and libraries
import random
from intset301 import IntSet301

class Node:
    """
    The Node class defines node as an object that is then used by the Skiplist.
    A node is an object that has the start, end and heigh as its main attributes.
    """

    def __init__(self, start, end, h):
        """
        A node initializes with start, end and height. Node data is represented as a tuple
        of intervals.
        """
        self.start = start
        self.end = end
        self.height = h
        self.data = (start, end)
        self.next = [None] * h

    def add_level(self):
        self.next.append(None)

    def __str__(self):
        return "<%d; %d; %d>" % (self.start, self.end, self.height)

    def compareTo(self, n):
        if self.start <= n <= self.end:
            return 0
        elif n < self.start:
            return 1
        else:
            return -1

class SkipList(IntSet301):
    def __init__(self):
        self.node_counts = [0]
        self.head = Node(-float("inf"), -float("inf"), 1)
        self.tail = Node(float("inf"), float("inf"), 1)
        self.head.next[0] = self.tail

    def size(self):
        return self.node_counts[0]
        
    def __find(self, key):
        last = [self.head] * len(self.head.next)

        curr = self.head
        level = len(self.head.next) - 1
        while level >= 0:
            while curr.next[level].start < key:
                # Change the condition in find so the inner loop stops when the next node contains key or an interval greater than key.
                if curr.next[level].compareTo(key) == 0 or curr.next[level].compareTo(key) == 1:
                    break
                else:
                    curr = curr.next[level]
            last[level] = curr
            level = level - 1

        return last

    def contains(self, value):
        """
        Checks if a value exists in the skiplist.
        """
        last = self.__find(value)[0]
        if last.next[0].compareTo == 0:
            return last.next[0].start == value

    def add(self, value):
        """
        Adds a node to a skiplist and performs merging operations wherever needed.
        """
        last = self.__find(value)
        curr = last[0].next[0]

        if self.contains(value) == True:    # if node already exists, do nothing
            pass
        else:
            if curr.start > value:
                if (abs(value-last[0].end) == 1) and (abs(value-curr.start) == 1):  # merge the nodes if value to be added follows this condition
                    last[0].end = curr.end
                    self.delete_node(last, curr)
                elif abs(value - last[0].end) == 1: # if value is 1 more than previous node
                    last[0].end = value
                elif abs(value - curr.start) == 1: # if value is 1 less than current node
                    curr.start = value
                else:   # else, create a new node entirely
                    new_height = self.__choose_height()

                    while len(self.head.next) < new_height:
                        self.head.add_level()
                        self.tail.add_level()
                        self.head.next[-1] = self.tail
                        last.append(self.head)
                        self.node_counts.append(0)

                    new_node = Node(value, value, new_height)

                    for h in range(0, new_height):
                        self.node_counts[h] += 1
                        old_next = last[h].next[h]
                        last[h].next[h] = new_node
                        new_node.next[h] = old_next

    def remove(self, value):
        """
        Removes a node from the skiplist and performs merging operations wherever needed.
        """
        last = self.__find(value)
        to_delete = last[0].next[0]

        if self.contains(value) == False:   # if node does not exist, do nothing
            pass
        else:
            if to_delete.start == to_delete.end == value:   # if node has only one value (no intervals), delete it
                self.delete_node(last, to_delete)
            elif (to_delete.start == value) and (to_delete.end != value):   # if value is the start integer of the to_delete node, resize the range by incrementing start value by 1
                to_delete.start += 1
            elif (to_delete.end == value) and (to_delete.start != value):   # if value is the end integer of the to_delete node, resize the range by decrimenting end value by 1
                to_delete.end -= 1
            else:
                del_start = to_delete.start         # to_delete.start value
                del_end = to_delete.end             # to_delete.end value
                self.delete_node(last, to_delete)   # delete the to_delete node

                for i in range(del_start, value):   # create node by iteratively adding consecutive nodes in range -- to_delete's start to value-1
                    self.add(i)
                for i in range(value+1, del_end+1):     # create node by iteratively adding consecutive nodes in range -- value+1 to to_delete's end
                    self.add(i)


    def delete_node(self, last, to_delete):
        """
        Deletes a given node from the skiplist.
        """
        # link around deleted node
        height = len(to_delete.next)
        for h in range(0, height):
            last[h].next[h] = to_delete.next[h]
            self.node_counts[h] -= 1

        # remove extra levels in dummy nodes
        while len(self.head.next) > 1 and self.node_counts[-1] == 0:
            self.head.next.pop()
            self.tail.next.pop()
            self.node_counts.pop()

    def next_excluded(self, n):
        """
        Returns the next excluded value of given n in the skiplist.
        """
        last = self.__find(n)[0]
        curr = last.next[0]

        if curr.start <= n <= curr.end:    # if n is in range, range's upper bound + 1
            return curr.end + 1 
        else:
            return n  # else n itself is the next excluded

    def __str__(self):
        out = ''
        curr = self.head.next[0]
        while curr != self.tail:
            out += curr.__str__()
            print (out)
            curr = curr.next[0]
        return out

    def __choose_height(self):
        """
        Randomly choses a height for a node.
        """
        height = 1
        while random.randint(0, 1) == 0:
            height += 1
        return height


def main():
    s = SkipList()

    test_values = [2, 1, 4, 6, 8, 3, 9, 10, 5, 7]
    print (s)
    for i in test_values:
        print("===ADDING %d ===" % i)
        s.add(i)
        print(s)
        for j in range(0, 12):
            print("next_excluded(%d) = %d" % (j, s.next_excluded(j)))

    for i in range(0, 12):
        print("%d: %s" % (i, s.contains(i)))
    print(s)

    remove_values = [1, 10, 5, 2, 4, 8, 7, 6, 9, 3]
    for i in remove_values:
        print("=== REMOVING %d ===" % i)
        s.remove(i)
        print(s)

    print("===ADDING BACK ===" )
    for i in test_values:
        s.add(i)
    print(s)
    

if __name__ == "__main__":
    main()