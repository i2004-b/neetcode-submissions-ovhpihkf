# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # Serialize using DFS --> O(n)
        # Use preorder traversal to make the serialization

        # Create a list to hold the result
        res = []

        # Create a helper dfs function
        def dfs(root):
            # Base case: if the root does not exist, append "N" to the list and return
            if not root:
                res.append("N")
                return

            # Add the root value as a string to the result list
            res.append(str(root.val))
            # Run dfs on the left and the right
            dfs(root.left)
            dfs(root.right)

        # Call dfs
        dfs(root)
        # Return res joined as a string
        return ",".join(res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # Extract the data string into an array
        vals = data.split(",")
        # Declare a member variable that will serve as a pointer to iterate through the array
        self.i = 0

        # Declare a dfs function to create the tree (no input needed)
        def dfs():
            # Base case: if you hit a Null node, increment the pointer and return None
            if vals[self.i] == "N":
                self.i += 1
                return None

            # If the node is not null, create the TreeNode and increment the counter
            # Make sure to convert the string to an integer
            node = TreeNode(int(vals[self.i]))
            self.i += 1

            # Call dfs to construct and connect the left and the right subtrees
            node.left = dfs()
            node.right = dfs()

            # Return the completed node
            return node

        # Call and return the value from dfs
        return dfs()
