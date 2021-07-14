from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import hello_world, AccountCreateView

app_name = 'accountapp'

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    #파라미터 지정-템플릿뭐 쓸건지
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name = 'login'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
    #클래스에서 함수로 뱉어주는......as_view
    path('create/',AccountCreateView.as_view(),name='create')
]