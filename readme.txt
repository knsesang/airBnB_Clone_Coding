참조 : https://nomadcoders.co/airbnb-clone/

동일단어에서 오는 혼동을 막기 위해서
앱은 app, 클래스는 cls, 변수는  var 접두어를 사용한다.
함수는 def_, related_name 은 rel

appRooms, appUsers
clsRoom, clsUser
varBio, varCity
def_count
relRoom

# 3-3 : syncdb 실행 :  no such column 오류 발생
# 3-6 : 강의 마친후 sqlite3.db 파일을 삭제후 다시 마이그레이션 한다.