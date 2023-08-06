class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        self.root = self._insert_recursively(self.root, key)
    
    def _insert_recursively(self, node, key):
        if node is None:
            return TreeNode(key)
        
        if key < node.key:
            node.left = self._insert_recursively(node.left, key)
        else:
            node.right = self._insert_recursively(node.right, key)
        
        return node
    
    def search(self, key):
        return self._search_recursively(self.root, key)
    
    def _search_recursively(self, node, key):
        if node is None or node.key == key:
            return node
        
        if key < node.key:
            return self._search_recursively(node.left, key)
        else:
            return self._search_recursively(node.right, key)
    
    def delete(self, key):
        self.root = self._delete_recursively(self.root, key)
    
    def _delete_recursively(self, node, key):
        if node is None:
            return node
        
        if key < node.key:
            node.left = self._delete_recursively(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursively(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            min_right_subtree = self._find_min(node.right)
            node.key = min_right_subtree.key
            node.right = self._delete_recursively(node.right, min_right_subtree.key)
        
        return node
    
    def _find_min(self, node):
        while node.left:
            node = node.left
        return node
    
    def in_order_traversal(self):
        result = []
        self._in_order_traversal_recursively(self.root, result)
        return result
    
    def _in_order_traversal_recursively(self, node, result):
        if node:
            self._in_order_traversal_recursively(node.left, result)
            result.append(node.key)
            self._in_order_traversal_recursively(node.right, result)


bst = BinarySearchTree()

# A)
elements_to_insert = [5, 2, 8, 1, 3]
for element in elements_to_insert:
    bst.insert(element)

# b)
search_key = 3
search_result = bst.search(search_key)
if search_result:
    print(f"Element {search_key} found in the tree.")
else:
    print(f"Element {search_key} not found in the tree.")

# c)
delete_key = 2
bst.delete(delete_key)
print(f"Element {delete_key} deleted from the tree.")

# d)
print("In-order traversal of the tree:", bst.in_order_traversal())
