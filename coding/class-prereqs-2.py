class Node(object):

    def __init__(self, id, parents=set(), children=set()):
        self.id = id
        self.parents = parents
        self.children = children

    def __repr__(self):
        return vars(self)

    def has_parent(self):
        return len(self.parents) > 0

    def has_children(self):
        return len(self.children) > 0

prereqs = [
    [1,2], [1,3], [1,6],
    [2,4], [2,5], [2,6],
    [4,5],
    [7,4], [7,8],
    ]

# Create all nodes and populate parent/child relationships based on prerequisites list
nodes = dict()
for prereq in prereqs:
    nodes[prereq[0]] = Node(prereq[0], children=(prereq[1]))
    nodes[prereq[1]] = Node(prereq[1], parents=(prereq[0]))

# Determine all paths through the prerequisites
paths = dict()
for node in nodes:
    paths[node.id] = list(node.id)
    ...


# The Plan...
# 1. create the nodes
# 2. build the paths
# 3. determine if any paths refer to the same node
