# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Declare a queue to store each level
        queue = deque()
        # Make a list that will hold the rightmost elements
        right = []

        # Add the root, making sure it is not null
        if root:
            queue.append(root)

        # Iterate while queue is non-empty to go through all the levels in the tree
        while queue:
            # Iterate through each node in the level
            for i in range(len(queue)):
                # Pop the leftmost value but store it in the curr pointer
                curr = queue.popleft()

                # Check to see if curr has any children and add them to the queue (the next level)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            # Curr will be at the rightmost element in the level by now, so add the value into the right array
            right.append(curr.val)

        return right