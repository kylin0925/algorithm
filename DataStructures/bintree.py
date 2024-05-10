#
#
#
class node():
	left = None
	right = None
	value = None
	
def find_node(nd,n):
	print n
	if n > nd.value:
		if(nd.right!=None):
			find_node(nd.right,n)
		else:
			print "add in right"
			tmp = node()
			tmp.value = n
			nd.right = tmp
	else:
		if nd.left != None:
			find_node(nd.left,n)
		else:
			print "add in left"
			tmp = node()
			tmp.value = n
			nd.left = tmp
			
def insert(tree,n):
	if tree == None:
		tmp = node()
		tmp.value = n
		tree = tmp
		print "tree ",tree.value
		return
	if tree.value >= n:
		print "to left ",tree.left
		insert(tree.left,n)
		print tree.left.value
	elif tree.value < n:
		print "to right ",tree.right
		insert(tree.right,n)
def dump(nd):
	
	if nd.left!=None:
		dump(nd.left)
	print nd.value
	if nd.right != None:
		dump(nd.right)
		
def add_node(root,n):
	app_node = find_node(root,n)
	
root = node()
root.value =2
#dump(root)
#add_node(root,2)
#add_node(root,1)
#add_node(root,3)
#add_node(root,0)
#add_node(root,-1)
#insert(root,2)
insert(root,1)
#insert(root,3)
#insert(root,0)
#insert(root,-1)
print "dump ::"
dump(root)
print "===== dump end =========="