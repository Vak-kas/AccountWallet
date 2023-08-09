import register_account;
import handle_account;
import find_account

def choice_function():
    print("작업 하시고 싶은 내용의 숫자를 입력하세요");

    
    while True:
        input_number = (input("[1]: 계정 생성/등록, [2] : 계정 수정/삭제, [3] : 계정 찾기, [4] : 프로그램 종료    >>>    "));
        
        #계정 생성/등록
        if input_number == "1":
            register_account.register();
        
        #계정 수정/삭제
        elif input_number == "2":
            print("어떤 기능을 수행할까요?");
            select_number = (input("[1]: 계정 수정, [2] : 계정 삭제, [3] : 뒤로 가기    >>>    "));
            if select_number == "1":
                handle_account.modify_account();
            elif select_number == "2":
                pass;
            else:
                print("|ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ|");
                continue;
            
        
        #계정 찾기
        elif input_number == "3":
            find_account.choose_find_type()
        
        
        else:
            print("프로그램을 종료합니다.");
            break;
        
        
        
    
    
    
    
    
