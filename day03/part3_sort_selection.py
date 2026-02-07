# part3_sort_selection.py
# 선택 정렬(selection sort)
# 선택정렬이란, 현재 인덱스를 가장 작은 값으로 선정한 뒤,
# path를 순회하며 가장 작은 값을 가진 인덱스를 찾는다.
# 그 인덱스의 값과 현재 인덱스의 값을 맞교환한다.
# 현재 인덱스를 1 증가시키고 위 과정을 반복한다.
def selection_sort(datas:list, show:bool=False):
    length = len(datas)
    count = 0

    # 외부 반복.
    for i in range(length):
        # 현재 인덱스(i)를 제일 작은 값으로 먼저 선정
        min_idx = i
        # 내부 path는 i+1번째 요소부터 비교를 한다. 마지막 요소까지
        for j in range(i+1, length):
            # 만약에 min_idx에 있는 요소 값보다
            # j번째에 있는 요소의 값이 더 작다면
            # j를 min_idx로 재설정한다.
            if datas[min_idx] > datas[j]:
                min_idx = j
            count += 1
        # 만약 i번째 값과 min_idx의 값이 같다면 교환이 필요없으므로
        # 다음 반복으로 넘어간다.
        if datas[i] == datas[min_idx]: continue
        # 내부 for문을 탈출한 시점에 min_idx는 가장 작은 값을 가진
        # 요소를 가리킬 것이다.
        # min_idx의 값과 i번째 요소의 값을 맞바꾼다.
        
        datas[i], datas[min_idx] = datas[min_idx], datas[i]
        # 맞바꿈이 일어난 직후의 datas를 출력
        if show: print(count, datas)
    if show: print(count)
    # 외부 반복문이 끝나면 정렬이 완료된 것이므로
    # 정렬된 datas를 반환한다.
    return datas

# 랜덤한 정수값을 일정 개수만큼 만드는 함수
def generate_random_list(size:int) -> list[int]:
    import random as r
    # size 개수 만큼의 랜덤한 숫자값을 가지는 리스트를 생성하여 반환
    result = [r.randint(1, 100) for _ in range(size)]
    return result

if __name__ == "__main__":
    datas = generate_random_list(100)
    print("start", datas[:10])
    datas = selection_sort(datas, False)
    print("end", datas[:10])
    pass