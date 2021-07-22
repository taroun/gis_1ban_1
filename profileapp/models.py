from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='profile')
    #OneToOneField-1대1로 연결시켜주겠다
    #on_delete-연결되있는 user가 탈퇴시..어떤 정책? CASCADE-종속된 같이 지움 SET_NULL-유지..
    #related_name 연경된 유저 객체 있으면 .profile로 접근가능..

    image = models.ImageField(upload_to='profile/', null=True)
    #upload_to-받아서 어디로 업로드 할거냐..
    #null-꼭 넣어야하는가아닌가..True이미지 없어도 괜참ㅎ음..

    nickname = models.CharField(max_length=30, unique=True)
    #max_length-최대길이, unique-유일....

    message = models.CharField(max_length=200, null=True)
