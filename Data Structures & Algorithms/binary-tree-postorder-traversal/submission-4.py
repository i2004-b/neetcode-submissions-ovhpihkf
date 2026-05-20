# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Initialize stack of visited nodes with the root
        stack = [root]
        # Initialize stack of whether or not the node has been visited twice with False
        visit = [False]
        # Declare list to hold result values
        res = []

        # Iterate while the stack is non-empty
        while stack:
            # Pop from both stacks
            curr, v = stack.pop(), visit.pop()

            # Check if curr is non Null (if curr is NULL, nothing will happen)
            if curr:
                # Check whether or not the node was visited
                # If visited, add it to res
                if v:
                    res.append(curr.val)
                else:
                    # Add back the node if not visited and update the boolean to be True
                    stack.append(curr)
                    visit.append(True)
                    # Add the children of the node curr is at
                    # Add the right first because want to visit left before
                    stack.append(curr.right)
                    visit.append(False)
                    stack.append(curr.left)
                    visit.append(False)

        # Return res
        return res
            
