from binary_search_tree import Pair, BinarySearchTree
from my_dict import MyDict

def test0():
    tree = BinarySearchTree()
    tree.insert_key(20)
    tree.insert_key(30)
    tree.insert_key(40)
    # tree.insert_key(10)
    tree.insert_key(50)
    tree.insert_key(45)
    tree.insert_key(15)
    tree.insert_key(35)
    tree.insert(Pair(10, "Olgier er kongurinn"))

    print(tree)
    print(tree.is_in(10))
    print(tree.is_in(50))
    # For testing _before/_after_/_first/_last
    for pair in tree:
        print(pair.key, end=' ')
    print()
    for pair in reversed(tree):
        print(pair.key, end=' ')
    print()
    print('==>', tree.pairs())
    print('=>', tree.keys())
    print(tree.get(10))
    tree.clear()
    print(tree)



def test1():
    tree = BinarySearchTree()
    keys = [50, 30, 20, 25, 70, 60, 40, 35, 65, 80, 55]
    for key in keys:
        tree.insert_key(key)
    print(tree)
    print(tree)
    tree.delete(55)
    print(tree)
    tree.delete(20)
    print(tree)
    tree.delete(70)
    print(tree)
    tree.delete(50)
    print(tree)
    for pair in tree:
        print(pair.key, end=' ')
    print()
    for pair in reversed(tree):
        print(pair.key, end=' ')
    print()


# Some basic BST tests, add more tests as needed!

d = MyDict()

print(d)


d[0] = "Gummso"
d[1] = "123"
d[2] = "Go"
d[3] = "Drakula"

print(d)

print(d[1])
print(d.get(2,"Nope"))

print(len(d))

print(d)
del d[0]
print(d)