class BinaryTree:
    def _init_(self,data):
        self.data=data
        self.left=None
        self.right=None
    def add_data(self,data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_data(data)
            else:
                self.left=BinaryTree(data)
        else:
            if self.right:
                self.right.add_data(data)
            else:
                self.right=BinaryTree(data)
    def preorder_traversal(self):
        e=[self.data]
        if self.left:
            e+=self.left.preorder_traversal()
        if self.right:
            e+=self.right.preorder_traversal()
        return e
    def inorder_traversal(self):
        e=[]
        if self.left:
            e+=self.left.inorder_traversal()
        e.append(self.data)
        if self.right:
            e+=self.right.inorder_traversal()
        return e
    def postorder_traversal(self):
        e=[]
        if self.left:
            e+=self.left.postorder_traversal()
        if self.right:
            e+=self.right.postorder_traversal()
        e.append(self.data)
        return e
    def buildtree(n):
        root=BinaryTree(n[0])
        for i in range(1,len(n)):
            root.add_data(n[i])
        return root
    def search(self,val):
        if self.data == val :
            return True
        if self.data > val:
            if self.left :
                return self.left.search(val)
            else:
                return False
        if self.data < val:
            if self.right :
                return self.right.search(val)
            else:
                return False
    def maxtree(self):
        if self.right is None:
            return self.data
        return self.right.maxtree()
    def mintree(self):
        if self.left is None:
            return self.data
        return self.left.mintree()
            
n=[55,25,86,75,69,1,53,62,10,0]
ntree=BinaryTree.buildtree(n)
print(ntree.preorder_traversal())
print(ntree.inorder_traversal())
print(ntree.postorder_traversal())
print(ntree.search(10))
print(ntree.maxtree())
print(ntree.mintree())
