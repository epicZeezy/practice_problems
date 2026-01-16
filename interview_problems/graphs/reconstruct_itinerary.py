'''
You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

'''
from typing import List
from collections import defaultdict
def find_itinerary(tickets: List[List[str]]) -> List[str]:
    # Iterate through tickets. And map source to list of destinations. So Adjacency list
    adjacency_list_airports = defaultdict(list)
    for ticket in tickets:
        source, destination = ticket
        adjacency_list_airports[source].append(destination)
    for key, value in adjacency_list_airports.items():
        sorted_value = sorted(value)
        adjacency_list_airports[key] = sorted_value[::-1]
    # Get JFK as first neighbor since you know that's where you start. Will use DFS
    home = "JFK"
    # Get JFK neighbors and add to the stack
    # neighbors = adjacency_list_airports[home]
    visited = set()
    # DFS. Will need to figure out how to keep track of paths. Not sure yet
    neighbors = adjacency_list_airports[home]
    visited = set()
    jfk_path = []
    stack = [home]
    result = []
    def dfs(node):
        while adjacency_list_airports[node]:
            next_destination = adjacency_list_airports[node].pop()
            dfs(next_destination)
        result.append(node)
    dfs("JFK")
    return result[::-1]

    # Mark JFK as visited
    # For each JFK neighbor, get it's neighbors in constant time and add to the stack
    # And keep doing this for each neighbor
    # When do we stop? When we have visited all nodes. We will have multiple paths so we will need to keep track of them somehow
    # As we do our DFS, we can keep track of paths for each node or keep track of previous for each one so we can do a trace. Not sure yet how we'll do the back track


assert find_itinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]) == ["JFK","MUC","LHR","SFO","SJC"]
assert find_itinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]) == ["JFK","ATL","JFK","SFO","ATL","SFO"]



'''
UMPIRE
Understand: We have a set of flights and we need to find the order of the flights starting from JFK
Match: Graph works here. DFS/BFS could work here. I'd probably use DFS because that's more intuitive for me
Plan:
Implement
Review
Evaluate
'''