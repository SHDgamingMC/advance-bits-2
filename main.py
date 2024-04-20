def determine_order(num_monsters, constraints):
    adjacency_list = {}
    for constraint in constraints:
        x, _, y = constraint.split()
        if x not in adjacency_list:
            adjacency_list[x] = set()
        if y not in adjacency_list:
            adjacency_list[y] = set()
        adjacency_list[x].add(y)
        adjacency_list[y].add(x)
    
    order = []
    visited = set()
    for node in sorted(adjacency_list.keys()):
        if node not in visited:
            dfs(node, adjacency_list, visited, order)
    
    return order[::-1]

def dfs(node, adjacency_list, visited, order):
    visited.add(node)
    for neighbor in sorted(adjacency_list[node]):
        if neighbor not in visited:
            dfs(neighbor, adjacency_list, visited, order)
    order.append(node)

# Sample input
num_monsters = 3
constraints = [
    "Buttercup must be killed beside Bella",
    "Blue must be killed beside Bella",
    "Sue must be killed beside Beatrice"
]

# Get the order
order = determine_order(num_monsters, constraints)

# Print the order
for monster in order:
    print(monster)


#by Suvin