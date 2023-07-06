import sys;
import os;

directory = "account_wallet"
file_list = os.listdir(directory)
def modify_account():
    # print("메뉴 화면으로 돌아가려면 exit를 입력하세요");
    while True:
        #폴더 입력받기
        dir_name = input("어떤 사이트(종류) 계정인지 입력하세요.(예 : 네이버, 다음, 카카오, 오버워치..) >>  ");
        #아이디 입력받기
        user_id = input("수정하고자 하는 id를 입력하세요 : ");
        
        file_path = os.path.join(directory, dir_name, f"{user_id}.txt");
        # print(file_path)
        
        #해당 폴더 안에 파일이 존재할 시, 파일 읽기
        if os.path.isfile(file_path):
            with open(file_path, "r") as file:
                content = file.read();
                print(content);
                print("|ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ|");
                break;
        #해당 폴더 안에 파일이 존재하지 않는다면?
        else:
            print("파일이 존재하지 않습니다.")
            print()
            print(f"해당 id의 모든 계정을 {dir_name}이 아닌 다른 곳에도 존재하는지 검색할까요?")
            choose = input("n을 입력할 경우, 해당 과정을 다시 시행하게 됩니다.[Y/N] >> ")
            choose = choose.lower();
            print(choose)
            #해당 폴더가 아닌 모든 폴더에서 파일이 존재하는지 확인하기
            if choose =="y" or choose =="n":
                if choose == "y":
                    print(f"{user_id} 아이디를 존재하는지 확인합니다.");
                    print("|ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ|");
            #처음부터 폴더 이름부터 입력받아서 다시 검색하기
                elif choose == "n":
                    print("계정 찾는 과정을 다시 시행합니다.");
                    print("|ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ|");
            #메인 메뉴화면으로 되돌아가기
            else:
                print("Y/N로 입력되지 않았기에, 메인 메뉴화면으로 돌아갑니다.");
                print("|ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ|");
                break;
            

def delete_account():
        # print("메뉴 화면으로 돌아가려면 exit를 입력하세요");
    #폴더 입력받기
    dir_name = input("어떤 사이트(종류) 계정인지 입력하세요.(예 : 네이버, 다음, 카카오, 오버워치..) >>  ");
    #아이디 입력받기
    user_id = input("삭제하고자 하는 계정의 아이디를 입력하세요 : ");

    file_path = os.path.join(directory, dir_name, f"{user_id}.txt");
    # print(file_path)

    #해당 폴더 안에 파일이 존재할 시, 파일 읽기
    if os.path.isfile(file_path):
        with open(file_path, "r") as file:
            content = file.read();
            print(content);
            print("|ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ|");
            
    #계정 비밀번호 입력
    
    # 현재 계정이 아이디, 비밀번호, 정보들을 보여준 후 이 정보를 계정지갑에서 삭제할 것이냐고 물어보기
    
    # 진짜로 삭제할 것인지 물어보기
    
    # y입력시 삭제후, 삭제가 완료되었습니다
    # n 입력시 계정 삭제가 취소되었습니다. 메뉴화면으로 돌아갑니다
    
    #해당 폴더 안에 파일이 존재하지 않는다면?
    else:
        print("존재하지 않는 계정입니다. 메인 메뉴화면으로 돌아갑니다.");
        print("|ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ|");
            
