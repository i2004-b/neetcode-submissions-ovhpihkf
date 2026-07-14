# Need to create a doubly linked node to store the order of which items were most recently seen
# Create a node class for DLL nodes
class Node:
    # Init function should set key and value; it should also set both pointers to Null
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev = self.next = None

class LRUCache:

    """
    __init__ should set the following:
        capacity
        a hashmap (to map the key to the nodes that store the values)
        left and right node pointers (left for the least recently used and right for the most recently used)
            Connect the nodes to each other: new nodes will be placed in between them
    """
    def __init__(self, capacity: int):
        self.capacity = capacity

        self.cache = {}

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    
    """
    insert is a helper function for constructing the DLL. Insert the node at the end between the second to last node and the right pointer
    Connect the new node with nodes nearby as well
    """
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt


    """
    remove is a helper function for managing the DLL. Remove the node by connecting the prev and next pointers
    """
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        
        

    """
    get should do the following:
        Check that the value exists in the hashmap:
            If it does, first remove it from the DLL and then add it back to the end as it was recently used
            Return the value of the key as well
        If not found, return -1
    """
    def get(self, key: int) -> int:
        if key in self.cache:
            # Go into the dictionary to get the node to remove
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1
        

    """
    put should do the following:
        Check that the key already exists:
            If it exists, remove the node (value)from the dictionary (no need to remove the key itself as a new node will replace its value)
        
        Insert the new node into its proper place both in the hashmap and the linked list

        Check that the capacity has not gone over:
            If it has, remove the least recently used item (use the left pointer for assistance)
    """
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            # Save the least recently used item
            lru = self.left.next
            # Remove from the DLL and the hashmap
            self.remove(lru)
            del self.cache[lru.key]
