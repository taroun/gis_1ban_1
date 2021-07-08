from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#alt+enter 하면.... 뜸..

#def hello_world(request):
#    return HttpResponse('Hello World!')

#html을 가져오기
#분기점 생성
#render에 추가정보 보내주기 text객체에 접근 가능함
from accountapp.models import HelloWorld


def hello_world(request):
    if request.method == 'POST':

        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        return render(request, 'accountapp/hello_world.html',
                      context={'hello_world_output': new_hello_world})
    else:
        return render(request, 'accountapp/hello_world.html',
                      context={'text': 'GET METHOD'})
