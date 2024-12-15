class Node:
    def __init__(self, parent, data):
        self.parent = parent
        self.data = data
        self.children = []

    def add(self, data):
        self.children.append(Node(self, data))
    
    def operator(self):
        return self.data
    
    def parent(self):
        return self.parent
    
    def children(self):
        return self.children
    
    def is_root(self):
        return self.parent == None
    
    def is_external(self):
        return self.children == []

def depth(node) :
    if node.parent == None:
        return 0
    else:
        return 1 + depth(node.parent)

def height(tree):
    if tree.is_external():
        return 0
    else:
        h = 0
        for i in tree.children():
            h = max(h, height(i))
        return h

def preorder(node):
    print(node.operator(), end = ' ')
    for i in node.children:
        preorder(i)

def postorder(node):
    for i in node.children:
        postorder(i)
    print(node.operator(), end=" ")
def generate_tree(number : int):
    def prime_factorize(number : int) -> list:
        n = 2
        factors = []
        while True:
            if number%n == 0:
                number = number//n
                factors.append(n)
            else:
                n += 1
                if n > number:
                    break
                continue
        return factors
    root : Node = Node(None, number)
    prime_factors = prime_factorize(number)
    if len(prime_factors) == 0:
        return root
    
    node_now = root
    for factor in prime_factors:
        if factor == number:
            break
        node_now.add(factor)
        right_child = (number//factor)
        node_now.add(right_child)
        number = right_child
        node_now = node_now.children[-1]
    return root

#
# Buat fungsi kalian di sini
#
def plus_minus(node):
    res = 0
    if node.operator() % 2 == 0:
        res += node.operator()
    else:
        res -= node.operator()
    for x in node.children:
        res += plus_minus(x)
    return res

def find_deepest_leaf(node):
    if node.is_external():
        return 0
    else:
        hasil_a = 0
        hasil_s = 0
        for x in node.children:
            hasil_s += 1 + find_deepest_leaf(x)
            if hasil_a <= hasil_s:
                hasil_a = hasil_s
            hasil_s = 0
        return hasil_a


def main():
    root = generate_tree(840)
    print(f"hasil plus minus = {plus_minus(root)}")
    print(f"leaf paling dalam = {find_deepest_leaf(root)}")
    print()
    root = generate_tree(1200)
    print(f"hasil plus minus = {plus_minus(root)}")
    print(f"leaf paling dalam = {find_deepest_leaf(root)}")
    print()
    root = generate_tree(8440)
    print(f"hasil plus minus = {plus_minus(root)}")
    print(f"leaf paling dalam = {find_deepest_leaf(root)}")
    print()
    root = generate_tree(53)
    print(f"hasil plus minus = {plus_minus(root)}")
    print(f"leaf paling dalam = {find_deepest_leaf(root)}")
    print()
    

if __name__ == "__main__":
    main()