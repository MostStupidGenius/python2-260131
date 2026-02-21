# part2_sort_merge.py
# 병합 정렬 알고리즘
# 병합정렬도 퀵정렬과 같이 분할정복 알고리즘을 기반으로 한다.
# 다만, Divide가 아니라 merge와 conquer를 같이 하는 것이 다른 점이다.
# 퀵정렬: divide + conquer -> merge(가볍게)
# 병합정렬: divide(가볍게) -> conquer + merge

# 그러다 보니 병합정렬은 나누는 동작을 하는 재귀함수와 정렬+병합하는 함수
# 이렇게 두 개로 구성된다.

# 재귀적으로 나누고 반환하는 동작만 수행
def merge_sort(datas:list):
    # 재귀함수이기 때문에 기본케이스부터 작성한다.
    # 1. 기본케이스
    # 데이터의 길이가 1이하면 그대로 반환
    if len(datas) <= 1:
        return datas
    
    # 2. 재귀 케이스
    # 2-1. 분할
    # 단순히 절반으로 리스트를 나눠버린다(left, right)
    mid_idx = len(datas) // 2
    # 2-2. 부분 정렬
    # 중앙인덱스를 기준으로 좌우 리스트를 분할 및 재귀적으로 정렬
    left = merge_sort(datas[:mid_idx])
    right = merge_sort(datas[mid_idx:])
    # 이 시점에서 left와 right는 정렬되어 있다고 가정한다.

    # 2-3. 병합
    result = merge(left, right)

    # 3. 반환
    return result

# 정렬과 병합을 동시에 수행하는 함수
# 이때 전달받는 두 개의 좌우 데이터는 모두 정렬되어 있다고 가정한다.
def merge(left:list, right:list)->list:
    pass

