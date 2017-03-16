#!/usr/local/bin/python3

# From Joe James Youtube tutorial: https://www.youtube.com/watch?v=YlgPi75hIBc
# users can perform the following operations
## bst = Tree()
## bst.insert(14)
## bst.preorder()
## bst.postorder()
## bst.inorder()


# Private interface
class Node:
    def __init__(self, val):
        self.value = val
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        # see if node that called function already has data
        if self.value == data:
            return False
        # see if data to be inserted is less than current node
        elif self.value > data:
            # if is larger, add a left node
            if self.leftChild:
                return self.leftChild.insert(data)
            # if no left child, add the node
            else:
                self.leftChild = Node(data)
                return True
        else:
            # if data to be inserted is greater than current node, insert into right child
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True

    def find(self, data):
        # if the data exists, then great
        if(self.value == data):
            return True
        # is data smaller than current nodes value?
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.find(data)
            # no, because it doesnt exist
            else:
                return False
        # If the value is greater than the current node, look in right node
        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False

    def preorder(self):
        if self:
            print(str(self.value))
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()

    def postorder(self):
        if self:
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print(str(self.value))

    def inorder(self):
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print(str(self.value))
            if self.rightChild:
                self.rightChild.inorder()


# Public interface
class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        # accepts a piece of data to insert
        if self.root:
            # see if root node exists - means at least one node does
            # call recursive funct to insert node
            return self.root.insert(data)
        else:
            # does not exist, so add it
            self.root = Node(data)
            return True

    def find(self, data):
        if self.root:
            return self.root.find(data)
        # if no root node, data is not in tree
        else:
            return False

    def preorder(self):
        print("PreOrder")
        self.root.preorder()

    def postorder(self):
        print("PostOrder")
        self.root.postorder()

    def inorder(self):
        print("InOrder")
        self.root.inorder()


bst = Tree()
print(bst.insert(10))
bst.insert(14)
bst.insert(28)
bst.insert(99)
bst.preorder()
bst.postorder()
bst.inorder()
