# part2_BFS.py
# 너비우선탐색(Breadth First Search)
# 시작지점을 기준으로 가까운 지점을 우선탐색하는 알고리즘
# 같은 거리에 있는 정점들을 하나의 레벨(level)에 있다고 표현하며,
# 각 레벨을 순차적으로 탐색하는 방식이다.

# 다음 방문 예정 노드를 순서 그대로 탐색을 한다 -> 입력 순서와 출력 순서가 같다
# 그래서 자료구조 중 큐 자료구조를 사용한다.

def bfs_queue(graph:dict, start:str):
    # 그래프 정보: graph
    # 시작 정점: start
    # 방문 여부를 담기 위한 set 데이터
    visited = set()
    # 다음 방문을 담을 큐 데이터
    queue = [start] # start를 먼저 담아준다.
    # start를 방문처리
    visited.add(start)

    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 0번째 데이터를 추출
        vertex = queue.pop(0) # 선입선출 -> 먼저 들어온 데이터를 추출한다.
        # 현재 방문 중인 정점을 출력
        print(vertex, end=" ")

        # 현재 정점의 이웃 정점을 순회
        for neighbor in graph[vertex]:
            # 만약에 해당 이웃 정점을 방문하지 않았다면
            if neighbor not in visited:
                # 방문처리
                visited.add(neighbor)
                # 방문예정(queue)의 마지막에 추가
                queue.append(neighbor)
    print()

if __name__ == "__main__":
    from part1_DFS import graph
    bfs_queue(graph, 'A') # A B C D E F
    bfs_queue(graph, 'F') # F C E A B D