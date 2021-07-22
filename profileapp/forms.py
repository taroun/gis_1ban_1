from django.forms import ModelForm

from profileapp.models import Profile


class ProfileCreationForm(ModelForm):
    class Meta:
        #Meta 정보-외적정보...데이터자체는 아니지만 설명해주는....
        model = Profile
        #user는 서버내에서...나머지는 클라이언트에게 받음..
        fields = ['image', 'nickname', 'message']
