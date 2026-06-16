class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

class BinaryTree:
    #inorder traverasal
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data,end=" ")
            self.inorder(root.right)
    
    #postorder traversal
    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end=" ")
    
    #preorder traversal
    def preorder(self,root):
        if root:
            print(root.data,end=" ")
            self.postorder(root.left)
            self.postorder(root.right)
            
bt=BinaryTree()
root=Node(10)
root.left=Node(20)
root.right=Node(30)
root.left.left=Node(40)
root.left.right=Node(50)

print("Inorder Traversal:")
bt.inorder(root)

print("\nPreorder Traversal:")
bt.preorder(root)

print("\nPostorder Traversal:")
bt.postorder(root)
