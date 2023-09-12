class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def findClosestPerfumes(root, budget):
    closest_lower = None
    closest_higher = None  
    def inorderTraversal(node):
        nonlocal closest_lower, closest_higher
        if node is None:
            return
        if node.value == budget:
            closest_lower = node.value
            closest_higher = node.value
            return
        if node.value < budget:
            if closest_lower is None or budget - node.value < budget - closest_lower:
                closest_lower = node.value
            inorderTraversal(node.right)
        else:
            if closest_higher is None or node.value - budget < closest_higher - budget:
                closest_higher = node.value
            inorderTraversal(node.left)
    inorderTraversal(root)
    return closest_lower, closest_higher
n = int(input())
root_price = int(input())
other_prices = [int(i) for i in input().split()]
budget = int(input())
root = TreeNode(root_price)
for price in other_prices:
    current = root
    while True:
        if price < current.value:
            if current.left is None:
                current.left = TreeNode(price)
                break
            current = current.left
        else:
            if current.right is None:
                current.right = TreeNode(price)
                break
            current = current.right

closest_lower, closest_higher = findClosestPerfumes(root, budget)
print(closest_lower, closest_higher)
