# part2_sort_bubble_adv.py
# 기존 버블 정렬은 n의 요소 개수에 대해서
# n * (n-1) 번의 검사를 진행한다. -> 비효율적
# 검사 횟수를 줄이기 위한 refactoring을 진행

# 1. 한번의 path를 지날 때마다 가장 큰 값이 마지막에 위치할 것이므로
#   이 부분은 정렬된 것으로 취급하여 추가적인 검사를 할 필요가 없다.
# -> 한 번의 path를 진행할 때마다 전체 반복횟수를 줄인다.
# => 전체 반복 횟수를 정량적(반절)으로 줄이는 최적화 방법이다.(정비례)

# 2. 한 번의 path 동안 단 한번도 교환이 이루어지지 않았다면
#   이후 path 반복에서도 교환이 이루어지지 않을 것이다.
#   이를 확인하고 조기종료하는 변수를 추가 선언, 사용

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
    is_swapped = False
    # 0부터 길이-1까지의 숫자를 반복
    for i in range(length):
        # 내부 반복을 통해 path를 설정
        # 전체 요소를 한 바퀴 순회하는 것을 path라고 하며
        # 확인할 부분은 전체다.
        # 매 path마다 is_swapped를 False로 초기화하고
        # 내부 반복에서 교환이 한번이라도 이루어졌다면 is_swapped를 True로 변경한다.
        is_swapped = False
        for j in range(length-1-i): # length - (i+1)
            # length-1까지 진행하는 것은 j+1이 인덱스를 넘지 않기 위해서다.
            # 매 path의 횟수를 저장하는 i만큼을 더 빼면 i개의 마지막 요소를
            # 검사하지 않게 된다.
            if datas[j] > datas[j+1]:
                # j번째(현재)요소의 값이 j+1(다음)번째 요소보다 크다면
                # 오름차순을 지키지 않은 것이므로 교환이 일어난다.
                datas[j], datas[j+1] = datas[j+1], datas[j] # 맞교환
                is_swapped = True
            count += 1 # 검사 및 교환 횟수를 세는 변수의 값을 1 증가
        if not is_swapped: # path가 반복되는 동안 한번도 교환이 일어나지 않았다면
            # 외부 반복을 중단한다. -> 조기종료
            break
            # 이미 어느 정도 정렬된 데이터에 대해서 조기종료로 최적화한다.
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