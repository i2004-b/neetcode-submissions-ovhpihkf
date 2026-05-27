# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Have a queue to keep track of the levels
        queue = deque()

        # Base Case: Check that the root exists and if so add to queue
        if root:
            queue.append(root)

        # Iterate while the queue is non empty
        while queue:
            # Pop left from the queue
            curr = queue.popleft()
            # Flip the children of curr
            curr.left, curr.right = curr.right, curr.left
            # Add the children to the queue if non-Null
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

        # Return the root
        return root