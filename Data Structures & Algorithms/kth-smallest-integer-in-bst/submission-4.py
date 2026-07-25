# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Declare member variable to hold the count
        self.count = 0
        self.k = k
        self.val = 0

        def inorder(root):
            if not root:
                return

            # Go left
            inorder(root.left)
            # Increment count by 1
            self.count += 1
            # Return the value if the kth biggest
            if self.count == self.k:
                self.val = root.val
            # Go right
            inorder(root.right)

        # Run helper function
        inorder(root)
        return self.val