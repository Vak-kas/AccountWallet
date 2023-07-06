#로그 임시 구현, 후에 암호화로 다시 생성 예정

import os;

path = os.path.join("log", "log.txt");

if os.path.isfile(path):
     with open(path, "w") as file:
        pass
else:
     with open(path, "w") as file:
            pass;
        
