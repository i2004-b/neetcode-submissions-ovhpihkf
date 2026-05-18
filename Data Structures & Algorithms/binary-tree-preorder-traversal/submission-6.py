# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Declare stack to hold visited nodes
        stack = []

        # Declare array to hold the traversal order
        vals = []

        # Have pointer to the nodes
        curr = root

        # Iterate while curr is non null or stack is non empty
        while curr or stack:
            # Iterate while curr is going down the tree
            while curr:
                # Add node to the stack
                stack.append(curr)
                # Add the value to the vals
                vals.append(curr.val)
                # Change the curr pointer
                curr = curr.left

            # Reassign curr to what is at the top of the stack
            curr = stack.pop()
            # Reassign to check the right
            curr = curr.right

        # Return vals
        return vals