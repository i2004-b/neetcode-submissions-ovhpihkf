# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Alternate iterative solution where you are no tracking whether or not the node has been visited
        # With this method, you do pre-order traversal but starting with the right
        # Then at the end, you just reverse and return the list

        # Declare a stack to store values
        stack = []
        # Declare array to store the result
        res = []
        # Assign pointer to the root
        curr = root

        # Iterate while the stack is non-empty
        while curr or stack:
            # if curr
            if curr:
                res.append(curr.val)
                stack.append(curr)
                curr = curr.right
            # else
            else:
                curr = stack.pop().left



        res.reverse()
        return res
