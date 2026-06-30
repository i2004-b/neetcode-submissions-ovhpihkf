# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Iterative solution
        # T: O(n), S: O(n)

        # If the root does not exist, return false
        if not root:
            return False

        # Intialize a stack that will hold tuples with the node and the sum at that point
        stack = [(root, targetSum - root.val)]

        # Iterate while the stack is non-empty
        while stack:
            # Pop the tuple at the top of the stack
            node, curr_sum = stack.pop()
            # Check if the node is a leafnode and if the curr_sum == 0, return True
            if not node.left and not node.right and curr_sum == 0:
                return True

            # Add the children to the node
            # Adding right child first so that you can access left child first when popping from stack
            if node.right:
                stack.append((node.right, curr_sum - node.right.val))
            if node.left:
                stack.append((node.left, curr_sum - node.left.val))

        # If it didn't return True within the loop, there is no path
        return False