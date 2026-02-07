# part4_sort_insertion.py
# 삽입정렬(insertion sort)
# 삽입정렬은 정렬된 부분과 정렬이 안 된 부분을 구분하여
# 정렬할 요소를 정렬된 부분의 적절한 위치로 삽입하는 방식이다.
# 정렬된 부분의 큰 요소부터 작은 요소까지 순차적으로 비교하기 때문에
# 모든 정렬된 요소와 비교하는 경우가 적다.

# part3에서 만들었던 랜덤 리스트를 만드는 함수를 가져와서 활용할 것이다.

def insertion_sort(datas:list, show:bool=False):
    length = len(datas)
    count = 0 
    # 0번째 요소는 이미 정렬되어있다고 간주하고 1번째 요소부터 정렬을 시작한다.
    for i in range(1, length):
        target = datas[i] # 현재 삽입하려는 대상 값
        # 추가적인 변수 1개가 필요하다.
        
        # 현재 인덱스의 이전위치
        j = i-1
        # 몇번이나 반복하여 삽입할 위치를 찾을지 모르기 때문에
        # for문이 아니라 while문으로 j값을 수동으로 1씩 줄이며 탐색한다.
        while j >= 0 and target < datas[j]: # j값이 0보다 크거나 같아야 하고(정렬된 부분 탐색)
            # target의 값이 j번째 값보다 작아야 탐색을 진행한다.
            # 정렬된 부분에서 j번째 값을 j+1번째 값으로 이동시킨다.
            datas[j+1] = datas[j]
            # j값을 1 감소시키는 것으로 정렬된 부분의 더 작은 값쪽으로 이동한다.
            j -= 1
            count += 1
        # while문을 탈출했다는 것은 j값이 -1이 되어 정렬된 값 중 가장 작은 값까지
        # 탐색을 했거나, target의 값이 j번째 요소의 값보다 크거나 같다는 것이다.
        # -> 적절한 위치를 찾았다.
        datas[j+1] = target
        # j값이 -1에 도달한 경우(다른 경우도 포함), -1번째에 값을 넣는 것이 아니라,
        # 1을 증가시켜서 target이 들어갈 위치에 삽입한다.
    if show: print(count, datas)
    # 전체 for문이 종료되면 모든 정렬이 완료된 것이므로 datas를 반환한다.
    return datas

if __name__ == "__main__":
    # 랜덤 리스트 생성 함수 가져오기
    from part3_sort_selection import generate_random_list as grl

    # 랜덤 데이터 생성
    datas = grl(10)
    print("start", datas)
    datas = insertion_sort(datas, True)
    print("end", datas)