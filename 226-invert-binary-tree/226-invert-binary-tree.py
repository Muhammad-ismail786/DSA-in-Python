# Step 1: TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Step 2: Solution class
class Solution:
    def invertTree(self, root):

        if root is None:
            return None

        # Swap left and right children
        root.left, root.right = root.right, root.left

        # Recursively invert left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


# Step 3: Tree print function
def print_tree(root):

    if root is not None:

        print(root.val, end=" ")

        print_tree(root.left)
        print_tree(root.right)


# Step 4: Main function
def main():

    # Create root node
    root = TreeNode(4)

    # Create child nodes
    node2 = TreeNode(2)
    node7 = TreeNode(7)

    node1 = TreeNode(1)
    node3 = TreeNode(3)
    node6 = TreeNode(6)
    node9 = TreeNode(9)

    # Connect root children
    root.left = node2
    root.right = node7

    # Connect node 2 children
    node2.left = node1
    node2.right = node3

    # Connect node 7 children
    node7.left = node6
    node7.right = node9

    # Print original tree
    print("Original Tree:")
    print_tree(root)

    # Invert binary tree
    solution = Solution()
    root = solution.invertTree(root)

    # Print inverted tree
    print("\nInverted Tree:")
    print_tree(root)

    print()


# Step 5: Program execution
if __name__ == "__main__":
    main()
