# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # BFS Solution --> need two queues
        p_queue = deque()
        q_queue = deque()

        p_queue.append(p)
        q_queue.append(q)

        while p_queue and q_queue:
            # Pop the nodes from both array
            p_node, q_node = p_queue.popleft(), q_queue.popleft()

            if not p_node and not q_node:
                continue
            elif not p_node or not q_node or p_node.val != q_node.val:
                return False

            # Add nodes to the queues
            p_queue.append(p_node.left)
            q_queue.append(q_node.left)
            p_queue.append(p_node.right)
            q_queue.append(q_node.right)

        return True