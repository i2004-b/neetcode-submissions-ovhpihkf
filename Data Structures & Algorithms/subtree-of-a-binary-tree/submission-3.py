# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Iterative solution
        if not subRoot:
            return True
        if not root:
            return False

        stack = [root]

        while stack:
            node = stack.pop()
            if self.same(node, subRoot):
                return True

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            

        # If exiting without finding the answer return False
        return False


    def same(self, root, sub_root):
        # Check if both null
        if not root and not sub_root:
            return True
        
        # Declare stack holding tuples
        stack = [(root, sub_root)]

        # Iterate while the stack exists
        while stack:
            # Pop the value at the top of stack
            r, s = stack.pop()

            if not r and not s:
                continue
            elif not r or not s or r.val != s.val:
                return False

            stack.append((r.right, s.right))
            stack.append((r.left, s.left))

        return True