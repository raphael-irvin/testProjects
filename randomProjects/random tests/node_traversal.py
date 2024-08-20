class TreeNode:
    def __init__(self,data = None):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.head = TreeNode()
    
    def append(self, data):
        cur = self.head
        new_node = TreeNode(data)
        while True:

            if cur.data == None:
                cur.data = data
                return
            
            if data < cur.data:
                if cur.left == None:
                    cur.left = new_node
                    return
                if cur.left != None:
                    cur = cur.right

            if data > cur.data:
                if cur.right == None:
                    cur.right = new_node
                    return
                if cur.right != None:
                    cur = cur.right
    
    def find_data(self, data):
        cur = self.head
        while cur.right != None and cur.left != None:

            if data > cur.data:
                cur = cur.right

            if data < cur.data:
                cur = cur.left
            
            if data == cur.data:
                return print(f'Data {data} has been found.')

        return print("Im sorry, your data is not found!")

my_tree = Tree()
my_tree.append(50)
my_tree.append(100)
my_tree.append(30)
my_tree.find_data(30)