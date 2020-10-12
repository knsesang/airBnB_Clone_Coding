from django.views.generic import ListView
from . import models

#   class list view 형식 페이징
#   찾는 파일은 templates/앱이름/클래스이름_list.html 을 자동으로 읽어들임
#   templates/appRooms/clsroom_list.html
class clsHomeview(ListView):
    model = models.clsRoom
    paginate_by = 10
    paginate_orphans = 5
    ordering = "varCreated"