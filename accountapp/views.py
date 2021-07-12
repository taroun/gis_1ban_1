from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
#alt+enter 하면.... 뜸..

#def hello_world(request):
#    return HttpResponse('Hello World!')

#html을 가져오기
#분기점 생성
#render에 추가정보 보내주기 text객체에 접근 가능함
from django.urls import reverse

from accountapp.models import HelloWorld


def hello_world(request):
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
