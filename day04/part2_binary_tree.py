# part2_binary_tree.py
# 이진트리(바이너리 트리)
# 이진트리는 트리 구조 중에서 자식 노드를 최대 2개까지만 가질 수 있는
# 트리를 가리킨다.
# 때문에 이러한 이진트리를 구현할 때에, 각 노드는 자기자신의 data와
# 왼쪽, 오른쪽 자식을 가리키는 각각의 변수, left, right를 가지게 된다.
# 조상노드로부터 자식노드로 가는 길은 하나의 길만 있으며
# 이러한 경로는 단방향 연결리스트의 성질을 가진다.

# 노드 클래스(이진트리용)
class Node():
    def __init__(self, data:int):
        self.data = data
        # 왼쪽 자식과 오른쪽 자식을 담을 변수 생성
        self.left = None
        self.right = None
    
    def __repr__(self):
        return f"{self.data}"
# 이진트리 클래스
class BinaryTree():
    def __init__(self, root:Node=None):
        # 최상위 부모 노드, 루트 노드를 설정한다.
        self.root = root
    
    # 완전이진트리의 성질을 따라서 데이터를 추가한다.
    # 왼쪽자식부터 노드가 비어있는지 여부를 확인한 뒤 설정하고
    # 만약 왼쪽 자식이 있다면 오른쪽 자식 노드를 확인한다.
    # 이를 반복적으로 수행하여 탐색하고 노드를 추가한다.
    # .append()
    def append(self, data:int):
        # 시작 노드는 루트 노드로 설정한다.
        current = self.root
        root = 3
        # 새로 추가할 노드를 변수에 저장
        new_node = Node(data)
        # 만약 루트 노드가 None이라면, .root를 Node(data)로 설정한다
        if current is None:
            self.root = new_node
            return
        # 다음으로 확인할 노드를 담을 queue 리스트
        queue = [current]
        # 대기열queue가 비어있지 않다면
        while queue: # 요소가 0개라면 False로 취급된다.
            # queue에서 0번째(탐색대상)을 pop 하여 추출한 다음
            current_node = queue.pop(0)
            # 해당 노드의 왼쪽 자식과 오른쪽 자식을 확인한다.
            if current_node.left:
                queue.append(current_node.left)
            else:
                current_node.left = new_node
                return
            # 오른쪽 자식 확인
            if current_node.right:
                queue.append(current_node.right)
            else:
                current_node.right = new_node
                return
        # while문 밖으로 나갈 일은 없다.
        return
    
    # 모든 노드의 데이터를 각 깊이별로 행마다 출력하는 기능
    def spread_tree(self):
        datas = [self.root]
        # 현재 세대를 나타내는 변수 생성
        count = 1
        while datas:
            current = datas.pop(0)
            count += 1
            is_last = count in [2**n for n in range(10)]
            print(current, end="\n" if is_last else " ")
            # 좌우 자식이 비어있지 않다면 추가
            if current.left:
                datas.append(current.left)
            else:
                continue
            if current.right:
                datas.append(current.right)
            else:
                continue
        print("\n출력끝")
if __name__ == "__main__":
    btree = BinaryTree(Node(1))
    [btree.append(e) for e in range(2, 10)]
    btree.spread_tree()