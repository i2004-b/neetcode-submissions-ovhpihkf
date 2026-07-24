# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Check that the root exists
        if not root:
            return []

        # Declare a queue initialized with the root
        queue = deque([root])
        # Have array to hold the right-side view
        right = []

        # Iterate while queue exists
        while queue:
            # Iterate through each level
            for _ in range(len(queue)):
                # Pop from the queue
                node = queue.popleft()
                # Add children if they exist
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Last value for node is the rightmost value
            # Add its value to the array
            right.append(node.val)

        return right