# part1_sort_quick.py
# 퀵 정렬
# 분할정복 알고리즘을 사용하는 고급 정렬 알고리즘 중 하나로,
# 나누면서 정렬까지 수행한 뒤, 병합은 간단하게 수행하는 알고리즘이다.
# 핵심 로직은 이진탐색트리와 크게 다르지 않다.

# 이러한 퀵 정렬은 재귀함수 형태로 구현된다.
# 재귀함수는 자기자신을 다시 호출하는 형태로 점점 깊게 들어간다.
# 하지만 이렇게 들어가기만 한다면 함수가 종료되지 않을 것이다.
# 그래서 필요한 것이 '기본 케이스'이다.
# 기본케이스는 함수를 재귀적으로 호출하지 않고
# 특정 값만 반환하는 형태로 구현된다.
# 재귀케이스는 자기자신을 재귀적으로 호출하는 형태를 가진다.

def quick_sort(datas:list):
    # 데이터의 요소는 모두 정수라고 가정한다.
    # 재귀함수로 구현할 것이기 때문에 재귀함수 설계에 들어가야 한다.
    # 1. 기본케이스
    # 전달받은 데이터의 요소 개수가 1개 이하이면
    # 정렬할 요소가 없으므로 그대로 반환한다.
    if len(datas) <= 1:
        return datas # 그대로 반환
    # if문에서 return을 썼기 때문에 else를 굳이 작성할 필요는 없다.
    # + 가능한 한 들여쓰기는 필요한 만큼만 해야 한다.

    # 2. 재귀케이스
    # 퀵 정렬에서는 기준(pivot)을 정해서 기준보다 작은 값은
    # left로 설정, 큰값은 right로 설정하여
    # left와 right를 각각 재귀적으로 정렬한다.
    # 2-1. 기준 정하기
    pivot = datas[0] # 첫번째 요소를 고른다.(어떤 것을 고르든 상관없다.)
    # + 다만, 가능하면 중앙값을 고르는 게 정렬 횟수를 줄이는 방법이다.
    # === 중앙값 먼저 고르기 코드
    # median = sum(datas)//len(datas)
    # pivot = median if median in datas else datas[0]
    # ===

    # 2-2. left, pivot, right 그룹 나누기
    left = [e for e in datas if e < pivot]
    pivot_datas = [e for e in datas if e == pivot]
    right = [e for e in datas if e > pivot]

    # 2-3. 각 그룹을 재귀적으로 정렬
    left_sorted = quick_sort(left)
    right_sorted = quick_sort(right)

    # 3. 정렬된 left, right 그리고 pivot을 순서대로 병합한다.
    # 리스트 + 리스트 = 병합된 리스트
    result = left_sorted + pivot_datas + right_sorted
    
    # 4. 반환
    return result

if __name__ == "__main__":
    import random as r
    # datas = [e for e in range(100)]
    datas = list(range(100))
    # 셔플
    r.shuffle(datas)
    # 정렬 전 데이터 출력
    print(f"정렬전:\n\t{datas[:10]}")

    # 정렬 진행
    datas_sorted = quick_sort(datas)

    # 정렬 후 데이터 출력
    print(f"정렬 후:\n\t{datas_sorted[:10]}")
