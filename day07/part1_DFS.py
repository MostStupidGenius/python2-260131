# part1_DFS.py
# 깊이우선탐색(Depth First Search)
# DFS는 데이터를 탐색 할 때 깊이 있는 것을 먼저 탐색하는 방식이다.
# 탐색 예정인 노드(정점)는 미리 저장해두지만, 실제로 방문하는 것은 저장된 것과
# 다른 순서로 방문하게 된다.
# 그런데 이진트리와 다르게 그래프는 순환이 가능한 구조이기 때문에
# 방문 여부를 저장을 해야 한다. 이때 방문 여부 정보는 set 자료구조로 저장한다
# 중복된 값을 저장하지 않기 때문에 set 자료구조가 방문여부 저장에 적합하기 때문이다.

# 이러한 깊이우선탐색 알고리즘을 함수로 구현할 때에는 두 가지 방식을 사용할 수 있다.
# 첫번째는 재귀함수 방식, 두번째는 stack 자료구조 활용

# 재귀함수 방식의 DFS
# 탐색을 진행할 때에는 탐색의 대상이 되는 그래프(지도)와 -> graph:dict
# 시작 지점(정점)을 전달받아야 한다. -> start:str
# 또, 방문 여부를 전달받아야 방문하지 않은 정점을 다음에 방문하게 될 것이다.
# -> visited:set
# 방문여부는 처음 사용할 때에는 전달받지 않고 내부적으로 생성을 한 뒤 활용할 것이다.
def dfs_recursive(graph:dict, start:str, visited:set=None):
    # 처음 호출을 한 경우라면 visited가 None일 것이다.
    # 이때에는 빈 set을 생성하여 visited에 세팅해준다.
    if visited is None:
        visited = set()
        print()
    
    # 전달받은 현재 노드(정점) start를 방문처리
    visited.add(start)
    # 방문한 정점을 출력
    print(start, end=" ") # end매개변수를 설정하는 이유는
    # 탐색한 데이터를 한 줄로 출력하기 위해서다.

    # graph = {
    #   'A': ['B', 'C'],
    #   'B': ['A', 'F'],
    #   ...
    # }
    # 현재 정점을 키값으로 하여 graph에서 이웃한 정점을 방문했는지 여부에 따라
    # 재귀적으로 방문을 재개한다.
    for vertex in graph[start]:
        # 위 예시를 기준으로 봤을 때, start가 'A'라면 vertex에는 'B', 'C'가
        # 순차적으로 임시 대입되어 활용될 것이다.
        # 해당 인접한 정점을 방문한 적이 없다면
        if vertex not in visited: # 재귀케이스
            # 해당 정점을 start로 하여 재귀함수 호출
            dfs_recursive(graph, vertex, visited)
        else: # 기본케이스
            # 방문한 적이 있다면 아무것도 하지 않고 넘어간다.
            pass

# stack 자료구조를 활용한 DFS 탐색 알고리즘 구현하기
def dfs_stack(graph:dict, start:str):
    # visited: 방문여부는 내부에서만 사용하는 것이기 때문에
    # 매개변수로 받아오지 않는다.
    
    # 방문한 노드를 저장할 set
    visited = set()
    # 다음 탐색 대상을 담을 stack 자료구조 데이터
    # 시작 정점을 넣어두고 시작한다.
    stack = [start]

    # 스택이 빌 때까지 무한 반복
    while stack:
        # 스택에서 정점을 꺼냄 -> 가장 최근에 추가된 노드를 꺼낸다.
        vertex = stack.pop() # -1번째 요소를 vertex에 저장
        
        # 방문한 적이 없는 정점이라면
        if vertex not in visited:
            visited.add(vertex) # 방문처리
            print(vertex, end=' ') # 해당 정점 데이터 출력

            # 현재 정점(vertex)의 이웃 정점을 다음 방문예정(stack)으로 추가
            # 방문하지 않은 이웃만 추가(filter)
            neighbor = [e for e in graph[vertex] if e not in visited]
            # stack에 현재 시점 방문하지 않은 이웃을 extend로 추가
            stack.extend(neighbor)
        else: # 기본케이스
            # 모든 정점에 대해서 방문한 적이 있다면
            # 더 이상 추가되지 않고 stack이 빈 상태가 될 것이다.
            # 이때 순회가 중단된다.
            pass

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
if __name__ == "__main__":
    dfs_recursive(graph, 'A') # 'A'를 시작점으로 깊이우선탐색 진행
    # A B D E F C
    # print()
    dfs_recursive(graph, 'D') # D로 시작
    # D B A C F E
    print("\n", "=" * 10, "stack 방식", "=" * 10)
    dfs_stack(graph, 'A') # A로 시작, A C F E B D
    print("\n", "=" * 10)
    dfs_stack(graph, 'D') # D로 시작, D B E F C A

