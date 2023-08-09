import sys
import os

# 현재 파일의 디렉토리 경로를 가져옴
current_dir = os.path.dirname(os.path.abspath(__file__))
# print(current_dir)

# 'operate_system' 폴더의 경로를 계산
operate_system_dir = os.path.join(current_dir, "operate_system")
# print(operate_system_dir)

# 'operate_system' 폴더를 sys.path에 추가
sys.path.append(operate_system_dir)

# main.py 모듈을 불러옴
import main
# main.py의 코드를 실행
main.main_function();
# main.make_log_report();






exit = input(("프로그램 종료하시려면 엔터키를 눌러주세요......"));
