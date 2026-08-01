# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # Preorder recursive solution
        # Have an array that will hold the values
        res = []

        # Declare dfs helper function to iterate through tree
        def dfs(root):
            # Base case: if the root does not exists, append "N"
            if not root:
                res.append("N")
                return

            # Add the current root value as a string
            res.append(str(root.val))
            # Run dfs on the left and the right
            dfs(root.left)
            dfs(root.right)

        # Run dfs
        dfs(root)
        # Return the joined array
        return ",".join(res)


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # Split the data into an array of values
        vals = data.split(",")
        # Make a pointer that is a member value. This will iterate through vals
        self.i = 0

        # Create a recursive dfs function to build the tree
        def dfs():
            # The base case is when you hit "N" to return None
            # Make sure to increment the pointer as well
            if vals[self.i] == "N":
                # Increment the pointer
                self.i += 1
                # Return None
                return None

            # Create the node if not Null and make the value into an integer
            node = TreeNode(int(vals[self.i]))
            # Increment self.i
            self.i += 1
            # Run recursively to build the left and the right
            node.left = dfs()
            node.right = dfs()

            # Return back up the node
            return node

        # Call and return the value of dfs
        return dfs()

