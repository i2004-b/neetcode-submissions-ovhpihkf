# Need to use a doubly linked list to create be able to track when the elements appear in the cache
# Create class for such nodes
class Node:

    def __init__(self, key, val):
        self.key, self.val = key, val
        # Set the prev and next pointers to none
        self.prev = self.next = None



class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        # Create a hashmap to map the keys and their corresponding nodes
        self.cache = {}

        # Create a left and right node
        # The left node will be for the item least recently used and the right node will be for the item most recently used
        self.left, self.right = Node(0, 0), Node(0, 0)
        # Connect the left and the right pointers together so that you can insert new pointers in between both of them
        self.left.next, self.right.prev = self.right, self.left

    def insert(self, node):
        # When inserting, insert at the most recent end, which is the right
        # Insert between the last element and the second to last element
        prev, nxt = self.right.prev, self.right
        # Connect the previous and next items to the new node
        prev.next = nxt.prev = node
        # Connect the new nodes pointers as well
        node.prev, node.next = prev, nxt

    
    def remove(self, node):
        # When removing, just connect pointers over each other
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev



    def get(self, key: int) -> int:
        # This function will return the value when the key exists; if it doesn't exist, return -1
        if key in self.cache:
            # Get counts as most recently used so need to update the node
            # Update by removing it and then adding it to the end of the list (make sure you are accessing the node)
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val

        return -1
        

    def put(self, key: int, value: int) -> None:
        # This function will add the value to the end of the list because most recently used
        # First check if the key already exists (if so, delete it)
        if key in self.cache: # Don't have to remove key from hashmap as it is the same in this case
            self.remove(self.cache[key])

        # Add the value to the key in hashmap
        self.cache[key] = Node(key, value)
        # Insert the node into the DLL
        self.insert(self.cache[key])

        # Check if the capacity has been exceeded
        if len(self.cache) > self.capacity:
            # Save the least recently used item
            lru = self.left.next
            # Remove from the least recently used side
            self.remove(lru)
            # Remove also from the hashmap
            del self.cache[lru.key]

        
