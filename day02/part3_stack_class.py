# part3_stack_class.py
# 스택 자료구조를 클래스로 만들어보기
# 스택 내부의 속성(객체 변수)으로 스택 데이터를 관리하고
# 기능들을 분리하여 해당 기능 내에서 오류가 날 수 있는 부분을 모두 처리한다.
# 이로써 외부에서는 오류 처리나 번거로운 작업을 줄일 수 있고 숨길 수 있다.(은닉화)
# 프로그램을 무한 루프 돌리는 메서드도 만들 것이다.

class Stack():
    def __init__(self, head=None):
        """
        스택 클래스 생성
        :param self: 따로 받지 않는다.
        :param head: 스택의 첫번째 데이터. 입력해도 되고 입력하지 않으면 빈 스택으로 생성
        """
        # 전달받은 head가 None이면 전달받은 첫번째 데이터가 없으므로
        # 빈 리스트로 초기화한다.
        self.datas = [] if head is None else [head]
        self.selection = [
            ("데이터 삽입", self.append),
            ("데이터 출력", self.pop),
            ("마지막 데이터 확인", self.get_last),
            (1,2),
            (2,3),
            (3,4)
        ]
        self.텍스트 = 0
        self.기능 = 1
    
    # 요소 추가
    # .append(데이터값)
    def append(self, data=None, print_=False): # data를 입력받지 않은 경우,
        # 직접 입력을 받는 안내문구 추가
        if data is None:
            data = input("추가할 데이터 입력: ")
        self.datas.append(data)
        if print_: print(f"데이터 추가: {data}")
        # chaining 기법
        # 메서드를 사용한 다음에 해당 객체의 self를 반환함으로써
        # 이어서 다른 메서드를 연쇄적으로 연결고리로 연결하여 실행하는 기법
        return self

    # 요소 제거
    # .pop() 매개변수 없이 마지막 요소 제거
    # + 요소의 개수가 0개이면 None 반환
    def pop(self, print_=False):
        data = None
        if self.get_last() is not None: # 마지막 요소가 있다면
            data = self.datas.pop()
            if print_: print(data)
        else:
            print("요소가 없습니다.")
        return data

    # 요소의 개수를 확인하고 마지막 요소를 반환하는 기능
    # .get_last()
    def get_last(self, print_=False):
        data = None
        if len(self.datas) >= 1:
            data = self.datas[-1]
        else: # datas의 길이가 0이라면
            data = None
        if print_: print(data) 
        return data
        return self.datas[-1] if len(self.datas) >= 1 else None

    # 프로그램을 구동하는 run 메서드
    # 종료를 하기 전까지 무한히 반복된다.
    def run(self):
        while True:
            print(self.datas)
            for index, text_func in enumerate(self.selection, 1):
                text, func = text_func # (text, func)
                print(f"{index}. {text}")
            print(f"{len(self.selection)+1}. 종료")
            try: # 입력한 값이 숫자가 아니면 오류가 생길 수 있다.
                # 입력 숫자를 정수로 변환
                select = int(input("입력: ")) # 1, 2, 3, 4 중 하나
            except Exception as e:
                print(f"{e}")
                continue
            if select == len(self.selection)+1:
                # 기능의 숫자+1의 값을 입력하여 종료를 고를 경우
                # 프로그램 무한실행 종료
                return self

            # 선택한 선택지가 종료 번호 보다도 큰 경우
            # 다시 입력 안내
            if select > len(self.selection)+1:
                print("잘못 입력하셨습니다. 다시 입력해주세요")
                continue

            self.selection[select-1][self.기능](print_=True)

            # if select == 1:
            #     data = input("추가할 데이터 입력: ")
            #     self.append(data)
            # elif select == 2:
            #     # 데이터를 제대로 추출하면 해당 값을 출력하고
            #     # 요소가 없는 경우 None이 반환되기 때문에
            #     # or의 결정자 기능을 이용해서 마지막 값인 빈문자열을
            #     # None 대신 출력
            #     print(self.pop() or "") 
            # elif select == 3:
            #     print(self.get_last())
            # elif select == 4:
            #     # 4 종료를 고를 경우
            #     # 프로그램 무한실행 종료
            #     return self

if __name__ == "__main__":
    s = Stack()
    s.append(3)\
        .append(4)\
        .append(5)\
        .append(6)
    print(s.datas)

    print("=" * 20)
    s.run()
    print("프로그램 종료")