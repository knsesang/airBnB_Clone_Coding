***참조 
https://nomadcoders.co/airbnb-clone/
linux 에서는 python3, 윈도우즈에서는 python

*** 아이디
djAdmin / **spdlqj
djUser / **spdlqj

***명명규칙
동일단어에서 오는 혼동을 막기 위해서
앱은 app, 클래스는 cls, 변수는  var 접두어를 사용한다.
함수는 def_, related_name 은 rel

appRooms, appUsers
clsRoom, clsUser
varBio, varCity
def_count
relRoom


*** 3-3 : no such column 오류 : syncdb 실행 
*** 3-6 : no such table : 일괄 마이그레이션이 아니라 개별 마이그레이션 해준다
python3 manage.py makemigrations appRooms
python3 manage.py migrate appRooms


*** 5-0 : no such table
python3 manage.py makemigrations appReviews
python3 manage.py migrate appReviews

*** 5-1 : no such table
python3 manage.py makemigrations appReservations
python3 manage.py migrate appReservations

*** 5-2 : no such table
python3 manage.py makemigrations appLists
python3 manage.py migrate appLists
