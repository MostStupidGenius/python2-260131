# part1_DP.py
# 동적 계획법(Dynamic Programming)
# 전역 문제(원래 문제)의 정답(최적해)을 찾기 위해서 문제를 쪼개어
# 부분 최적해(부분 정답)를 구하여 그것으로 구성한 결과가
# 전역 최적해가 되도록 하는 알고리즘 설계기법이다.
# 부분 문제가 반복적으로 등장하여 중복 계산이 필요해지는 경우에
# 동적 계획법을 적용한다.
# 이때, 중복 계산을 피하기 위해 사용하는 정보 전달방법을
# 메모이제이션(memoization)이라고 부른다.
# 이전에 이미 계산한 결과를 메모이제이션에 저장하여 중복계산을 피한다.

# 피보나치 수열 - 메모이제이션
def fibo_memo(n:int, memo:dict={}, show=False):
    # memo 매개변수는 최초 호출시에는 사용하지 않는다.
    # 기본 케이스(기저사례)
    if n <= 1: # n이 0 혹은 1인 경우, 그대로 반환한다.
        return n
    
    # 메모에 저장된 계산결과를 활용하여 반환
    # 즉, 이미 memo에 n에 대한 결과값이 있다면
    if n in memo:
        # 그것을 반환한다. 중복 계산을 하지 않는다.
        return memo[n]
    
    if show: print(n)
    # 계산하고 저장하는 일반적인 로직
    memo[n] = fibo_memo(n-1, memo, show) + fibo_memo(n-2, memo, show)
    # memo에 n이라는 키값으로 그 결과값을 저장하여
    return memo[n] # 그것을 반환한다.

if __name__ == "__main__":
    import time
    # 실행시간 측정
    start = time.time()
    fibo_memo(10, show=True)
    end = time.time()
    print(f"{end-start:.5f}s")