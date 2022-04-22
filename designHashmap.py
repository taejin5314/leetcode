class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.nxt = None
        return
    
class MyHashMap:

    def __init__(self):
        self.bucket_size = 997 # Prime Number less than 1000
        self.bucket = [None] * self.bucket_size
        return

    def hashedKey(self, key: int) -> int:
        return key % self.bucket_size
    
    def put(self, key: int, value: int) -> None:
        
        head = self.bucket[self.hashedKey(key)]
        
        # If bucket is empty add new key-value pair to the bucket
        if not head:
            
            self.bucket[self.hashedKey(key)] = Node(key, value)
            
        else:
            
            # Replace the value if the key is already present
            # Same as editing a node in the link list
            curr = head
            prev = None
            while curr:
                if curr.key == key:
                    curr.val = value
                    break
                prev = curr
                curr = curr.nxt
            else: # If key is not present, add new key-value pair
                prev.nxt = Node(key, value)
                    
            
        return
        

    def get(self, key: int) -> int:
        
        head = self.bucket[self.hashedKey(key)]
       
        # if bucket is not empty
        if head:
            
            # Look for key in the bucket
            # Same as finding a Node from link-list
            curr = head
            while curr:
                if curr.key == key:
                    return curr.val
                curr = curr.nxt
                
        return -1
        
    def remove(self, key: int) -> None:
        
        head = self.bucket[self.hashedKey(key)]
        
        # if bucket is not empty
        if head:
            
            # Look for key in the bucket, and remove accordingly
            # Same as removing a node from link-list
            curr = head
            prev = None
            while curr:
                if curr.key == key:
                    if prev:
                        prev.nxt = curr.nxt
                    else:
                        head = curr.nxt
                    break
                prev = curr
                curr = curr.nxt
            
            # Re-Assign Head to bucket
            self.bucket[self.hashedKey(key)] = head
                
        return