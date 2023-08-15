from tree_intersection import Tnode, intersection

def test_intersection():
    t1 = Tnode(1)
    t1.left = Tnode(2)
    t1.right = Tnode(3)
    t1.left.left = Tnode(4)
    t1.left.right = Tnode(5)

    t2 = Tnode(3)
    t2.left = Tnode(5)
    t2.right = Tnode(6)
    t2.left.left = Tnode(1)
    t2.left.right = Tnode(2)

    result = intersection(t1, t2)
    assert result == [1, 2, 3, 5]


    t3 = None
    t4 = Tnode(7)

    result = intersection(t3, t4)
    assert result == []


    t5 = Tnode(1)
    t5.left = Tnode(2)
    t5.right = Tnode(3)

    t6 = Tnode(4)
    t6.left = Tnode(5)
    t6.right = Tnode(6)

    result = intersection(t5, t6)
    assert result == []


