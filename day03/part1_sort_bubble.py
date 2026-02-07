# part1_sort_bubble.py
# 버블 정렬
# 버블정렬은 기초 정렬 알고리즘 중에서도 가장 구현하기 쉬운 알고리즘으로
# 그만큼 효율성은 떨어진다.
# 인접한 요소끼리 크기를 비교하여 오름차순/내림차순 기준을 충족하지 않으면
# 맞바꾸는 동작을 수행한다.

# 함수로 bubble_sort 구현하기
# 데이터를 리스트로 받는다고 가정
# 정렬과정을 관찰하기 위한 출력을 할 것인데, 실제 동작에서는 출력을 막아야 하므로
# show 매개변수로 출력을 제어한다.
def bubble_sort(datas:list, show:bool=False):
    """
    :param datas: 리스트로 데이터 전달받기
    :type datas: list
    :param show: True일 경우 print()문 출력
    :type show: bool
    """
    # 전체 데이터의 길이를 변수로 저장
    length = len(datas)
    count = 0
    # 0부터 길이-1까지의 숫자를 반복
    for i in range(length):
        # 내부 반복을 통해 path를 설정
        # 전체 요소를 한 바퀴 순회하는 것을 path라고 하며
        # 확인할 부분은 전체다.
        for j in range(length-1):
            # length-1전까지 순회하는 이유는 
            # j의 다음요소를 가리키는 j+1이 전체 길이보다 크거나 같으면 
            # 데이터 인덱스를 넘어가게 되기 때문이다.
            if datas[j] > datas[j+1]:
                # j번째(현재)요소의 값이 j+1(다음)번째 요소보다 크다면
                # 오름차순을 지키지 않은 것이므로 교환이 일어난다.
                datas[j], datas[j+1] = datas[j+1], datas[j] # 맞교환
            count += 1 # 검사 및 교환 횟수를 세는 변수의 값을 1 증가
    if show: print(count)

    # 정렬된 결과 반환
    return datas


if __name__ == "__main__":
    # 데이터 랜덤하게 섞는 기능
    import random as r

    datas = list(range(100)) # 0부터 99까지의 숫자가 오름차순 정렬

    r.shuffle(datas)
    # 섞인 데이터 출력
    print(datas[:10])
    datas = bubble_sort(datas, True)

    # 정렬된 데이터 출력
    print(datas[:10])