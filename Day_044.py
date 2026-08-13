# ============================================================
# QUESTION:
# Your gym has multiple branches. Model which branches are
# connected by transport routes using a bidirectional graph.
#
# Given the following connections:
#
# connections = [
#     ("Pune", "Mumbai"),
#     ("Pune", "Nashik"),
#     ("Mumbai", "Surat"),
#     ("Nashik", "Aurangabad"),
#     ("Surat", "Vadodara")
# ]
#
# Write:
# 1. build_graph(connections) -> dict
#       Build the graph using an adjacency list.
#
# 2. bfs(graph, start) -> list
#       Return BFS traversal order from start node.
#
# 3. dfs(graph, start) -> list
#       Return DFS traversal order from start node.
#
# 4. is_connected(graph, a, b) -> bool
#       Check whether branch b can be reached from branch a.
#
# 5. shortest_path(graph, a, b) -> list
#       Return the path from a to b having the fewest hops.
# ============================================================


connections = [
    ("Pune", "Mumbai"),
    ("Pune", "Nashik"),
    ("Mumbai", "Surat"),
    ("Nashik", "Aurangabad"),
    ("Surat", "Vadodara")
]


# ------------------------------------------------------------
# 1. BUILD GRAPH
# ------------------------------------------------------------

def build_graph(connections):
    graph = {}

    # Go through every connection
    for a, b in connections:

        # Create empty list for a if it does not exist
        if a not in graph:
            graph[a] = []

        # Create empty list for b if it does not exist
        if b not in graph:
            graph[b] = []

        # Because graph is bidirectional,
        # add b to a's neighbors
        graph[a].append(b)

        # Also add a to b's neighbors
        graph[b].append(a)

    return graph


# ------------------------------------------------------------
# 2. BREADTH-FIRST SEARCH
# ------------------------------------------------------------

def bfs(graph, start):

    # Queue stores nodes waiting to be processed
    queue = [start]

    # Set keeps track of already visited nodes
    visited = {start}

    # Stores the final BFS order
    order = []

    # Continue until queue becomes empty
    while queue:

        # Remove the first node from queue
        node = queue.pop(0)

        # Add it to traversal result
        order.append(node)

        # Visit all neighboring nodes
        for neighbor in graph[node]:

            # Only process an unvisited neighbor
            if neighbor not in visited:

                # Mark it visited
                visited.add(neighbor)

                # Add it to the queue
                queue.append(neighbor)

    return order


# ------------------------------------------------------------
# 3. DEPTH-FIRST SEARCH
# ------------------------------------------------------------

def dfs(graph, start):

    # Stack is used for DFS
    stack = [start]

    # Keep track of visited nodes
    visited = set()

    # Store DFS traversal order
    order = []

    # Continue until stack becomes empty
    while stack:

        # Remove the last item from stack
        node = stack.pop()

        # Ignore node if already visited
        if node in visited:
            continue

        # Mark node as visited
        visited.add(node)

        # Add node to result
        order.append(node)

        # Add neighbors to stack
        #
        # reversed() helps maintain a predictable traversal
        # order similar to the adjacency list order.
        for neighbor in reversed(graph[node]):

            # Add only unvisited neighbors
            if neighbor not in visited:
                stack.append(neighbor)

    return order


# ------------------------------------------------------------
# 4. CHECK CONNECTIVITY
# ------------------------------------------------------------

def is_connected(graph, a, b):

    # If either branch does not exist,
    # there cannot be a path.
    if a not in graph or b not in graph:
        return False

    # BFS from branch a
    visited = {a}
    queue = [a]

    while queue:

        # Take the next branch
        node = queue.pop(0)

        # If we reached b, return True
        if node == b:
            return True

        # Check neighboring branches
        for neighbor in graph[node]:

            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    # b was never reached
    return False


# ------------------------------------------------------------
# 5. SHORTEST PATH
# ------------------------------------------------------------

def shortest_path(graph, a, b):

    # If either branch does not exist,
    # no path can be found.
    if a not in graph or b not in graph:
        return []

    # Queue contains:
    # (current_node, path_taken_so_far)
    queue = [(a, [a])]

    # Start node is already visited
    visited = {a}

    while queue:

        # Get current node and its path
        node, path = queue.pop(0)

        # If we reached destination,
        # return the path.
        if node == b:
            return path

        # Explore all neighbors
        for neighbor in graph[node]:

            if neighbor not in visited:

                # Mark neighbor as visited
                visited.add(neighbor)

                # Create a new path
                new_path = path + [neighbor]

                # Add it to the queue
                queue.append((neighbor, new_path))

    # No path exists
    return []


# ============================================================
# EXAMPLE USAGE
# ============================================================

# Build the adjacency-list graph
graph = build_graph(connections)

print("Graph:")
print(graph)

print("\nBFS from Pune:")
print(bfs(graph, "Pune"))

print("\nDFS from Pune:")
print(dfs(graph, "Pune"))

print("\nIs Pune connected to Vadodara?")
print(is_connected(graph, "Pune", "Vadodara"))

print("\nShortest path from Pune to Vadodara:")
print(shortest_path(graph, "Pune", "Vadodara"))
