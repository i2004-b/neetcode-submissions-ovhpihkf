# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # BFS serialize attempt
        # Go through level by level to make the string

        # Check if the root exists. If it doesn't return "N"
        if not root:
            return "N"

        # Create array to hold the result
        res = []

        # Create a queue to iterate through the tree. Initialize with the root
        queue = deque([root])

        # Iterate while the queue exists
        while queue:
            # Pop the node from the queue
            node = queue.popleft()
            # If the node does not exist, add "N" to res
            if not node:
                res.append("N")
            # If the node exists, add the value to the result and add the children to the queue
            else:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)

        # Return the joined array
        return ",".join(res)
                
            
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # Split the data string into separate characters in a list
        vals = data.split(",")

        # Check that the root exists
        if vals[0] == "N":
            return None

        # Create the root with the first value in the vals array
        root = TreeNode(int(vals[0]))

        # Create a queue initialized with root --> need this to iteratively create the tree
        queue = deque([root])

        # Create a pointer for the current index, starting at 1
        index = 1

        # Iterate while the queue exists
        while queue:
            # Pop the node from the queue
            node = queue.popleft()

            # Need to connect the node to its children
            # Check that the current value that index is pointing to (left child) is not Null
            if vals[index] != "N":
                # Connect node's left child
                node.left = TreeNode(int(vals[index]))
                # Add that node to the queue
                queue.append(node.left)
            # Increment the index
            index += 1

            # Check that the current value that the index is pointing to (right child) is not Null
            if vals[index] != "N":
                # Connect node's right child
                node.right = TreeNode(int(vals[index]))
                # Add the right child to the queue
                queue.append(node.right)
            # Increment index by 1
            index += 1

        return root

