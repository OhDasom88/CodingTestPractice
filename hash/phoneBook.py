def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book,key=lambda x: x)
    for i in range(1, len(phone_book)):
        if len(phone_book[i-1]) < len(phone_book[i]):
            if phone_book[i-1] == phone_book[i][:len(phone_book[i-1])]:
                answer = False 
                break
    return answer

phone_book =["119", "97674223", "1195524421"]#false
phone_book =["123","456","789"]#true
phone_book =["12","123","1235","567","88"]#false
phone_book =["12","123","10",'11','0','01','02','00',"1235","567","88"]#false

solution(phone_book)