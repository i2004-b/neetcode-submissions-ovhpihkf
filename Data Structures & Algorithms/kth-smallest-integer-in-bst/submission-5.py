# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1

        count = 0

        stack = []

        curr = root

        while curr or stack:
            # Iterate downward
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            count += 1
            if count == k:
                return curr.val
            # Set to the right
            curr = curr.right

        