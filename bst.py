#binary search tree 
#create a class BST and an instance of it 
class BST:
    def __init(self,root,left,right):
        self.root=root
        self.right=right
        self.left=left

    #basic add function
    def add_to_bst(self, data):
        if data==self.data:
            return

        if data<self.data:
            if self.left:
                self.left.add_to_bst(data)

        if data>self.data:
            if self.right:
                self.right.add_to_bst(data)


    #inorder traversal
    def in_order_traversal(self):
        list=[]
        if self.left:
            list+= self.left.in_order_traversal()
        list.append(self.data)
        if self.right:
            list+=self.right.in_order_traversal()
    #postorder traversal 
    def post_order_traversal(self):
        #since list is defined no need again
        if self.left:
            list+=self.left.post_order()
            list.append(self.data)
        if self.right:
            list+=self.right.post_order_traversal()
        #come to root
        list.append(self.root.data)


    def search(self,value,root):
        if value==root:
            return value
        elif value<root:
            self.search(value, root.left)
        else:
            self.search(value,root.right)


#mention the list since its declared empty 
            
