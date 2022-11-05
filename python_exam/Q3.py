"""
Enter the solution for Q3 here.
Note: You may use may define any additional class, functions if necessary.
However, DO NOT CHANGE THE TEMPLATE CHANGE THE TEMPLATE OF THE FUNCTIONS PROVIDED.
"""
import numpy as np

def calc_time(st):
    hrs = int(st[:2])
    mins = int(st[3:5])
    secs = int(st[6:])

    return 3600*hrs + 60*mins + secs

def number_of_routes(source_stopid: str, destination_stopid: str) -> int:
    """
    Find the number of routes going from source stop id to destination stop id.

    Args:
        source_stopid (str): Source Stop Id
        destination_stopid (str): Destination Stop Id

    Returns:
        final_count (int): Number of routes going from source to destination.
    """
    final_count = -1
    try:
        with open(__file__[:-5] + "stop_times.txt") as f:
            lines = f.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i][:-1].split(',')[:4]
        
        lines = lines[1:]

        trip_to_stops = {}
        for i in range(len(lines)):
            trip_to_stops[lines[i][0]] = []
    
        for i in range(len(lines)):
            trip_to_stops[lines[i][0]].append(lines[i][1])

        with open(__file__[:-5] + "trips.txt") as f:
            lines = f.readlines()
        
        for i in range(len(lines)):
            lines[i] = lines[i][:-1].split(',')[:2]
        lines = lines[1:]
            
        route_to_stops = {}
        for i in range(len(lines)):
            route_to_stops[lines[i][1]] = set()
        
        for i in range(len(lines)):
            stops = trip_to_stops[lines[i][0]]
            for stop in stops:
                route_to_stops[lines[i][1]].add(stop)
        final_count = 0
        for v in route_to_stops.values():
            if source_stopid in v and destination_stopid in v:
                final_count+=1

        return final_count
    except:
        return final_count