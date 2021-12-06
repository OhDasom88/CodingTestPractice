
list1=['computer','asd1']#회원 아이디 
message = None
while True : 
    print(list1)
    id=input('아이디를 넣어주세요')
    print(id) 
    for nom in list1 : 
        if id==nom : 
            message = '로그인 되었습니다'
            print(message)
    if message ==None : 
        message ='로그인 되지않았습니다'
        print(message)
        newid=input('가입 아이디를 넣어 주세요.: ')
        list1.append(newid)




for number2 in [1,2,3,4,5,6,7,8,9]:
    print(f"{number2}단시작") 
    for number3 in [1,2,3,4,5,6,7,8,9]:
        print(f"{number2}*{number3}={number2*number3}")











