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
    # 반환할 병합된 리스트를 result라는 이름으로 만들어둔다.
    result = []
    # + C언어였다면 좌우 리스트 길이의 합만큼의 크기로
    # 배열을 만들었을 것이다.

    # 왼쪽, 오른쪽 리스트에서 현재 비교대상되는 요소를 가리키는 인덱스 변수
    left_current, right_current = 0, 0 # 0번째 요소부터 시작
    
    # 두 리스트를 비교하며 인덱스를 증가시킨다.
    # 비교대상이 되는 요소들 중 더 작은 값을 result에 append시키고
    # 더 이상 비교할 대상이 없는 리스트가 나오면(요소 소모)
    # 남은 요소를 모두 result에 extend시킨다.

    # 대상의 인덱스가 길이와 같거나 커지면 반복은 중단한다.
    # 인덱스 범위를 넘어가기 때문이다.
    while left_current < len(left) and right_current < len(right):
        # 만약에 왼쪽의 현재 인덱스 요소 값이
        # 오른쪽 현재 인덱스 요소 값보다 작거나 같다면
        if left[left_current] <= right[right_current]:
            # 해당 요소 값을 result에 append한다.
            result.append(left[left_current])
            # left_current값을 1 증가 시켜서 다음 요소를 가리키게 한다.
            left_current += 1
        else:
            # 오른쪽 요소의 값이 더 작은 경우
            result.append(right[right_current])
            right_current += 1
    # while문 종료
    # while문이 종료되었다는 것은, 좌우 리스트 중 최소 하나는
    # 모든 요소가 소모되었음을 의미한다.
    # 어떤 리스트가 모두 소모되었는지 확인하기 번거롭기 때문에
    # 양쪽의 남은 요소(슬라이싱)를 모두 extend 해준다.
    result.extend(left[left_current:])
    result.extend(right[right_current:])

    # 최종 병합된 데이터 리스트 반환
    return result

if __name__ == "__main__":
    import random as r
    datas = list(range(100))
    r.shuffle(datas)
    
    # 정렬 전
    print("before:\n", datas[:10])
    datas = merge_sort(datas)

    # 정렬 후
    print("after:\n", datas[:10])