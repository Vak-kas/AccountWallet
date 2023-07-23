import os


def delete_account():
    target_path = "admintest.txt"

    if target_path == None:
        return -1
    
    file_path = target_path

    admin_password = ""

    with open(target_path, "r") as f:
        line = f.readline()

        print(line)

        if len(line) == 0:
            print("파일을 읽어오지 못하거나, 파일에 내용이 존재하지 않습니다.")
            return -1
        
        admin_password = str(line[64:(len(line) - 1)])
        for i, txt in enumerate(line):
            print(i, txt)
        
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
    

delete_account()