from pythonds3.trees import BinaryTree

def build_tree():
    return ["a", ["b", [], ["d"]], ["c", ["e"], ["f"]]]

def build_tree_ref():
    t = BinaryTree("a")
    t.insert_left("b")
    t.get_left_child().insert_right("d")
    t.insert_right("c")
    t.get_right_child().insert_right("f")
    t.get_right_child().insert_left("e")
    return t
