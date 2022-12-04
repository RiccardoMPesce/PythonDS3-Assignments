from binary_search_tree import BinarySearchTree, TreeNode

class BinarySearchTreeUpdate(BinarySearchTree):
    def __init__(self):
        super().__init__()
    
    def _put(self, key, value, current_node):
        if key < current_node.key:
            if current_node.left_child:
                self._put(key, value, current_node.left_child)
            else:
                current_node.left_child = TreeNode(
                    key, value, parent=current_node
                )
        elif key == current_node.key:
            current_node.replace_value(
                key,
                value,
                current_node.left_child,
                current_node.right_child
            )
        else:
            if current_node.right_child:
                self._put(key, value, current_node.right_child)
            else:
                current_node.right_child = TreeNode(
                    key, value, parent=current_node
                )

if __name__ == "__main__":
    my_tree = BinarySearchTree()
    my_tree["a"] = "a"
    my_tree["q"] = "quick"
    my_tree["b"] = "brown"
    my_tree["f"] = "fox"
    my_tree["j"] = "jumps"
    my_tree["o"] = "over"
    my_tree["t"] = "the"
    my_tree["l"] = "lazy"
    my_tree["d"] = "dog"

    print(my_tree["q"])
    print(my_tree["l"])
    print("There are {} items in this tree".format(len(my_tree)))
    my_tree.delete("a")
    print("There are {} items in this tree".format(len(my_tree)))

    for node in my_tree:
        print(my_tree[node], end=" ")
    print()
