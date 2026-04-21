# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Create list containing all levels to return
        levels = []

        # Create queue to hold nodes to visit
        queue = deque()

        # Add the root
        if root:
            queue.append(root)

        # Iterate through the tree
        while len(queue) > 0:
            # Create a list to store each level
            level = []
            # Iterate through items already in the queue
            for _ in range(len(queue)):
                # Pop the frontmost element
                curr = queue.popleft()
                # Add the value of the node to the level list
                level.append(curr.val)

                # Add the children of the node to the queue
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            # Append the smaller list to the list of all levels
            levels.append(level)

        # Return all levels
        return levels