class NodeIterator:
    def __init__(self, node: 'Node'):
        self.node = node

    def __next__(self):
        if self.node is None:
            raise StopIteration
        n = self.node
        self.node = self.node.next
        return n

class Node:
    def __init__(self, val: int, next: 'Node' = None):
        self.val = val
        self.next = next

    def __iter__(self):
        return NodeIterator(self)

def main():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node1.next = node2
    node2.next = node3

    for node in node1:
        print(node.val)

if __name__ == '__main__':
    main()