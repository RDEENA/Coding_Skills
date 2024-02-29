class Node:
     def __init__(self,data):
         self.data = data
         self.left = None
         self.right = None
def insert(root,data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left,data)
    elif data > root.data:
        root.right = insert(root.right,data)
    else:
        pass
    return root
def inorder(root):
    res = []
    if root:
        res = inorder(root.left)
        res.append(root.data)
        res = res + inorder(root.right)
    return res
def preorder(root):
    res = []
    if root:
        res.append(root.data)
        res = res + preorder(root.left)
        res = res + preorder(root.right)
    return res
def postorder(root):
    res = []
    if root:
        res = postorder(root.left)
        res = res + postorder(root.right)
        res.append(root.data)
    return res
root = None
root = insert(root, 27)
root = insert(root, 14)
root = insert(root, 35)
root = insert(root, 10)
root = insert(root, 19)
root = insert(root, 31)
root = insert(root, 42)
print(inorder(root))
print(preorder(root))
print(postorder(root))