def solution(id_pw, db):
    login_db = {}
    for i in range(len(db)):
        login_db[db[i][0]] = db[i][1]
        
    if id_pw[0] in login_db:
        print('아이디 맞음')
        if login_db[id_pw[0]] == id_pw[1]:
            print('로그인')
            return 'login'
        else:
            print('비밀번호 틀림')
            return 'wrong pw'
    else:
        print('아이디 없음')
        return 'fail'