# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self, data):
        if data == self.data:
            return
        
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
                
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
        
    def search(self, val):
        if self.data == val:
            return True
            
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
            
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
    
    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        
        elements.append(self.data)
        
        if self.right:
            elements += self.right.in_order_traversal()
            
        return elements
        
    def pre_order_traversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.pre_order_traversal()
            
        if self.right:
            elements += self.right.pre_order_traversal()
            
        return elements
        
    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.pre_order_traversal()
            
        if self.right:
            elements += self.right.pre_order_traversal()
            
        elements.append(self.data)
            
        return elements
        
    def find_min(self):
        if not self.left:
            return self.data
            
        else:
            self.left.find_min()
            
    def find_max(self):
        if not self.right:
            return self.data
            
        else:
            self.right.find_max()
            
    def calculate_sum(self):
        sum = 0
        sum += self.data
        if self.left:
            sum += self.left.calculate_sum()
        if self.right:
            sum += self.right.calculate_sum()
        return sum
            
        
def build_tree(elements):
    print("\nBuilding tree with these elements: ", elements)
    root = BinarySearchTreeNode(elements[0])
    
    for i in range(1, len(elements)):
        root.add_child(elements[i])
        
    return root
    
countries = ["India", "Pakistan", "Germany", "USA", "China", "India", "UK", "USA"]
country_tree = build_tree(countries)
print("Inorder Traversal: ", country_tree.in_order_traversal())

nums = [11,2,44,56,677,53,64,2,11,44]
nums_tree = build_tree(nums)
print("Inorder Traversal: ", nums_tree.in_order_traversal())
print("\n", nums_tree.pre_order_traversal())
print("\n", nums_tree.post_order_traversal())
print("\n", nums_tree.calculate_sum())