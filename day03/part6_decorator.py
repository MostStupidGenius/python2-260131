# part6_decorator.py
# 데코레이터(decorator)
# 데코레이터는 함수에 사용하는 특이한 기술로,
# 이름처럼 다른 함수를 꾸미기 위한 기술이다.
# 데코레이터는 함수를 통해서 구현된다.
# 이렇게 만들어진 데코레이터는 데코레이터 함수라고 불린다.
# 함수를 꾸미는(가로채기) 기능을 하기 때문에
# 함수를 인자로 전달받아서 내부에서 실행하는 동작을 수행한다.

# 단순히 외부에서 함수를 전달받아 사용하는 것을 
# 고차함수라고 부르지만, 데코레이터는 이를 더욱 쉽게
# 사용할 수 있도록 만들어준다.
import time
from part4_sort_insertion import insertion_sort

# 데코레이터 연습 함수
def check_time_deco(func): # 데코레이터 함수는 함수만 전달받는다.
    # 내부 함수를 선언
    # 내부 함수는 외부에서 접근이 불가능한 함수다.
    # 이 함수 내부에서만 선언되고 사용될 수 있다.
    def wrapper(*args): # 내부 함수는 몇 개의 인자를 받을지 모르기 때문에
        start_time = time.time()
        func(*args) # *args 혹은 **kwargs로 그대로 전달한다.
        end_time = time.time()
        times = end_time - start_time
        print(f"{times:.3f}")
        return times
    # 내부 함수를 안에서 실행하는 것이 아니라
    # 외부로 전달하여 실행되도록 한다.
    # 데코 함수 안에서는 이러한 wrapper 함수를 만드는 역할만 한다.
    return wrapper # 실행이 아님!

# 데코레이터 함수를 이 함수에 감싸려면
# @와 함께 데코레이터 함수 이름을 작성하면 된다.
@check_time_deco
def sleep_times():
    time.sleep(3)

@check_time_deco
def insertion(datas):
    return insertion_sort(datas)
if __name__ == "__main__":
    print("1")
    sleep_times()
    print("2")
    insertion([1, 3, 2, 4])
    pass