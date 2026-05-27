# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Stack initialized with the root
        stack = [root]
        # Stack initialized with False to represent how many times the node has been visited
        visit = [False]
        # Array to track the order
        traversal = []

        # Iterate while the stack is non empty
        while stack:
            # Pop the top of the stack and the visit stack
            curr, v = stack.pop(), visit.pop()

            # Check if curr is non NULL and only do operations if that is the case
            if curr:
                # Check to see if the node has been visited twice
                if v:
                    traversal.append(curr.val)
                else:
                    # Append curr back to the stack
                    stack.append(curr)
                    # Append the value of True to the visit stack
                    visit.append(True)
                    # Add the children and he booleans saying that they have not been visited twice to the stack
                    # Add the right child first because you want to check the left child, so need to pop it before the right child
                    stack.append(curr.right)
                    visit.append(False)
                    stack.append(curr.left)
                    visit.append(False)

        # Return the traversal array
        return traversal
