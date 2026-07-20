# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Check if the root exists
        if not root:
            return None

        # Declare a queue
        queue = deque()
        # Put the first element in the queue
        queue.append(root)

        # Iterate while queue exists
        while queue:
            # Pop from queue
            node = queue.popleft()
            # Swap the left and right children
            node.left, node.right = node.right, node.left
            # Put back into queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root