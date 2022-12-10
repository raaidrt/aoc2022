lines = []

while True:
    try:
        line = input()
        lines.append(line)
    except EOFError:
        break

def countInitialSpaces(line):
    count = 0
    for i in range(len(line)):
        if line[i] != " ": 
            return count
        count += 1
    return count

class Leaf:
    def __init__(self, name, parent, size):
        self.size = size
        self.parent = parent
        self.name = name
    def __repr__(self):
        return f"""Leaf(
\tname = {self.name},
\t{self.size}
)"""

from copy import deepcopy as dc

class Node:
    def __init__(self, name, parent, children):
        self.children = dc(children)
        self.parent = parent
        self.name = name
    def __repr__(self):
        return f"""Node(
\tname = {self.name},
\t{self.children}
)
"""

root = Node("/", None, [])
traversing = root

last = 1
prevCommand = None
for line in lines[1:]:
    isCommand = False
    if line[0] == "$":
        command = line[2:]
        prevCommand = command
        isCommand = True
    else:
        command = prevCommand

    if isCommand:
        tokens = command.split(" ")
        if tokens[0] == "cd":
            dirname = tokens[1]
            if dirname == "..":
                traversing = traversing.parent
            else:
                found = False
                for c in traversing.children:
                    if c.name == dirname:
                        traversing = c
                        found = True
                if not found:
                    traversing.children.append(Node(dirname, traversing, []))
                    traversing = traversing.children[-1]
    else:
        tokens = line.split(" ")
        if tokens[0] == "dir":
            if tokens[1] not in [c.name for c in traversing.children]:
                traversing.children.append(Node(tokens[1], traversing, []))
        else:
            size = int(tokens[0])
            if tokens[1] not in [c.name for c in traversing.children]:
                traversing.children.append(Leaf(tokens[1], traversing, size))

def size(node):
    if isinstance(node, Node):
        return sum(size(c) for c in node.children)
    return node.size

def count(node):
    if isinstance(node, Node):
        s = size(node)
        if s <= 100000:
            return s + sum(count(c) for c in node.children)
        else:
            return sum(count(c) for c in node.children)
    return 0

total = 70000000
unused_requirement = 30000000

unused = total - size(root)
print(f"Currently {unused} space is unused")

ms = [None]
def minSize(node):
    if isinstance(node, Node):
        s = size(node)
        u = unused + s
        print(f"Checking if {u} satisfies requirement")
        if u >= unused_requirement:
            if ms[0] == None:
                ms[0] = s
            else:
                ms[0] = min(ms[0], s)
        for c in node.children:
            minSize(c)


minSize(root)
print(ms[0])