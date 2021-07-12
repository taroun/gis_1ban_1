from django.urls import path

from accountapp.views import hello_world, AccountCreateView

app_name = 'accountapp'

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    #클래스에서 함수로 뱉어주는......as_view
    path('create/',AccountCreateView.as_view(),name='create')
]