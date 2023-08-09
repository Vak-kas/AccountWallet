import os
import find_account;

def delete_account():
    site_name = input("삭제할 계정의 사이트를 입력하세요 : ");
    id_info = input("계정의 아이디를 입력하세요 : ");
    id_name = id_info+".txt";
    target_path = find_account.return_file_path(site_name, id_name);

    if target_path == None:
        print("계정이 존재하지 않습니다.")
        return
    
    file_path = target_path

    

    with open(target_path, "r") as f:
        line = f.readline()

        # print(line)

        if len(line) == 0:
            print("파일을 읽어오지 못하거나, 파일에 내용이 존재하지 않습니다.")
            return -1
        
        #현재 경로
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # passward.txt 파일의 경로
    passward_file_path = os.path.join(script_dir, '..', 'login', 'passward.txt')
    passwd_file = open(passward_file_path, "r")
    #저장되어 있던 비밀번호 불러오기
    admin_password  = passwd_file.readline();
    print(admin_password);
    print("** 계정 삭제 **")
    print("계정 삭제를 위해 계정 지갑 비밀번호를 입력해주세요 >>")

    password = input()

    count = 5

    if(admin_password == password):
        file_delete(target_path)
        return 0
    else:
        print("계정지갑의 비밀번호가 틀렸습니다.")
        while count != 0:
            print("남은 횟수 : ", count)
            print("계정 삭제를 위해 계정 지갑 비밀번호를 입력해주세요 >>")
            password = input()

            if(admin_password == password):
                file_delete(target_path)
                return 0

            count -= 1
        
    print("계정파일이 삭제되지 않았습니다.")
    
    return -1

def file_delete(file_path):
    # 파일을 삭제합니다.
        try:
            os.remove(file_path)
            print(f"{file_path} 파일이 삭제되었습니다.")
        except FileNotFoundError:
            print(f"{file_path} 파일을 찾을 수 없습니다.")
        except PermissionError:
            print(f"{file_path} 파일을 삭제할 권한이 없습니다.")
        except Exception as e:
            print(f"파일 삭제 중 오류가 발생했습니다: {e}")
    

# delete_account()

#find_account 함수 생성시 유동경로로 만들예정
#target_path = find_account

# target_path = "find_account"

def modify_account():
    ## 파일을 찾지 못했을 때

    site_name = input("수정할 계정의 사이트를 입력하세요 : ");
    id_info = input("계정의 아이디를 입력하세요 : ");
    id_name = id_info+".txt";
    target_path = find_account.return_file_path(site_name, id_name);
    
    # print(target_path);
    if target_path == None:
        print("계정이 존재하지 않습니다")
        return -1 

    ##
    
    print("** 비밀번호 수정 **")

    ## 새로운 비밀번호 생성
    print("새로운 비밀번호를 입력해주세요 (4자리 이상) >> ")
    new_password = input() 
    ##

    ## 비밀번호 자릿수 예외처리
    while (len(new_password) < 4):
        print("너무 적은 비밀번호가 입력되었습니다.")
        print("새로운 비밀번호를 입력해주세요 >> ")
        new_password = input() 
    ##

    account_list = []
    # flag == 1 (admin)
    # flag == 2 (etc.)
    flag = 0

    ## 계정 파일 읽어오기
    with open(target_path, "r") as f:
        line = f.readline()

        #삭제할 부분
        # print(line)
        #

        if len(line) == 0:
            print("파일을 읽어오지 못하거나, 파일에 내용이 존재하지 않습니다.")
            return -1

        account_list = line.split(",")

        # print(account_list)

        ## 계정 파일 수정
        # print(account_list) 
        account_list[3] = f" password: {new_password}\n"   
        # print(account_list)
        ##

    ## 계정 파일 수정하기
    with open(target_path, "w") as f:
        account_txt = f"{account_list[0]},{account_list[1]},{account_list[2]},{account_list[3]}\n"
        # print(account_txt)
        f.write(account_txt)
        
        print("수정이 완료 되었습니다.")
    ##

    return 0

# modify_account()
    
