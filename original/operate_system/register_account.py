import os
def register():
    print("|ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ|");
    print("계정을 등록합니다");
    #폴더 유형 선택
    dir_name = input("어떤 사이트(종류) 계정인지 입력하세요.(예 : 네이버, 다음, 카카오, 오버워치..) >>  ");
    
    #경로 생성
    path = os.path.join("account_wallet", dir_name)
    
    #폴더 생성, 폴더 존재시 그냥 넘어감
    os.makedirs(path, exist_ok=True)

    user_id = input("계정의 아이디를 입력해주세요 : ");
    user_pw = input("계정의 비밀번호를 입력해주세요 : ");
    path = os.path.join("account_wallet", dir_name, user_id+".txt");
    
    subject = input("계정에 대한 추가적인 설졍을 적어주세요(계정 이름, 주제 등) : ");
    

    
    if os.path.isfile(path):
        print("동일한 계정이 존재합니다. 다른 단어로 다시 등록해주시길 바랍니다.");        
        print("|ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ|")
            
        
    else:
        with open(path, "w") as file:
            file.write(f"id : {user_id}\npw : {user_pw}\n"); 
            file.write(subject)
        print("계정 등록이 완료 되었습니다.")
        print("|ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ|")
