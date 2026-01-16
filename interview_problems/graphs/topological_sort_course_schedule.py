'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
'''
from typing import List
from collections import defaultdict, deque

def dfs(graph, start_node, visited, visiting, sorted_nodes):
    visiting.add(start_node)
    result = True
    if start_node in graph:
        neighbors = graph[start_node]
        for neighbor in neighbors:
            # import pdb; pdb.set_trace()
            if neighbor in visited:
                continue
            if neighbor not in visiting:
                result = dfs(graph, neighbor, visited, visiting, sorted_nodes)
                if result is False:
                    return result
            else:
                return False
    visited.add(start_node)
    visiting.remove(start_node)
    sorted_nodes.appendleft(start_node)
    return result

def canFinish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    course_graph = defaultdict(list)
    # Indegrees
    indegrees_mapping = defaultdict(int)
    # Build graph
    for prerequisite in prerequisites:
        course, prereq = prerequisite
        course_graph[prereq].append(course)
        indegrees_mapping[course] += 1
        indegrees_mapping[prereq] += 0
    indegrees_items_array = deque(indegrees_mapping.items())
    sorted(indegrees_items_array, key=lambda x: x[1])
    # DFS Searchs
    visited = set()
    visiting = set()
    sorted_nodes = deque()
    course_graph_keys = course_graph.keys()
    result = True
    for node in course_graph_keys:
        if node not in visited:
            result = dfs(course_graph, node, visited, visiting, sorted_nodes)
            if result is False:
                return result
    return result
    # return num_courses == 0
    # DFS till num_courses is zero. Need to make sure we mark visited edges so we don't visit them again
    # DFS: Where do I start? Can start from node that has no indegrees, but has outdegrees
    # For each node with zero indegrees, Look at it's children. Start decreasing by one once the node has no neighbors
    # For each node with zero indegrees, pass it to DFS. Get it's neighbors. Pass it's neighbors to DFS as you pop them off. Then if no neighbors, reduce number courses by 1

# canFinish(2, [[1,0]])
# canFinish(5, [[1,4],[2,4],[3,1],[3,2]])
# canFinish(2, [[1,0],[0,1]])
# assert canFinish(2, [[1,0]]) == True
# assert canFinish(2, [[1,0],[0,1]]) == False
# assert canFinish(3, [[1,0],[0,2]]) == True
# assert canFinish(3, [[1,0],[0,2], [0, 1]]) == False
# assert canFinish(3, [[2,0],[2,1]]) == True
# assert canFinish(4, [[0,1],[0,2],[1,3],[3,0]]) == False
assert canFinish(3, [[0,2],[1,2],[2,0]]) == False


'''
UMPIRE
Understand: Will have number courses you need to take. Prerequisite integeres represent the course number. The number before represents the dependency of the subsequent course on that one
Each item will just have a dependency. You will need to construct the graph yourself.
Match: Topological Sort Maybe? But how. We construct graph
Plan: Need to keep track of visited edges to prevent cycles. Can use DFS to visit neighbors first
Implement: 
Review
Evaluate

'''