class LinkedBinaryTree:
    def __init__(self, root):
        self.key = root
        self.left = None
        self.right = None
        self.parent = None

    def insert_left(self, new_node):
        if self.left is None:
            self.left = LinkedBinaryTree(new_node)
            self.left.parent = self
        else:
            t = LinkedBinaryTree(new_node)
            t.left = self.left
            self.left.parent = self
            self.left = t
            self.left.parent = self

    def insert_right(self, new_node):
        if self.right is None:
            self.right = LinkedBinaryTree(new_node)
            self.right.parent = self
        else:
            t = LinkedBinaryTree(new_node)
            t.right = self.right
            self.right.parent = self
            self.right = t
            self.right.parent = self

    def get_right(self):
        return self.right

    def get_left(self):
        return self.left

    def get_parent(self):
        return self.parent

    def set_root_val(self, obj):
        self.key = obj

    def get_root_val(self):
        return self.key
