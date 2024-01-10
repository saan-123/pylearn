class pycodes:
	def program1:
		print(f"""
import heapq

def aStarAlgo(start_node, stop_node):
    open_set = [(0, start_node)]
    closed_set = set()
    g = {start_node: 0}
    parents = {start_node: start_node}

    while open_set:
        _, n = heapq.heappop(open_set)

        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print(f"Path found: {path}")
            return path
        
        closed_set.add(n)
        for m, weight in get_neighbors(n) or []:
            tentative_g = g[n] + weight
            if m not in g or tentative_g < g[m]:
                g[m] = tentative_g
                heapq.heappush(open_set, (tentative_g + heuristic(m), m))
                parents[m] = n
    
    print("Path doesn't exist")
    return None

def get_neighbors(v):
    return Graph_nodes.get(v, [])

def heuristic(n):
    H_dist = {
        'A': 10, 'B': 8, 'C': 5, 'D': 7, 'E': 3,
        'F': 6, 'G': 5, 'H': 3, 'I': 1, 'J': 0
    }
    return H_dist.get(n, 0)


Graph_nodes = {
    'A': [('B', 6), ('F', 3)],
    'B': [('C', 3), ('D', 2)],
    'C': [('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 8)],
    'E': [('I', 5), ('J', 5)],
    'F': [('G', 1), ('H', 7)],
    'G': [('I', 3)],
    'H': [('I', 2)],
    'I': [('E', 5), ('J', 3)]
}

aStarAlgo('A', 'J')
""")
