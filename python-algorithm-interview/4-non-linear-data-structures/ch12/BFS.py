# BFS

# input 에시
graph = {
    1: [2, 3, 4],
    2: [5],
    5: [6, 7]
    }


# 1. BFS 큐를 이용한 반복 구조로 구현
def iterative_bfs(start_v):
    discovered = [start_v]
    queue = [start_v]
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)
    return discovered
