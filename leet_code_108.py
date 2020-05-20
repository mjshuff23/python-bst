"""
View the full problem and run the test cases at:
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
"""
from bst import TreeNode

def sortedArrayToBST(nums):
  """
  :type nums: List[int]
  :rtype: TreeNode
  """

bst_root = sortedArrayToBST([-10,-3,0,5,9])
print(bst_root.value)               # 0
# print(bst_root.left.value)          # -3
# print(bst_root.left.left.value)     # -10
# print(bst_root.right.value)         # 9
# print(bst_root.right.left.value)    # 5
# Returns the root of the following binary search tree:
#       0
#      / \
#    -3   9
#    /   /
#  -10  5
