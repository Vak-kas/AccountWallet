import pickle
import os
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

data_tmp = []

def register_wallet():
    if not os.path.exists('data.pickle'): 
        #pickle 파일이 존재하지 않는 경우 초기 가입도 안되어 있기 때문에 초기 가입 실행
        print("초기 비밀번호가 설정되어 있지 않습니다.")
        while True:
            print("설정할 비밀번호를 입력해주세요.(최소 4자리 이상)")
            wallet_password = input()
            if len(wallet_password) < 4:
                print("최소 4자리 이상 설정해주세요.")
            else:
                data_tmp.append({'url': 'account_wallet', 'user_id': 'admin', "password": wallet_password})
                break
        with open("data.pickle", 'wb') as fw:
            pickle.dump(data_tmp, fw)

    with open('data.pickle', 'rb') as fw:
        data_tmp = pickle.load(fw)

    if len(data_tmp) == 0:
        print("초기 비밀번호가 설정되어 있지 않습니다.")
        while True:
            print("설정할 비밀번호를 입력해주세요.(최소 4자리 이상)")
            wallet_password = input()
            if len(wallet_password) < 4:
                print("최소 4자리 이상 설정해주세요.")
            else:
                data_tmp.append({'url': 'account_wallet', 'user_id': 'admin', "password": wallet_password})
                break
        with open("data.pickle", 'wb') as fw:
            pickle.dump(data_tmp, fw)

def register():
    with open('data.pickle', 'rb') as fw:
        data_tmp = pickle.load(fw)
        
    wallet_auth = ''
    for data in data_tmp:
        if data['url'] == 'account_wallet':
            wallet_auth = data['password']

    while True:
        print("계정 지갑 비밀번호를 입력하세요.")
        input_password = input()
        if input_password == wallet_auth:
            print("인증되었습니다.")
            break
        else:
            print("비밀번호가 틀립니다.")

    while True:
        print("계정 생성 페이지 입니다. 중지하시려면 X 를 입력하세요.")
        print("등록할 사이트의 별명을 입력해주세요.")
        input_name = input()
        if input_name == 'X' or input_name == 'x':
            break
        print("등록할 사이트의 기본 URL을 입력해주세요.")
        input_url = input()
        print("등록할 사이트의 아이디를 입력해주세요.")
        input_user_id = input()
        print("등록할 사이트의 비밀번호를 입력해주세요.")
        input_password = input()
        data_tmp.append({'site_name': input_name, 'url': input_url, 'user_id': input_user_id, 'password': input_password})
        with open("data.pickle", 'wb') as fw:
            pickle.dump(data_tmp, fw)


register_wallet()
register()