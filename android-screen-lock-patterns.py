# How many patterns Android screen lock supports?  Let's calculate it ...
# (note: this small program requests Python 3)

# The graph of Android screen lock includes 9 nodes
#Graph = {1, 2, 3, 4, 5, 6, 7, 8, 9}

# The graph of Android screen lock includes 16 nodes
Graph = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}

# Each node has few neighbors as following
Neighbors = [
    {2, 5, 6},                      # 1
    {1, 3, 5, 6, 7},                # 2
    {2, 4, 6, 7, 8},                # 3
    {3, 7, 8},                      # 4
    {1, 2, 6, 9, 10},               # 5
    {1, 2, 3, 5, 7, 9, 10, 11},     # 6
    {2, 3, 4, 6, 8, 10, 11, 12},    # 7
    {3, 4, 7, 11, 12},              # 8
    {5, 6, 10, 13, 14},             # 9
    {5, 6, 7, 9, 11, 13, 14, 15},   # 10
    {6, 7, 8, 10, 12, 14, 15, 16},  # 11
    {7, 8, 11, 15, 16},             # 12
    {9, 10, 14},                    # 13
    {9, 10, 11, 13, 15},            # 14
    {10, 11, 12, 14, 16},           # 15
    {11, 12, 15}                    # 16
]

# Each node has few neighbors as following
#Neighbors = [
    #{2, 4, 5, 6, 8},            # 1
    #{1, 3, 4, 5, 6, 7, 9},      # 2
    #{2, 4, 5, 6, 8},            # 3
    #{1, 2, 3, 5, 7, 8, 9},      # 4
    #{1, 2, 3, 4, 6, 7, 8, 9},   # 5
    #{1, 2, 3, 5, 7, 8, 9},      # 6
    #{2, 4, 5, 6, 8},            # 7
    #{1, 3, 4, 5, 6, 7, 9},      # 8
    #{2, 4, 5, 6, 8}             # 9
#]

# But some "lazy" guys may not use "tricky" connections (e.g. from node 1 to
# node 6 or 8).  To calculate that scenario, we can replace the Neighbors ...
# Neighbors = [
#   {2, 4, 5},                  # 1
#   {1, 3, 4, 5, 6},            # 2
#   {2, 5, 6},                  # 3
#   {1, 2, 5, 7, 8},            # 4
#   {1, 2, 3, 4, 6, 7, 8, 9},   # 5
#   {2, 3, 5, 8, 9},            # 6
#   {4, 5, 8},                  # 7
#   {4, 5, 6, 7, 9},            # 8
#   {5, 6, 8}                   # 9
# ]

# Total number of solutions (for each length) will be stored here
Solutions = [0, 0, 0, 0,  0, 0, 0, 0,  0, 0, 0, 0,  0, 0, 0, 0]


# Print text tree log with "node" and "length"
def log(node, length):
    string = ""
    for i in range(0, length):
        string += "."
    print(string + str(node))


# Recursively scan current "graph" from the "node" with current "length"
def scan(graph, node, length):
    Solutions[length] += 1
    subgraph = graph - {node}

    #log(node, length)

    for each_node in Neighbors[node - 1]:
        if each_node in subgraph:
            scan(subgraph, each_node, length + 1)

# Scan all possible patterns
for each_node in Graph:
    scan(Graph, each_node, 0)
print(Solutions)
