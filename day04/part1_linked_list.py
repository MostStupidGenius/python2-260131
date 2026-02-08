# part1_linked_list.py
# 연결 리스트(linked list)
# 연결 리스트는, 각 요소가 노드(node)라는 것으로 이루어진 선형자료구조를 가리킨다.
# 노드는, 값을 저장하는 data 속성과 다음 노드를 가리키는 next 속성으로 이루어져 있다.
# 기본적인 연결 리스트는 단방향 연결리스트로, 다음 노드만 가리키는 방식으로 구현된다.

# 노드 클래스
# self.data, self.next를 보유한다.
class Node():
    def __init__(self, data:int, next=None):
        # 노드의 데이터를 반드시 받는 방식으로 진행
        # 다음 노드에 대한 정보는 받을 수도, 안 받을 수도 있음.
        # 다음 노드가 없으면 .next는 None값을 가짐.
        self.data = data
        self.next = next
    
    def __str__(self) -> str:
        return f"Node({self.data})"

# 연결리스트 클래스
# 시작이 될 노드를 self.head로 저장한다.
# 이를 기준으로 다음 노드를 탐색하는 방식을 취한다.
# 특정 data를 가진 노드를 찾거나, 특정 data를 가진 노드와
# .next 사이에 새로운 노드를 삽입하는 등
# 연결 리스트를 다루는 동작 등을 정의한다.
class LinkedList():
    def __init__(self, head:Node=None, data:int=None):
        # 만약 head 매개변수로 Node타입의 데이터가 들어왔다면
        # 그것으로 먼저 설정하고,
        # head가 들어오지 않았다면 data를 Node에 담아서 head에 세팅한다.
        self.head = head or (Node(data) if data else None)
        self.length = int(bool(self.head))
        # 0, 0.0, None, "" 등은 False로 취급된다.
    
    # .append() 마지막에 새로운 데이터를 추가(Node)
    def append(self, data:int)->bool: # 잘 추가됐으면 True
        # 추가에 실패했으면 False
        # self.head가 있는지 확인
        # 만약에 없으면 새로운 데이터를 Node에 담아서 .head에 저장
        if self.head is None:
            # 새로운 데이터를 Node에 저장하여 head에 전달
            self.head = Node(data)
            # 제대로 저장되었으므로 True 반환
            return True
        # 있으면 .next를 반복적으로 확인
        # while문을 이용하여 조건식에 현재 노드의 .next가 있는지를 검사하고
        # .next가 있다면 현재 노드를 다음 노드로 바꿔준다.
        # 현재 노드를 담을 변수
        current_node = self.head # self.head가 있으므로
        # 현재 노드를 self.head로 설정
        while current_node.next is not None:
            # current를 .next로 설정한다.
            current_node = current_node.next
        # 현재 탐색중인 노드의 next가 None이라면
        # 현재 노드의 next를 새로운 데이터를 담은 노드로 설정해준다.
        current_node.next = Node(data)
        return True

    # .find() 특정 data를 가진 노드를 찾아서 반환
    # 해당 data를 가진 노드가 없으면 None 반환
    # 해당 data를 가진 노드가 여럿이 있다면 처음으로 만난 노드를 반환
    # + 매개변수 prev를 True로 설정하면, 이전노드와 찾는 노드를
    # 하나의 튜플로 포장하여 반환(prev기본값은 False)
    def find(self, data:int):
        # 현재 보고 있는 노드를 담을 변수
        current = self.head
        # current가 None이 아니라면 무한반복하며 다음 노드 탐색
        while current is not None:
            # 만약 현재 노드의 데이터가 찾는 데이터와 같다면
            if current.data == data:
                # 현재 노드를 반환
                return current
            # 찾는 데이터가 아니라면, .next를 current에 담는다.
            current = current.next
        # while문을 탈출했다는 것은, current가 None이라는 것이다.
        # 즉, 마지막 노드의 데이터도 찾는 데이터가 아니었다는 뜻이다.
        # 데이터를 못 찾았으므로 None을 반환한다.
        return None

    # .insert() 특정 data를 가진 노드(A)의 next로 새 Node를 추가
    # 이때, next(B)가 있었다면 새로운 Node(C)의 next로 B를 설정하고
    # A의 next에 새로운 노드C가 들어간다.
    def insert(self, target_data:int, new_data:int):
        # target_data를 가진 노드 뒤에 new_data를 가진 노드를 삽입
        new_node = Node(new_data)
        # self.find()를 이용하여 target_data를 가진 노드를 반환받자
        target_node = self.find(target_data)
        
        # + 만약 찾은 target_node가 None이라면,
        # next나 data 등의 속성을 가지지 못한다.
        # target_node를 못 찾았다면 삽입 실패 -> None 반환
        if target_node is None: return None

        # 기존 타겟의 다음 노드를 새로운 노드의 다음 노드로 설정
        new_node.next = target_node.next
        # 새로운 노드를 타겟 노드의 다음 노드로 설정
        target_node.next = new_node
        # 삽입 완료 시 new_node를 반환
        return new_node

    # .extract_datas_to_list() 모든 노드를 순회하여
    # 그 데이터들을 list에 담아서 반환
    # to_node 매개변수를 추가하여 False면 list로 데이터 반환
    # True면 노드를 리스트에 담아서 반환
    def extract_datas_to_list(self, to_node:bool=False):
        # 반환할 빈 리스트를 생성
        result = list()
        # self.head부터 시작하여 current 노드가 있으면 반복
        current = self.head
        while current is not None:
            # to_node의 True/False 여부에 따라
            # .data를 리스트에 담을지, current를 리스트에 담을지를 결정한 뒤
            result.append(current if to_node else current.data)
            # 다음 노드를 가리켜야 하므로 .next를 current에 설정해준다.
            current = current.next
        # while문을 탈출했다는 것은, 현재 노드가 None이라는 것이므로
        # 해당 리스트를 반환한다.
        return result


if __name__ == "__main__":
    node1 = Node(3)
    print(node1) # Node(3)
    print("=" * 10)

    link = LinkedList(node1)
    link.append(13)
    link.append(14)
    link.append(15)
    current = link.head
    while current:
        print(current.data)
        current = current.next
    print("=" * 10)
    print(link.find(14)) # Node(14)
    print(link.find(1)) # None

    print("=" * 10)
    # 삽입 성공 케이스
    new_node = link.insert(14, 24) # 14값을 가진 노드 뒤에
    # 24를 가진 노드를 삽입
    print(new_node) # Node(24) -> 삽입 성공
    
    # 삽입 실패 케이스
    print(link.insert(5, 55)) # 5라는 데이터를 가진 노드가 없으므로
    # 55 값을 가진 노드 삽입은 실패하고
    # None이 반환되어 print로 출력된다.
    
    print("=" * 5, "데이터 추출", "=" * 5)
    print(link.extract_datas_to_list()) # 리스트로 출력
    for node in link.extract_datas_to_list(1):
        print(node, end=" ")








