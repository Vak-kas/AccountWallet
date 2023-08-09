
import os;
file_path  = os.path.join(os.path.dirname(__file__), "passward.txt");
import sys;
import menu as mn;

def start_make_file():
    print("|ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ|");
    print("계정 입력/저장을 시작합니다.");
    print("|ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ|");
    
    
def set_passward():
    special_char = ["!", "@", "#", "$"]
    number = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0" ]

    while True:
        print("|ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ|");
        passward = input("설정할 비밀번호를 입력해주세요(특수문자(!, @, #, $), 영어, 숫자 포함 9글자 이상) : ")
        re_passward = input("비밀번호 확인 : ");
        check_special_char = False;
        check_number = False;
        len_check = False;

        if passward != re_passward :
            print("비밀번호와 비밀번호 확인이 서로 일치 하지 않습니다. 다시 설정해주세요.");
        else:
            for i in special_char:
                if i in passward:
                    check_special_char = True;
                    # print("특수문자 확인");
                    break;

            for i in number:
                if i in passward:
                    check_number = True;
                    # print("숫자 확인");
                    break;

            if len(passward) >=9:
                len_check = True;

            if check_special_char and check_number and len_check:
                passwd_file = open(file_path, "w")

                #암호화 시켜서 passwd_file 에 적을 것.
                passwd_file.write(passward);
                print("비밀번호가 설정되었습니다.");
                break;   

            else:
                print("비밀번호 조건에 부합되지 않습니다. 다시 입력해주세요.");

                
                
                
#비밀번호가 설정되어 있는지 확인
def check_passward():
    flag = False; #파일 존재 유무 확인위한 flag 변수
    #passward 파일 찾기
    if os.path.isfile(file_path):
        flag = True; #파일이 존재하면 flag = True

    #파일이 존재 하지 않다면    
    if not flag:
        print("비밀번호를 설정해야 합니다.");
        #비밀번호 설정요구, 
        while True: #y/n을 입력했을 시 반복문 정상입력으로 보고 탈출, 그 외 입력시 재입력 요구를 위한 while 반복문
            answer = input("비밀번호를 설정하시겠습니까?[Y/N] : ")
            answer = answer.lower(); 
            print(answer);
            # y 또는 n 입력 요구(대소문자 구분 x)
            if answer == "y"  or answer == "n":
                if answer =="y": #y를 입력했다면
                    set_passward(); #비밀번호 설정 함수 
                    break; 
                else: #n을 입력했다면
                    print("프로그램을 종료합니다");  #프로그램 종료
                    break;
            else:
                print("[Y/N]으로만 입력해주세요.")
                #재입력 요구
        
        
        
        
                    
    else:
        #passward.txt 파일이 존재할 시
        #파일 읽어오기
        passwd_file = open(file_path, "r")
        #저장되어 있던 비밀번호 불러오기
        saved_passward = passwd_file.readline();
        
        input_passward = input("비밀번호를 입력하세요 : ");
        if saved_passward == input_passward:
            print("비밀번호가 확인되었습니다.");
            print("|ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ|");
            mn.choice_function();
            
        else:
            print("비밀번호가 틀렸습니다.")
