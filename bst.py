class TreeNode:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class BinarySearchTree:
  def __init__(self):
    self.root = None

  # TODO: Finish node value insertion method
  def insert_value(self, value, current_node=False):
    pass

  # TODO: Finish iterative search method
  def search_iteratively(self, value):
    pass

  # TODO: Finish recursive search method
  def search_recursively(self, value, current_node=None):
    pass

tree = BinarySearchTree()
print(tree.root)                          # None

# 1. Test node value insertion
tree.insert_value(10)
tree.insert_value(5)
tree.insert_value(16)
tree.insert_value(1)
tree.insert_value(7)
tree.insert_value(16)
# print(tree.root.value)                    # 10
# print(tree.root.left.value)               # 5
# print(tree.root.right.value)              # 16
# print(tree.root.left.left.value)          # 1
# print(tree.root.left.right.value)         # 7
# print(tree.root.right.right.value)        # 16

# 2. Test iterative search
empty_tree = BinarySearchTree()
# print(empty_tree.search_iteratively(10))  # False
# print(tree.search_iteratively(10))        # True
# print(tree.search_iteratively(7))         # True
# print(tree.search_iteratively(-1))        # False

# 3. Test recursive search
# print(empty_tree.search_recursively(10))  # False
# print(tree.search_recursively(10))        # True
# print(tree.search_recursively(7))         # True
# print(tree.search_recursively(-1))        # False
