*** 참조 
https://nomadcoders.co/airbnb-clone/
linux 에서는 python3, 윈도우즈에서는 python

*** 쿼리분석기
https://www.electronjs.org/apps/sqlectron
sqlite  부터해서 지원되는 DB 많음

*** 아이디
djAdmin / **spdlqj
djUser / **spdlqj
djGuest / **spdlqj

***명명규칙
동일단어에서 오는 혼동을 막기 위해서
앱은 app, 클래스는 cls, 변수는  var 접두어를 사용한다.
클래스 안의 함수는 def_, 
클래스 밖의 함수는  fn_, 
related_name 은 rel
form이나 파라미터에 사용하는 변수는 txt

appRooms, appUsers
clsRoom, clsUser
varBio, varCity
def_count
fn_coun
relRoom
txtPage

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

*** 5-3 : no such table
python3 manage.py makemigrations appConversations
python3 manage.py migrate appConversations

*** 파이썬 3.4부터는 os.path.join() 대신에 pathlib  사용
path = os.path.join(BASE_DIR, 'uploads')
↓
path = BASE_DIR / 'uploads'

*** 9-0 : django-seed
폴더를 새로 만들어 진행했을경우에는
settings.py에도 앱을 추가해주어야 사용가능
> python  manage.py loveyou --times 5

*** 9-5
settings.py에서 오타 수정
MEDDIA_URL = "/media/"	
→	MEDDIA_URL = "/media/"

THIRD_PARTY_APPS = [    "djagno_seed",	]
→	THIRD_PARTY_APPS = [    "django_seed",	]


*** 10-0
urls.py 에서 namespace 사용

--- urls.py ------------------------
app_name = "core"
urlpatterns = [
    path("", room.view, name="view"),
    path("", room.delete, name="delete"),
]
-------------------------------------

--- html 에서 사용 -----------------
<a href='{% url "code.view" 파라미터 %}'>aa</a>
-----------------------------

*** 11-0
페이징 강의 방향에 대한 설명

*** 11-7
장고 참고 사이트 : https://ccbv.co.uk/projects/Django/2.2/

장고앱 이름(=폴더명)이 appRooms 일 경우

paginater 이용시 templates/rooms/home.html 은 작동 (임의 폴더명 가능)

class view 이용시 templates/rooms/home.html 은 오류 (임의 폴더명 불가능)
Exception Type: TemplateDoesNotExist
Exception Value: appRooms/clsroom_list.html

class view 이용시 templates/appRooms/home.html 으로 바꾸어야 작동함
