
def dfs(graph, current_vertex, target, visited=None):
    if visited == None:
        visited = []
    visited.append(current_vertex)
    if current_vertex == target:
        return visited 
    else:
        for neighbour in graph[current_vertex]:
            if not neighbour in visited:
                path = dfs(graph, neighbour, target, visited)

                if path:
                    return path 

def bfs(graph, start_vertex, target):
    path = [start_vertex]
    vertex_and_path = [start_vertex, path]
    bfs_queue = [vertex_and_path]
    visited = set()

    while bfs_queue:
        current_vertex, path = bfs_queue.pop()
        visited.add(current_vertex)

        for neighbour in graph[current_vertex]:
            if not neighbour in visited:
                if neighbour == target:
                    path.append(neighbour)
                    return path 
                else:
                    path.append(neighbour)
                    bfs_queue.append([neighbour, path])
    
    return None