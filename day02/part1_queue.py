# part1_queue.py
# 선형자료구조 큐(queue)
# 큐는 대기열이라는 의미로, 먼저 들어온(FirstIn) 데이터가
# 먼저 나가는(First Out) 선형데이터구조다.(FIFO)
# 데이터 추가는 마지막에 추가되므로 .append(데이터)로 추가
# 데이터 추출은 0번째 요소를 제거하므로 .pop(0)으로 추출

# 함수 생성
def queue_program():
    # 데이터를 담을 큐를 생성
    queue = list()
    while True:
        # 현재 큐에 담긴 데이터 출력
        print(queue)
        # 입력을 받는 부분
        select = input(f"1. 데이터추가\n2. 데이터 출력\nexit. 프로그램 종료\n입력: ")
        
        # 들어온 값을 공백문자를 기준으로 나눴을 때 두 개의 값으로 나뉘는지 여부
        # 문자열.split(구분자문자열)
        splited = select.split(" ")
        if len(splited) > 1:
            # 1. 데이터 입력: 1을 입력하고 공백문자를 사용한 뒤
            # 입력할 데이터를 넣으면 해당 데이터를 큐에 추가
            # 예) 1 30 입력 -> 30이라는 값을 큐에 추가
            # splited의 길이가 2개 이상이므로 1번째 요소를 queue에 추가한다.
            queue.append(splited[1]) # 데이터 추가
            continue # 다음 반복으로 이동
        
        elif len(splited) == 1:
            # 2. 데이터 출력: 2를 입력하면 0번째에 있는 값을 출력
            if select == "2":
                # 요소의 개수를 확인
                if len(queue) == 0:
                #   요소가 없으면 "요소가 없습니다" 출력
                    print("요소가 없습니다.")
                    continue
                else:
                    # 요소가 있으므로 0번째 요소 출력
                    print(queue.pop(0))
                    continue
            # 3. "exit"를 입력하면 프로그램 종료(break)
            # elif select == "exit":
            elif select in ["exit", "esc", "x"]: # 다중 명령문
                print("프로그램 종료")
                break # while문 탈출
            else:
                # 미리 정해진 입력이 아닌 경우
                print("알 수 없는 값입니다. 다시 입력해주세요.")

if __name__ == "__main__":
    queue_program()
