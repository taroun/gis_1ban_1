from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/create.html'

    #오버라이딩
    def form_valid(self, form):
        form.instance.user = self.request.user  #지금 요청을 보내는 유저가 그 프로필 주인..
        return super().form_valid(form)