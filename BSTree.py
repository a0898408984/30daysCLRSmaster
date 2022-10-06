import argparse

class Node():
    #########################
    # DO NOT MODIFY CODES HERE
    # DO NOT MODIFY CODES HERE
    # DO NOT MODIFY CODES HERE
    # It's important and repeat three times
    #########################
    def __init__(self, key):
        self.value = key
        self.left_child = None
        self.right_child = None
    def __repr__(self):
        return str(self.value)

class BS_tree():
    def __init__(self):
        self.root = None
        self.size = 0
    def inorder(self, output):      # print the in-order traversal of binary search tree
        # Todo
        self.inorder_recur(self.root, output)
        output.write("\n")

    def inorder_recur(self, node, output):
        if node != None:
            self.inorder_recur(node.left_child, output)
            output.write(str(node.value) + " ")
            self.inorder_recur(node.right_child, output)

    def preorder(self, output):     # print the pre-order traversal of binary search tree
        # Todo
        self.preorder_recur(self.root, output)
        output.write("\n")

    def preorder_recur(self, node, output):
        if node != None:
            output.write(str(node.value) + " ")
            self.preorder_recur(node.left_child, output)
            self.preorder_recur(node.right_child, output)

    def postorder(self, output):    # print the post-order traversal of binary search tree
        # Todo
        self.postorder_recur(self.root, output)
        output.write("\n")

    def postorder_recur(self, node, output):
        if node != None:
            self.postorder_recur(node.left_child, output)
            self.postorder_recur(node.right_child, output)
            output.write(str(node.value) + " ")

    def find_max(self, output):     # print the maximum number in binary search tree
        # Todo
        node = self.root
        while(node.right_child != None):
            node = node.right_child
        output.write(str(node.value) + "\n")

    def find_min(self, output):     # print the minimum number in binary search tree
        # Todo
        node = self.root
        while(node.left_child != None):
            node = node.left_child
        output.write(str(node.value) + "\n")

    def insert(self, key):          # insert one node
        # Todo
        newnode = Node(key)
        node = self.root
        if node == None:
            self.root = newnode
            return
        prev = None
        while node != None:
            prev = node
            if key > node.value:
                node = node.right_child
            elif key <= node.value:
                node = node.left_child
        if key > prev.value:
            prev.right_child = newnode
        elif key <= prev.value:
            prev.left_child = newnode
        self.size += 1


    def delete(self, key):          # delete one node
        # Todo
        prev = None
        node, prev = self.finds(self.root, prev, key)
        if node == None:
            return
        self.size -= 1
        if node.left_child == None:
            if prev == None:
                self.root = node.right_child
            else:
                if prev.left_child != None:
                    if prev.left_child.value == key:
                        prev.left_child = node.right_child
                if prev.right_child != None:
                    if prev.right_child.value == key:
                        prev.right_child = node.right_child
            return
        if node.right_child == None:
            if prev == None:
                self.root = node.left_child
            else:
                if prev.left_child != None:
                    if prev.left_child.value == key:
                        prev.left_child = node.left_child
                if prev.right_child != None:
                    if prev.right_child.value == key:
                        prev.right_child = node.left_child
            return
        minnode = node.right_child
        minprev = None
        while (minnode.left_child != None):
            minprev = minnode
            minnode = minnode.left_child
        if minprev != None:
            minprev.left_child = minnode.right_child
        if prev != None:
            if prev.left_child != None:
                if prev.left_child.value == key:
                    prev.left_child = minnode
            if prev.right_child != None:
                if prev.right_child.value == key:
                    prev.right_child = minnode
        else:
            self.root = minnode
        minnode.left_child = node.left_child
        if minprev != None:
            minnode.right_child = node.right_child

    def finds(self, node, prev, key):
        try:
            if node.value == None:
                return None, None
        except:
            pass
        if node != None:
            if key == node.value:
                return node, prev
            elif key > node.value:
                return self.finds(node.right_child, node, key)
            elif key < node.value:
                return self.finds(node.left_child, node, key)
        else:
            return None, None

    def level(self, output):        # print the height of binary search tree(leaf = 0)
        # Todo
        if self.root == None:
            return output.write(str(0) + "\n")
        output.write(str(self.level_recur(self.root)) + "\n")

    def level_recur(self, node):
        if node == None:
            return -1
        return max(self.level_recur(node.left_child),
                self.level_recur(node.right_child)) + 1


    def internalnode(self, output): # print the internal node in binary search tree from the smallest to the largest
        # Todo
        self.inter_recur(self.root, output)
        output.write("\n")

    def inter_recur(self, node, output):
        if node != None:
            if (node.left_child == None) and (node.right_child == None):
                return
            else:
                self.inter_recur(node.left_child, output)
                output.write(str(node.value) + " ")
                self.inter_recur(node.right_child, output)

    def leafnode(self, output):     # print the leafnode in BST from left to right
        # Todo
        self.leaf_recur(self.root, output)
        output.write("\n")

    def leaf_recur(self, node, output):
        if node != None:
            if node.left_child == None and node.right_child == None:
                output.write(str(node.value) + " ")
                return
            else:
                self.leaf_recur(node.left_child, output)
                self.leaf_recur(node.right_child, output)

    def main(self, input_path, output_path):
        #########################
        # DO NOT MODIFY CODES HERE
        # DO NOT MODIFY CODES HERE
        # DO NOT MODIFY CODES HERE
        # It's important and repeat three times
        #########################
        output = open(output_path, 'w')
        with open(input_path, 'r', newline='') as file_in:
            f = file_in.read().splitlines()
            for lines in f:
                if lines.startswith("insert"):
                    value_list = lines.split(' ')
                    for value in value_list[1:]:
                        self.insert(int(value))
                if lines.startswith('inorder'):
                    self.inorder(output)
                if lines.startswith('preorder'):
                    self.preorder(output)
                if lines.startswith('postorder'):
                    self.postorder(output)
                if lines.startswith('max'):
                    self.find_max(output)
                if lines.startswith('min'):
                    self.find_min(output)
                if lines.startswith('delete'):
                    value_list = lines.split(' ')
                    self.delete(int(value_list[1]))
                if lines.startswith('level'):
                    self.level(output)
                if lines.startswith('internalnode'):
                    self.internalnode(output)
                if lines.startswith('leafnode'):
                    self.leafnode(output)
        output.close()
if __name__ == '__main__' :
    #########################
    # DO NOT MODIFY CODES HERE
    # DO NOT MODIFY CODES HERE
    # DO NOT MODIFY CODES HERE
    # It's important and repeat three times
    #########################
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, default = './input_3.txt',help="Input file root.")
    parser.add_argument("--output", type=str, default = './output_3.txt',help="Output file root.")
    args = parser.parse_args()

    BS = BS_tree()
    BS.main(args.input, args.output)



