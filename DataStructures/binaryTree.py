#Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

def traversal(root):
    if root == None:
        return

    traversal(root.left)
    print(root.val)
    traversal(root.right)
finish = False
def addNode(root,node):
    global finish
    if root == None:
        root = TreeNode(node.val)
        return
    print(root.val,node.val)
    if finish == False and root.left == None:
        print("add to left")
        root.left = TreeNode(node.val)
        finish = True
        return
    if finish == False and root.right == None:
        print("add to right")
        root.right = TreeNode(node.val)
        finish = True
        return
    print("to left")
    addNode(root.left,node)
    print("to right")
    addNode(root.right,node)

def buildTestBST(data):
    global finish
    if data == None:
        return None
    root = TreeNode(data[0])
    for i in range(1,len(data)):
        finish = False
        addNode(root,TreeNode(data[i]))
    return root
tree = buildTestBST([4,2,6,1,3])
print("dump tree")
traversal(tree)