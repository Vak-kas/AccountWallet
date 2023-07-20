#계정 검색
import os
import sys
directory = "account_wallet"
file_list = os.listdir(directory)

#menu에서 import 되어서 실행되는 함수
def choose_find_order():
    #어떤 기능을 수행할 지 입력
    order_choose = (input("[1] : 사이트의 id들 검색하기, [2] : 비밀번호 검색하기, [3] : 뒤로 가기 >> "));
            
    #사이트 id를 검색하기
    if order_choose == "1":
        #사이트 입력받기, 엔터만 입력시 전체 계정 탐색
        site_name = input("어떤 사이트의 id들을 불러올까요?(입력 없을 시 모든 사이트들의 계정을 불러옵니다)  >>  ").rstrip();
        #엔터만 입력받아을 경우
        if site_name =="":
            print("전체 계정을 검색합니다");
            id_list = find_all_id(None); #전체 계정 검색하고, 리스트 돌려받기
            print(id_list)
            raise ValueError("아직 개발 덜 됐다.")
            
        else:
            print(f"{site_name}의 계정들을 검색합니다");
            id_list = find_all_id(site_name); #특정 사이트의 계정 전체 검색하기, 리스트로 돌려받기
            print(id_list)
            raise ValueError("아직 개발 덜 됐다.")
    
    #id를 입력하면 pw를 돌려받기
    elif order_choose == "2":
        find_user_passward();
    
    #1 또는 2가 입력이 되지 않았을 경우 계정 검색 함수 종료
    else:
        print("계정 찾기를 종료합니다.");
        print("|ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ|");
    return #함수 끝내기

#해당 사이트 디렉터리 안에 있는 파일들 불러와서 id와 계정에 대한 정보 싹 다 불러오기
def find_all_id(site):
    #site 매개변수에 None 이 입력받았을 경우에는 모든 계정 찾기
    if site == None:
        id_list = []; #return 할 변수
        #file_list 는 맨 윗줄에서, "account_wallet"안에 있는 리스트들의 목록을 저장해 두었음.
        #file_list 계정을 돌면서 반복
        for dir_name in file_list:
            #dir_name 에 directory를 돌면서 값을 넣어주고, 파일 검색을 위해 file_path에 넣어줌

            #피클 기능 X
            file_path = os.path.join(directory, dir_name);
            tmp_list = (os.listdir(file_path));
            id_list.append((dir_name, tmp_list)) #폴더명과 파일들을 하나의 튜플로 묶어서 id_list에 append 해주기
        return id_list
            
            
            
            #피클 기능 O     
    else:
        if site in file_list:
            file_path = os.path.join(directory, site);
            id_list = [(site, os.listdir(file_path))]
            return id_list
            
            
        else:
            print("해당 사이트 이름으로 등록된 계정이 없습니다.");
            tmp = input("모든 사이트에서 계정을 확인할까요?[Y/N]  >>  ");
            if tmp == "y" or tmp=="Y":
                print("|ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ|");
                find_all_id(None);
            else:
                print("메뉴화면으로 돌아갑니다");
                print("|ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ|");
                return;


#list를 읽고, index를 입력 받으면 해당 index의 비밀번호를 출력
def find_passward_using_list(lst):
    pass;


#사이트, 아이디 입력받으면 비밀번호 출력
def find_user_passward():
    #사이트 입력받기, 엔터만 입력시 전체 계정 탐색
    site_name = input("어떤 사이트의 id들을 불러올까요?(입력 없을 시 모든 사이트들의 계정을 불러옵니다)  >>  ").rstrip();
    id_info = input("비밀번호를 알고 싶은 계정의 id를 입력하세요 >> ").rstrip();
    id_name = id_info+".txt";
    file_path = os.path.join(directory, dir_name, id_name); #파일 경로 설정
    
    #파일 경로에 파일이 존재하는가?
    if os.isfile(file_path):
        pass;
    
    #파일 경로에 파일이 존재하지 않는가?
    else:
        pass
    
    
