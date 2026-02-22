# part2_sort_heap.py
# 최대힙 구조와 힙 정렬
# 최대힙(max heap)이란, 전체 데이터 중 가장 큰 값을
# 0번째 위치로 끌어올리기 위한 구조를 가리킨다.
# 최대힙 구조는 부모노드의 값이 자식노드의 값보다 항상
# 크거나 같은 상태를 유지하는 구조를 가리킨다.
# 이러한 구조를 유지하기 위해 재정렬하는 것을 heapify라고 부른다.

# 힙정렬은 최대힙 구조에서 가장 큰 값을 찾아내는 기능을 적극적으로 활용하여
# 가장 큰 값을 맨 뒤에 위치시키고 남은 요소 중 가장 큰 값을 다시 
# 끌어올리는 동작을 반복함으로써 오름차순 정렬을 구현해낸다.

# part1에서 작성한 MaxHeap 클래스를 import로 가져와서
# 힙정렬에 사용하자.
if __name__ == "__main__":
    from part1_max_heap import MaxHeap
else:
    from day06.part1_max_heap import MaxHeap
def heap_sort(data:list, show:bool=False):
    # 전달받은 데이터는 정렬되지 않은 정수값들의 집합이다.
    # 모든 데이터를 순차적으로 MaxHeap 객체에 추가하여
    # heap구조를 유지한다.
    heap_obj = MaxHeap()
    [heap_obj.insert(e) for e in data]

    # 정렬 단계
    # 현재는 힙속성이 유지되지만 한 상태다.
    # 가장 큰 값인 0번째의 값을 마지막 요소와 교환한 뒤
    # 힙 크기를 줄이고 남은 요소들에 대해서 heapify를 진행한다.
    result = [] # 반환할 정렬된 리스트
    # for i in range(len(heap_obj.heap)):
    #     result.append(heap_obj.extract_max())
    while heap_obj.heap:
        result.insert(0, heap_obj.extract_max())
        if show: print(result)
    return result

if __name__ == "__main__":
    import random as r
    data = list(range(20))
    r.shuffle(data)
    print(data[:10])
    sorted_data = heap_sort(data, True)
    print(sorted_data[:])