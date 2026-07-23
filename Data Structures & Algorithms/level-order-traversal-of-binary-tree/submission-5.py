# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        # Queue to hold the level values
        queue = deque([root])
        # Array to hold the sublists for each level
        arr = []

        # Iterate while the queue is non-empty
        while queue:
            # Declare array for each level
            level = []
            # Iterate over the items in the level
            for _ in range(len(queue)):
                # Pop the value
                node = queue.popleft()
                # Add the value to the level array
                level.append(node.val)
                # Add children of the node to the queue as long as they are non-Null
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Append the level sublist to the result array
            arr.append(level)

        return arr

