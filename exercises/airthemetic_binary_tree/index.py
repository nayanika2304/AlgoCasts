class Node():
    def __init__(self,value,left = None,right=None):
        self.val = value
        self.left = left
        self.right = right


def evaluate(node):
    operators = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '/': lambda a, b: a / b,
        '*': lambda a, b: a * b,
    }

    if node.val in operators:
        fn = operators[node.val]

        return fn(evaluate(node.left),evaluate(node.right))
    else:
        return node.val

node = Node('*')
node.left = Node('+')
node.right = Node('+')
node.left.left = Node(3)
node.left.right = Node(2)
node.right.left = Node(4)
node.right.right = Node(5)

print(evaluate(node))
