import sys
import os
# from cryptography import Fernet

from login import check_passward_file as mf



def main_function():
    mf.start_make_file();
    mf.check_passward();
    
    
def make_log_report():
    # 암호화 키 생성
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)

    # 암호화된 디렉토리 경로
    encrypted_dir = "encrypted_directory"

    # 암호화된 파일 경로
    encrypted_file = os.path.join(encrypted_dir, "encrypted_file.txt")

    # 암호화할 내용
    data = b"Hello, World!"

    # 암호화된 디렉토리 생성
    os.makedirs(encrypted_dir, exist_ok=True)

    # 파일 암호화
    encrypted_data = cipher_suite.encrypt(data)

    # 암호화된 파일 저장
    with open(encrypted_file, "wb") as file:
        file.write(encrypted_data)

    print("파일이 암호화되었습니다.")