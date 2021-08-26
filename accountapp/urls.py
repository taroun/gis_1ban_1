from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView

app_name = 'accountapp'

urlpatterns = [
    #파라미터 지정-템플릿뭐 쓸건지
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name = 'login'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
    #클래스에서 함수로 뱉어주는......as_view
    path('create/',AccountCreateView.as_view(),name='create'),
    #pk-프라이머리 키,이유저 고유값 주소창에 함께 넘겨주기..
    path('detail/<int:pk>',AccountDetailView.as_view(),name='detail'),
    path('update/<int:pk>',AccountUpdateView.as_view(), name='update'),
    path('delete/<int:pk>',AccountDeleteView.as_view(), name='delete'),
]