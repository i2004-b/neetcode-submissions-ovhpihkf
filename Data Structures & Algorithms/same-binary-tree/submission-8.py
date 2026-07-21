# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        p_stack = []
        if p:
            p_stack.append(p)
        
        q_stack = []
        if q:
            q_stack.append(q)
        
        while p_stack and q_stack:
            node_p = p_stack.pop()
            node_q = q_stack.pop()

            if node_p.val != node_q.val:
                return False

            if node_p.right and node_q.right:
                p_stack.append(node_p.right)
                q_stack.append(node_q.right)
            elif (node_p.right and not node_q.right) or (not node_p.right and node_q.right):
                return False
            
            if node_p.left and node_q.left:
                p_stack.append(node_p.left)
                q_stack.append(node_q.left)
            elif (node_p.left and not node_q.left) or (not node_p.left and node_q.left):
                return False
            
        
        return True if not p_stack and not q_stack else False

