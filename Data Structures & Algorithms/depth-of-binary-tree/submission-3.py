# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque()
        queue.append(root)
        level = 0

        while queue:
            level += 1
            # Pop from the queue
            for _ in range(len(queue)):
                node = queue.popleft()

                # Add values of left and right if not null
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return level