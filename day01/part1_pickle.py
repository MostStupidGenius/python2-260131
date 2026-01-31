# part1_pickle.py
# 피클링(pickling)
# 피클링이란, 파이썬에서 만든 객체나 데이터를
# 다른 파이썬 환경에서 그대로 파이썬 객체로 사용하기 위해
# 바이너리 파일로 내보내서 저장하는 기술을 가리킨다.
# 다른 파일 형태로 만들어서 내보내는 것은 번거롭고 시간이 걸리지만
# 피클링을 통해 내보내는 것은 파이썬에서 제공한 방식을 사용하기 때문에
# 간편할 뿐더러 빠르기까지 하다.

# 기본 내장 라이브러리이기 때문에 import만 해주면 된다.
import pickle

# 피클 파일로 내보내기(쓰기) w, a
# 저장할 데이터 객체, 저장할 파일명을 전달받아서 저장하는 기능
# 이때 저장이 잘 되면 파일명을 반환한다.
# 저장이 실패하면 None을 반환한다.
def write_to_pickle(file_path:str, data:any) -> str|None:
    """
    피클링 기술로 데이터를 저장하는 함수
    :param file_path: 저장할 파일 경로
    :type file_path: str
    :param data: 저장할 데이터. dict, 함수, 클래스 객체 등 객체 형태는 모두 가능하다.
    :type data: any
    :return: 정상 저장 시 저장한 파일 경로 반환, 실패 시 None 반환
    :rtype: str | None
    """
    file = None # finally 처리 시 해당 객체가 없으면 에러가 생기므로
    # 변수 초기화만 해준다.
    try: # 파일 저장시 오류가 발생할 수 있음.
        # 전달받은 파일 경로를 with open으로 'bw'모드로 열어서(bw, wb 동일)
        with open(file_path, "bw") as file:
            # 전달받은 data를 .dump()로 저장한다.
            # 이때 저장할 데이터가 첫번째 인수, 두번째 인수가 저장할 파일 경로
            pickle.dump(obj=data, file=file)
    # 예외처리
    except FileExistsError as e:
        # 위와 같은 오류가 발생했을 때, 아래의 코드를 실행하고
        # 프로그램 종료 없이 코드 계속 수행.
        print(f"에러 발생: {e}")
    except FileNotFoundError as e:
        print("해당 폴더나 파일을 찾을 수 없습니다.")
    except Exception as e:
        # 모든 에러를 감지하고자 할 때 사용한다.
        # 실무에서는 알 수 없는 에러는 종료하는 것이 낫기 때문에
        # 사용을 권장하지 않는다.
        print(f"알 수 없는 에러: {e}")
    # finally 블록은 위에서 에러 발생여부와 무관하게 항상 실행되는 코드 블록이다.
    finally:
        if file:
            print("파일 객체 남아있음. 삭제")
            file.close()

# 피클링된 객체 파일을 다시 파이썬 객체로 바꿔서 받아오는 기능
# 파일 경로만 전달받는다.
# 반환값은 전달받은 객체를 그대로 돌려준다.
def read_from_pickle(file_path:str) -> any:
    result = None
    try:
        # unpickling은 pickle.load(파일객체)로 데이터를 받아올 수 있다.
        # 모드는 rb로 하여 바이너리 읽기 모드로 진행한다.
        with open(file_path, "rb") as file:
            result = pickle.load(file)
    except Exception as e:
        print(f"에러 발생: {e}")
    return result

if __name__ == "__main__":
    # 저장할 데이터 생성
    data = {
        "name": "홍길동",
        "age" : 30,
    }
    # 파일 경로
    file_path = "test.pkl" # 파일 확장자(.뒤의 내용)는 정해져있지 않지만,
    # 일반적으로 pkl, pickle 등을 사용한다. 

    # write_to_pickle 함수 사용
    write_to_pickle(file_path, data)

    # read_from_pickle 함수 사용
    data_pkl = read_from_pickle(file_path)
    print(data_pkl)