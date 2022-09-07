#create a basic stack push and pop elements into it 
# create an empty list called stack
stack = []  #initialise an empty one 
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)
stack.pop()
stack.pop()
stack.pop()




#Queue operations on a simple note using collections module 
from collections import deque
# Initializing a queue
q = deque()
# Adding elements to a queue
q.append('a')
q.append('b')
q.append('c') 
print("Initial queue")
print(q)
# Removing elements from a queue
print("\nElements dequeued from the queue")
print(q.popleft())
print(q.popleft())
print("\nQueue after removing elements")
print(q)





#Create a basic singly linked list with some basic operations
class Node:
    def __init__(self, data=None, next=None):
        self.data=None
        self.next=None

class LinkedList:
    def __init__(self, head):
        self.head=None

    def insert_at_beg(self,data):
        node=Node(data, self.head)
        self.head=node

    def print():
        if self.head is None:
            print("its empty")
            return 
        itr = self.head
        linkedstr=[]
        while itr:
            itr=itr.next #iterate through whole LL
        print(linkedstr)

---------------------------------


    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data,None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

------------------------------------

    def insert_index(self, data, index):
        if index<0 or index > len(LinkedList):
            raise Exception("invalid index")

        if index == 0:
            self.inser_at_beg(data)
            return 

        count=0
        itr=self.head
        while itr:
            if count = index-1:
                node=Node(data, itr.next)
                break
            itr=itr.next
            count+=1

----------------------------------------
    linked=LinkedList()
    linked=#mention the function
    linked.print()
    #above functions 
    # insert_index
    # insert_at_end
    # insert_at_beg



    




#Binary search tree




            

         
