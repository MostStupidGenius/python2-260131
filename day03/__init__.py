# day03.__init__.py
# 현재 파일의 위치를 기준으로, 루트폴더를 찾아간다.
# 경로를 추출하는 os 패키지를 임포트 해야 한다.
import os

# 특정 경로의 부모 폴더 경로를 추출하는 기능
# os.path.dirname()
# 현재 실행하는 파일의 절대경로
file_path = __file__
# 부모 폴더의 경로
parent_folder = os.path.dirname(file_path)
print(parent_folder) # 예상: day03 폴더 경로 전체 출력

# day03은 루트폴더 workspace의 하위폴더다
# workspace의 절대경로를 추출하여 시스템의 환경변수에 등록해주어야
# day04, day05 등 다른 폴더의 파일의 모듈을 import할 수 있게 된다.
root_folder = os.path.dirname(parent_folder)
print(root_folder)

# 시스템 환경변수에 등록하기
# sys 패키지를 가져와서 등록해주어야 한다.
import sys
sys.path.append(root_folder) # 환경변수 등록