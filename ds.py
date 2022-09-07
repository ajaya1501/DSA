# #create a basic stack push and pop elements into it 
# # create an empty list called stack
# stack = []  #initialise an empty one 
# stack.append(1)
# stack.append(2)
# stack.append(3)
# print(stack)
# stack.pop()
# stack.pop()
# stack.pop()




# #Queue operations on a simple note using collections module 
# from collections import deque
# # Initializing a queue
# q = deque()
# # Adding elements to a queue
# q.append('a')
# q.append('b')
# q.append('c') 
# print("Initial queue")
# print(q)
# # Removing elements from a queue
# print("\nElements dequeued from the queue")
# print(q.popleft())
# print(q.popleft())
# print("\nQueue after removing elements")
# print(q)





#Create a basic singly linked list 
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

            

         
