# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # RETRY
        # Declare queue to hold the nodes of a certain level
        queue = deque()
        # Create list to hold every level
        tree = []

        # Add the root to the queue, if it exists. Also add its value to the tree array
        if root:
            queue.append(root)

        # Iterate while the queue is non-empty
        while queue:
            # Create an empty list to add the values of that particular level
            level = []
            # Iterate through the nodes in the queue (current level)
            for i in range(len(queue)):
                # Pop the node from the queue but save it whole node
                curr = queue.popleft()
                # Add the value of the node to the sublist
                level.append(curr.val)
                # Add the children (next level) to the queue
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            # Add the subarray to the main array
            tree.append(level)

        # Return the list holding all levels
        return tree