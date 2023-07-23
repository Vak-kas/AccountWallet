#find_account 함수 생성시 유동경로로 만들예정
#target_path = find_account

target_path = "test.txt"

def handle_account():
    ## 파일을 찾지 못했을 때
    if target_path == None:
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
        print(line)
        #

        if len(line) == 0:
            print("파일을 읽어오지 못하거나, 파일에 내용이 존재하지 않습니다.")
            return -1

        account_list = line.split(",")

        print(account_list)

        ## 계정 파일 수정
        print(account_list) 
        account_list[3] = f" password: {new_password}\n"   
        print(account_list)
        ##

    ## 계정 파일 수정하기
    with open(target_path, "w") as f:
        account_txt = f"{account_list[0]},{account_list[1]},{account_list[2]},{account_list[3]}\n"
        print(account_txt)
        f.write(account_txt)
    ##

    return 0

handle_account()
    