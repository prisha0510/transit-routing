"""
Enter the solution for Q2 here.
Note: You may use may define any additional class, functions if necessary.
However, DO NOT CHANGE THE TEMPLATE CHANGE THE TEMPLATE OF THE FUNCTIONS PROVIDED.
"""
import numpy as np
import heapq
#from Q1 import Dij_generator

def bidirectional_dij(source: int, destination: int, graph_object) -> int:
    """
    Bi-directional Dijkstra's algorithm.

    Args:
        source (int): Source stop id
        destination (int): destination stop id
        graph_object: python object containing network information

    Returns:
        shortest_path_distance (int): length of the shortest path.

    Warnings:
        If the destination is not reachable, function returns -1
    """
    shortest_path_distance = -1

    try:
        graph_forward = graph_object
        graph_backward = graph_object.T

        V = graph_object.shape[1]

        q_f = [(0,source-1)]
        visited_f = np.zeros(V)
        dist_f = np.ones(V) * np.inf
        dist_f[source-1] = 0
        
        q_b = [(0,destination-1)]
        visited_b = np.zeros(V)
        dist_b = np.ones(V) * np.inf
        dist_b[destination-1] = 0

        while (q_f and q_b):
            smallest_dist_f,u_f = heapq.heappop(q_f)
            visited_f[u_f]=1
            for i in range(V):
                new_dist = smallest_dist_f + graph_forward[u_f][i]
                if new_dist<dist_f[i]:
                    dist_f[i]=new_dist
                    heapq.heappush(q_f, (new_dist, i))

            smallest_dist_b,u_b = heapq.heappop(q_b)
            visited_b[u_b]=1
            for i in range(V):
                new_dist = smallest_dist_b + graph_backward[u_b][i]
                if new_dist<dist_b[i]:
                    dist_b[i]=new_dist
                    heapq.heappush(q_b, (new_dist, i))
            
            if(visited_b[u_f]==1):
                break
            if(visited_f[u_b]==1):
                break
        
        shortest_path_distance = np.inf
        shortest_path_distance = np.min(dist_b + dist_f)
        shortest_path_distance = shortest_path_distance if shortest_path_distance!= np.inf else -1 

        return round(shortest_path_distance+0.0000000001)
    except:
        return shortest_path_distance

#graph_object = Dij_generator()
#print(bidirectional_dij(370, 641, graph_object))