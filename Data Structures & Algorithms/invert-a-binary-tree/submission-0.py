# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Iterative BFS attempt
        # Declare a queue to hold nodes for the levels
        queue = deque()

        # Check that the root value is non-Null and add it to the queue
        if root:
            queue.append(root)

        # Iterate while the queue is non-empty
        while queue:
            # Iterate through the items in the queue
            for i in range(len(queue)):
                # Pop the left element in the queue to get the node
                curr = queue.popleft()
                # Swap the left and right children of the popped node
                curr.left, curr.right = curr.right, curr.left
                # Add children on each child to the queue if non-Null
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

        # Return the root
        return root