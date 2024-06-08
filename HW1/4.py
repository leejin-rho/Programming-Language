class Tree:
	def __init__(self,value):
		self.value = value
		self.left = None
		self.right = None

def preorder(node):
	if node:
		print(node.value)
		preorder(node.left)
		preorder(node.right)
		
def inorder(node):
	if node:
		inorder(node.left)
		print(node.value)
		inorder(node.right)
		
def postorder(node):
	if node:
		postorder(node.left)
		postorder(node.right)
		print(node.value)

root = Tree(15)

root.left = Tree(1)
root.right = Tree(37)
root.left.left = Tree(61)
root.left.right = Tree(26)
root.right.left = Tree(59)
root.right.right = Tree(48)

print("Preorder Traverse")
preorder(root)
print("Inorder Traverse")
inorder(root)
print("Postorder Traverse")
postorder(root)
