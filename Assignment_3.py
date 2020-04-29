# A binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Print all keys in the B-Tree in increasing order
def print_tree(root):

    if root is None:
        return

    # Recurse for left subtree first
    print_tree(root.left)

    # Print root's value
    print root.value

    # Recurse for right subtree
    print_tree(root.right)


# Search a given key in BST + print search path
def search(root, key):

    if root is not None:
        print root.value

    # Base Cases: root is null or key is present at root
    if root is None or root.value == key:
        if root is None:
            print("The tree does not contain the value")
            return
        else:
            return root

    # Key is greater than root's key
    if key > root.value:
        return search(root.right, key)

    # Key is smaller than root's key
    return search(root.left, key)


# Test
root = Node(100)
root.left = Node(90)
root.right = Node(110)
root.left.left = Node(80)
root.left.right = Node(95)

# Print tree
print("Print tree values in accending order:")
print_tree(root)

print("\n-------- Search section -------------")
value_to_find = eval(raw_input("Insert a value to find:"))
# Search
search(root, value_to_find)
