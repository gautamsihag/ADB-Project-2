class TreeNode:
    left = None
    center = None
    right = None
    classification = None
    data = 0
    parent = None
    
    def __init__(self, data, specificity, classification, parent):
        self.center = None
        self.left = None
        self.classification = classification
        self.data = data
        self.parent = parent
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
    
    def newNode(self, data, specificity, classification, parent):
        return TreeNode(data, specificity, classification, parent)
    
    def insertLeft(self, root, data, parent, classification):
        if root == None:
            return self.newNode(data, 1, classification, parent)
        else:
            root.left = self.insertLeft(self.left, data, root, classification)
            return root
    
    def insertRight(self, root, data, parent, classification):
        if root == None:
            return self.newNode(data, 1, classification, parent)
        else:
            root.right = self.insertRight(root.right, data, root, classification)
            return root
    
    def insertCenter(self, root, data, parent, classification):
        if root == None:
            return self.newNode(data, 1, classification, parent)
        else:
            root.center = self.insertCenter(root.center, data, root, classification)
            return root
    
    def maxDepth(self, root):
        if root == None:
            return 0
        else:
            leftdepth = self.maxDepth(root.left)
            centerdepth = self.maxDepth(root.center)
            rightdepth = self.maxDepth(root.right)
            return max(leftdepth, rightdepth, rightdepth) + 1
    
    def size(self, root):
        if root == None:
            return 0
        else:
            return self.size(root.left) + self.size(root.center) + self.size(root.right) + 1
            
    def isLeaf(self, root):
        if root.left == None and root.right == None and root.center == None:
            return True
        else:
            return False