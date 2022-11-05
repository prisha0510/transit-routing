"""
CiSTUP Internship: Round 1
Enter the solution for Q1 here.
Note: You may use may define any additional class, functions if necessary.
However, DO NOT CHANGE THE TEMPLATE CHANGE THE TEMPLATE OF THE FUNCTIONS PROVIDED.
"""
import numpy as np
import heapq

def Dij_generator():
    """
    Reads the ChicagoSketch_net.tntp and convert it into suitable python object on which you will implement shortest-path algorithms.

    Returns:
        graph_object: variable containing network information.
    """ 

    graph_object = None
    try:
        with open(__file__[:-5] + "ChicagoSketch_net.tntp") as f:
            lines = f.readlines()
        lines = lines[9:]
        n = len(lines)
        inits = np.zeros(n)
        terms = np.zeros(n)
        lengths = np.zeros(n)
        for i in range(n):
            temp = lines[i].split()
            inits[i] = int(temp[0])
            terms[i] = int(temp[1])
            lengths[i] = float(temp[4])
        
        dims1 = np.max(inits)
        dims2 = np.max(terms)
        graph_object = np.ones((int(dims1), int(dims2)))*np.inf
        for i in range(n):
            graph_object[int(inits[i]-1)][int(terms[i]-1)] = lengths[i]
            
        return graph_object
    except:
        return graph_object


def Q1_dijkstra(source: int, destination: int, graph_object) -> int:
    """
    Dijkstra's algorithm.

    Args:
        source (int): Source stop id
        destination (int): : destination stop id
        graph_object: python object containing network information

    Returns:
        shortest_path_distance (int): length of the shortest path.

    Warnings:
        If the destination is not reachable, function returns -1
    """
    shortest_path_distance = -1
    try:
        V = graph_object.shape[1]

        q = [(0,source-1)]
        dist = np.ones(V) * np.inf
        dist[source-1] = 0

        while (q):
            smallest_dist, u = heapq.heappop(q)
            for i in range(V):
                new_dist = smallest_dist + graph_object[u][i]
                if new_dist<dist[i]:
                    dist[i] = new_dist
                    heapq.heappush(q, (new_dist, i))
            if (u == destination-1):
                break
        
        shortest_path_distance = dist[destination-1] if dist[destination-1]!= np.inf else -1      
        return shortest_path_distance
    except:
        return shortest_path_distance
