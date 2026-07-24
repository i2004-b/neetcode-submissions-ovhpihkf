# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Check that root exists
        if not root:
            return True

        queue = deque([(root, float("-inf"), float("inf"))])

        while queue:
            # Pop from the queue
            node, left, right = queue.popleft()

            # Check that the node is within the proper range
            if not (left < node.val < right):
                return False

            # Add the children with the correct values for the bounds
            if node.left:
                queue.append((node.left, left, node.val))
            if node.right:
                queue.append((node.right, node.val, right))

        return True