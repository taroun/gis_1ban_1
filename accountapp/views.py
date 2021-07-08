from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#alt+enter 하면.... 뜸..

#def hello_world(request):
#    return HttpResponse('Hello World!')

#html을 가져오기
#분기점 생성
#render에 추가정보 보내주기 text객체에 접근 가능함
def hello_world(request):
    if request.method == 'POST':
        return render(request, 'accountapp/hello_world.html',
                      context={'text': 'POST METHOD'})
    else:
        return render(request, 'accountapp/hello_world.html',
                      context={'text': 'GET METHOD'})
