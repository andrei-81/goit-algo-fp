import uuid
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.cm as cm

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, traversal):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    cmap = cm.get_cmap('coolwarm', len(traversal))
    norm = mcolors.Normalize(vmin=0, vmax=len(traversal) - 1)

    for step, node in enumerate(traversal):
        node.color = mcolors.rgb2hex(cmap(norm(step)))
        nx.set_node_attributes(tree, {node.id: {'color': node.color}})

    colors = [node[1]['color'] for node in tree.nodes(data=True)]

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def bfs(root):
    if not root:
        return []
    queue = [root]
    traversal = []
    while queue:
        node = queue.pop(0)
        traversal.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return traversal

def dfs(root):
    if not root:
        return []
    stack = [root]
    traversal = []
    while stack:
        node = stack.pop()
        traversal.append(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return traversal

# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Обходи дерева
bfs_traversal = bfs(root)
dfs_traversal = dfs(root)

# Візуалізація обходу в ширину
print("Обхід в ширину:")
draw_tree(root, bfs_traversal)

# Візуалізація обходу в глибину
print("Обхід в глибину:")
draw_tree(root, dfs_traversal)
