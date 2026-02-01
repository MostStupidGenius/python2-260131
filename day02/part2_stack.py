# part2_stack.py
# 선형자료구조 - 스택(stack)
# 스택 자료구조는 들어오는 입구와 출구가 같은 자료구조로
# 나중에 들어온(LastIn) 데이터가 먼저 나가는(FirstOut) 자료구조이다.
# 이러한 스택은 파이썬으로 구현할 때 마지막에 데이터를 추가하는 append와
# 마지막 데이터를 추출하는 pop만으로 구현할 수 있다.

# cmd(터미널)창에 명령어를 전달하여 터미널 창을 깨끗하게 만든 뒤
# 프로그램 출력을 보여주도록 하자.
import subprocess

def program_stack():
    # 스택을 담을 변수
    stack = list()
    # 입력할 선택지에 대한 정보를 튜플로 관리
    selection = (
        "데이터 추가",
        "데이터 출력",
        "종료"
    )
    data = None
    while True:
        # 프로그램 화면을 지우고 새로운 화면 띄우기
        subprocess.run("cls", shell=True)
        # subprocess.run(["cmd", "/c", "cls"])
        # 추출된 값 출력
        if data: print(data)

        # 현재 스택에 저장된 값 출력
        print(stack)
        # 입력 안내 문구 출력
        for i, text in enumerate(selection, 1):
            print(f"{i:02d}. {text}")
        # 입력받기(문자열)
        # 문자열에 .strip(제거할 문자열앞뒤 문자)를 사용하면
        # 해당되는 앞뒤에 위치한 값을 제거한 뒤 새로운 문자열을 반환한다.
        # 예: " 2 " -> "2", " 3 3 " -> "3 3"
        # 아무 값도 전달하지 않으면 아스키코드에서 문자로 표현할 수 없는 공백문자를
        # 모두 제거한다(32번 아래의 코드들)
        select = input("입력: ").strip()
        # 숫자 1을 입력하고 엔터 -> 추가할 데이터를 입력
        if select == "1":
            stack.append(input("추가할 데이터 입력: "))
            continue
        # 숫자 2를 입력하고 엔터 -> 저장된 데이터 중 마지막 요소(-1)를 추출/출력
        elif select == "2":
            # 요소의 길이가 1개 미만이면 다음 반복으로 이동
            if len(stack) < 1:
                print("출력할 요소가 없습니다.")
                continue
            data = stack.pop()
            print(f"추출: {data}")
            continue
        # 숫자 3을 입력하고 엔터 -> 프로그램 종료
        elif select == "3":
            break
        else:
            print("알 수 없는 입력입니다. 다시 입력해주세요.")

if __name__ == "__main__":
    program_stack()
    pass
