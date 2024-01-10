from queue import PriorityQueue

class Graph:
    def __init__(self, graph, heuristic, start):
        self.graph = graph
        self.heuristic = heuristic
        self.start = start
        self.parent = {}
        self.solutionGraph = {}

    def applyAOStar(self):
        priority_queue = PriorityQueue()
        priority_queue.put((self.heuristic[self.start], self.start))

        while not priority_queue.empty():
            cost, current = priority_queue.get()
            if current == 'T':
                break

            for neighbor, weight in self.graph.get(current, {}).items():
                new_cost = self.heuristic[neighbor] + weight
                priority_queue.put((new_cost, neighbor))
                self.parent[neighbor] = current

        for node, parent in self.parent.items():
            if parent in self.solutionGraph:
                self.solutionGraph[parent].append(node)
            else:
                self.solutionGraph[parent] = [node]

    def printSolution(self):
        print("FOR GRAPH SOLUTION, TRAVERSE THE GRAPH FROM THE START NODE:", self.start)
        print("--------------------------------------------------------------------------")
        print(f"{self.solutionGraph}")
        print("--------------------------------------------------------------------------")


heuristic_values = {'A': 1, 'B': 6, 'C': 2, 'D': 12, 'E': 2, 'F': 1, 'G': 5, 'H': 7, 'I': 7, 'J': 1, 'T': 3}
graph_edges = {
    'A': {'B': 1, 'C': 1, 'D': 1},
    'B': {'G': 1, 'H': 1},
    'C': {'J': 1},
    'D': {'E': 1, 'F': 1},
    'G': {'I': 1}
}

G1 = Graph(graph_edges, heuristic_values, 'A')
G1.applyAOStar()
G1.printSolution()