import pytest
from  Trees.Trees import Queue , QueueNode , BinaryTree , BST , Tnode





# Can successfully instantiate an empty tree
def test_instantiate_empty():
    tree = BinaryTree()
    actual = tree.root
    expected = None
    assert actual == expected


# Can successfully instantiate a tree with a single root node

def test_instantiate_single():
    tree = BST()
    tree.add(5)
    actual = tree.root.value
    expected = 5
    assert actual == expected

# For a Binary Search Tree, can successfully add a left child and right child properly to a node
def test_add_left_and_right_children():
    tree = BST()
    tree.add(10)
    tree.add(20)
    tree.add(5)
    assert tree.root.value == 10
    assert tree.root.left.value == 5
    assert tree.root.right.value == 20



# Can successfully return a collection from a pre-order traversal

def test_pre_order():
    tree = BST()
    tree.add(10)
    tree.add(20)
    tree.add(50)
    tree.add(30)
    tree.add(40)
    tree.add(60)

    res = tree.depth_first_pre_order()
    actual = res
    expected = [10,20,50,30,40,60]
    assert actual == expected


def test_in_order():
    tree = BST()
    tree.add(10)
    tree.add(20)
    tree.add(50)
    tree.add(30)
    tree.add(40)
    tree.add(60)

    res = tree.depth_first_in_order()
    actual = res
    expected = [10,20,30,40,50,60]
    assert actual == expected




def test_post_order():
    tree = BST()
    tree.add(10)
    tree.add(20)
    tree.add(50)
    tree.add(30)
    tree.add(40)
    tree.add(60)

    res = tree.depth_first_post_order()
    actual = res
    expected = [40,30,60,50,20,10]
    assert actual == expected



# Returns true	false for the contains method, given an existing or non-existing node value

def test_contains():
    tree = BST()
    tree.add(10)


    res = tree.contains(10)
    actual = res
    expected = True
    assert actual == expected

def test_contains2():
    tree = BST()
    tree.add(10)


    res = tree.contains(99999)
    actual = res
    expected = False
    assert actual == expected