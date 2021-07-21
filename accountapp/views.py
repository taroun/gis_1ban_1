from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
#alt+enter 하면.... 뜸..

#def hello_world(request):
#    return HttpResponse('Hello World!')

#html을 가져오기
#분기점 생성
#render에 추가정보 보내주기 text객체에 접근 가능함
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.forms import AccountCreationForm
from accountapp.models import HelloWorld

#경로 변경 가능...
@login_required()
def hello_world(request):
#로그인 여부확인..
    if request.method == 'POST':

        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        #get방식으로 변경 직접안치고 라우팅(어떤 앱안의 저 name으로 가라..)
        #이 네임을 기반으로 역추적하는 reverse
        return HttpResponseRedirect(reverse('accountapp:hello_world'))

    else:
        # get방식에도...
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html',
                      context={'hello_world_list': hello_world_list})


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    #클래스에서는 reverse_lazy로.. 불러오는 방식이 달라서..
    success_url = reverse_lazy('accountapp:hello_world')
    #회원가입 페이지
    template_name = 'accountapp/create.html'
    #어떤 페이지로 들어가야.라우팅..

class AccountDetailView(DetailView):
    model = User
    #보고자하는 유저
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/delete.html'
