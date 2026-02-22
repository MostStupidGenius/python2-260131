# 최대 힙 구조 클래스로 구현하기
# 최대힙 구조를 클래스로 구현하려면
# 1. 삽입 기능 : 새로운 값 추가(append) 및 heapify 진행
# 2. 추출 기능 : 최대값 추출
# 3. 재정렬(heapify) 기능(up/down)

# 클래스 선언
class MaxHeap():
    def __init__(self):
        # 힙 구조가 들어갈 빈 리스트 생성
        self.heap = []

    # 부모노드 인덱스 추출하기
    def parent(self, i:int):
        # i는 현재 노드의 인덱스를 전달받는다.
        # 부모노드의 인덱스는 현재 노드의 인덱스엣 1을 뺀 뒤
        # 2로 나눈 몫이 부모노드의 인덱스이다
        result = (i-1) // 2
        return result

    # 왼쪽 자식노드 인덱스 추출하기
    # 왼쪽 자식 인덱스는 현재 노드의 인덱스에서 2를 곱한 뒤 
    # 1을 더하면 왼쪽 자식 인덱스가 도출된다.
    def left_child(self, i:int):
        return i*2 + 1

    # 오른쪽 자시노드 인덱스 추출하기
    # 왼쪽 자식 인덱스보다 1크다
    def right_child(self, i:int):
        return self.left_child(i) + 1

    # 부모노드의 인덱스가 적절한지(존재하는지)
    # 만약 부모노드의 인덱스가 0보다 작다면
    # 음수가 나오게 되면서 실제 부모 노드가 아니게 될 수 있다.
    # 적절한지 여부(T/F)를 반환하는 함수
    def has_parent(self, i:int):
        return self.parent(i) >= 0

    # 왼쪽 자식 인덱스 적절한지
    def has_left_child(self, i:int):
        return self.left_child(i) < len(self.heap)
    
    # 오른쪽 자식 인덱스 적절한지
    def has_right_child(self, i:int):
        return self.right_child(i) < len(self.heap)
    
    def __repr__(self):
        return f"{self.heap}"
    
    # 삽입 연산
    # 새로운 데이터가 삽입되면 마지막 요소로 추가된다.
    # 삽입된 값이 부모노드보다 작으면 상관없지만
    # 힙속성이 유지되지 않은 상태면 힙구조로 되돌려야 하므로 
    # heapify를 수행해주어야 한다.
    # 이때, 아래쪽에서 위로 올라가면 heapify를 수행하게 되므로 
    # 이를 heapify_up이라고 부른다.

    # insert
    # 단순히 데이터를 마지막에 추가하는 동작
    # + heapify_up함수 호출
    def insert(self, data:int):
        # 1. self.heap의 끝에 새로운 값을 요소로 추가
        self.heap.append(data)

        # 2. self._heapify_up 호출
        # 메서드 이름에 언더스코어_가 먼저 붙는 메서드는
        # 외부에서 호출하지 않고 클래스가 내부에서만 호출한다는 의미를 가진다
        new_data_idx = len(self.heap) -1
        self._heapify_up(new_data_idx)

    # _heapify_up
    def _heapify_up(self, index: int):
        # 1. 부모노드가 존재하는지 검사
        has_parent = self.has_parent(index) 
        if has_parent:
            # 현재 노드의 데이터
            current_data = self.heap[index]
            # 부모 노드의 데이터
            parent_data = self.heap[self.parent(index)]
            if current_data > parent_data:
                # 현재 노드가 부모노드보다 그 값이 크다면
                # 교환이 일어난다
                parent_idx = self.parent(index)
                self.heap[index], self.heap[parent_idx] = \
                    self.heap[parent_idx], self.heap[index]
                # 교환 후, 현재 노드였던 데이터가 부모노드의 인덱스로 옮겨갔으므로,
                # 부모노드의 인덱스를 대상으로 
                # 재귀적으로 heapify_up을 수행한다
                self._heapify_up(parent_idx)
                pass
        else : # 부모노드가 존재하지 않거나
            # 존재하더라도 그 값이 현재 노드보다 작거나 같다면
            # 아무 동작을 취하지 않는다
            # -> 기본 케이스
            pass

    # 삭제 연산
    # 가장 큰 값인 루트 노드(0번째 요소)의 값을 추출하는 기능
    # 이때, 가장 큰 값이 추출되어 사라지면 힙 구조가 무너지므로
    # 다시 heap속성 유지를 위해 heapify가 수행된다.
    # 수행되는 방향이 아래쪽을 향하므로 heapify_down이라고 부른다.

    def extract_max(self, show:bool=False):
        # 1. 힙 구조의 길이가 0인지 여부를 검사
        # 0이면 추출할 데이터가 없으므로 None 반환
        if len(self.heap) == 0:
            return None

        # 2. 길이가 1 이상이라면, 0번째 요소의 값을 추출하여 변수에 저장
        # 마지막에 반환 예정
        max_value = self.heap[0]

        # 3. 마지막 요소([-1])를 0번째 요소에 덮어씌우고
        # 마지막 요소를 힙구조에서 제외시킨다(pop)
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        if show: print(self.heap)

        # 4. 남은 요소들에 대해서 heapify_down을 진행한다.
        # 이대 기준은 루트노드부터 시작한다. 
        # (작은 값인 루트노드가 끌어내려진다)
        # 이를 재귀적으로 하향 조정 수행
        if len(self.heap) > 0: # pop을 한 뒤에도
            # 요소의 개수가 0개가 아니라면
            self._heapify_down(0)
            # 아까 추출한 최대값을 반환
            return max_value
    
    def _heapify_down(self, index:int):
        # 현재 노드의 인덱스index가 가장 큰 값을 가진 인덱스라고 가정한 뒤
        largest_idx = index
        # 자식 노드의 값들과 비교하여 가장 큰 값을 가진 노드의 인덱스를
        # 찾아낸다
        # 1-1. 왼쪽 자식과 비교
        if self.has_left_child(index):
            left_data = self.heap[self.left_child(index)]
            current_data = self.heap[index]
            # 왼쪽 자식의 데이터 크기가 현재 노드보다 크다면
            if left_data > current_data:
                # 왼쪽 자식이 가장 큰 값인 것으로 설정
                largest_idx = self.left_child(index)
            # 오른쪽 자식에 대해서 값 비교
            if self.has_right_child(index):
                right_data = self.heap[self.right_child(index)]
                # largest의 인덱스가 변경되었을 수 있으므로
                # largest의 값과 비교하여 더 큰 값을 가진 인덱스로 설정한다.
                if self.heap[largest_idx] < right_data:
                    largest_idx = self.right_child(index)

        else:
            # 왼쪽 자식이 없다면, 오른쪽 자식도 없는 것이므로
            # 사실상 비교할 자식이 없는 셈이다
            # 이 경우, 아무런 동작도 취하지 않는다.
            # -> 기본 케이스
            pass

        # 2. 만약 처음에 설정했던 인덱스와 마지막에 변경된 가장 큰 인덱스가
        # 서로 다르다면, 세개(부모, 좌우자식)의 노드가 
        # 힙속성을 만족하지 못하는 것이므로
        if largest_idx != index:
            # 3. heapify_down이 수행되어 원래의 노드와 자식 노드가 교환된다.
            # largest에 저장된 인덱스와 index의 값이 서로 교환된다.

            # 값을 교환
            self.heap[index], self.heap[largest_idx] = \
                self.heap[largest_idx], self.heap[index]
            
            # heapify_down 호출
            self._heapify_down(largest_idx)
        # 끌어내려진 노드 인덱스를 전달한다.

        # 현재 노드의 값이 세 노드 중 가장 크다면
        # 힙속성을 유지한 것이므로 아무것도 하지 않고 반환된다
        # -> 기본 케이스
        else:
            pass


if __name__ == "__main__":
    import random as r
    heap = MaxHeap()
    data = list(range(10))
    r.shuffle(data)
    print(data)

    # 최대힙 객체에 랜덤으로 생성돈 숫자들을 순차적으로 삽입
    [heap.insert(e) for e in data]
    # 힙에 저장된 데이터 출력
    print(heap)
    
    # 가장 큰 값을 가진 데이터를 추출한다
    max_value = heap.extract_max(True)
    print (max_value) # 추출 데이터 확인

    # heapify_down이 제대로 수행되었는지 확인
    input("Enter to continue")

    print(heap)
    pass
