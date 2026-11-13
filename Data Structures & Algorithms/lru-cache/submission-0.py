class Node:
    def __init__(self,key:int=0,val: int=0,prev=None,next=None):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}

        self.head=Node()
        self.tail=Node()
        self.head.next=self.tail
        self.tail.prev=self.head
    
    def _remove(self,node :Node):
        node_prev=node.prev
        node_next=node.next
        node_prev.next=node_next
        node_next.prev=node_prev
    
    def _add(self,node: Node):
        next_node=self.head.next
        self.head.next=node
        node.next=next_node
        node.prev=self.head
        next_node.prev=node


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self._remove(self.cache[key])
        self._add(self.cache[key])
        return self.cache[key].val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
           node=self.cache[key]
           node.val=value
           self._remove(node)
           self._add(node)
        else:
            if len(self.cache)>=self.capacity:
                lru=self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]
            
            node=Node(key,value)
            self.cache[key]=node
            self._add(node)
            


        
