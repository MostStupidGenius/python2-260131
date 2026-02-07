# part5_check_sort_time.py
# 세 가지 정렬 알고리즘을 import하여 가져오고
# 일괄적으로 같은 데이터셋을 대상으로 정렬을 수행한 뒤
# 수행하는 데 걸린 시간을 측정하여 출력해보자.

# 기본라이브러리
import time
import random
# 설치형 라이브러리(현재 없음)
# 내 작업장 내 라이브러리(파일)
from part2_sort_bubble_adv import bubble_sort
from part3_sort_selection import selection_sort
from part4_sort_insertion import insertion_sort

# 랜덤 데이터를 생성하여 리스트를 반환하는 함수
def gen_rand_list(size:int=10, start:int=1, end:int=100):
    # 안 쓰지만 만들어야 하는 변수는 언더바(스코어)로 표현한다.
    return [random.randint(start, end) for _ in range(size)]

# 수행시간을 측정하는 wrapper 함수 -> 감싸는 함수
# 정렬 알고리즘 함수를 전달받아서 내부에서 실행한다.
def check_time(func, datas:list):
    """
    :param func: datas를 전달받아서 사용하는 함수. check_time 함수 내부에서 실행된다.
    :param datas: 전달받은 func 함수에 전달할 인자/인수
    :type datas: list
    """
    # 시간 측정을 위한 시작시간 저장
    start_time = time.time()
    # 전달받은 func 함수를 실행한다.
    func(datas)
    end_time = time.time()
    return end_time - start_time


if __name__ == "__main__":
    # 기준 데이터 생성
    datas = gen_rand_list(1000)
    # 데이터를 여러 함수에 동일하게 전달하기 위해 함수를 튜플로 저장
    funcs = (bubble_sort, selection_sort, insertion_sort)
    # for문을 이용해 각각의 함수를 check_time에 전달
    for func in funcs:
        # 실행시간을 측정하기 위해 같은 데이터를 넣어야 한다.
        # 기준 데이터를 복사(copy)하여 check_time에 전달한다.
        exc_time = check_time(func, datas.copy())
        print(f"{func.__name__} {exc_time:.3f}s")