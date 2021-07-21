#별도의 파이썬 파일..

def decorator(func):
    def decorated(input_text):
        print("함수 시작!")
        func(input_text)
        print("함수 끝!")
    return decorated

@decorator
def hello_world(input_text):
    print(input_text)

#hello_world('HelloWorld!')

def decorator0(func):
    def decorated0(width,height):
        if width>=0 and height>=0:
            return func(width,height)
        else:
            raise ValueError('Input must be positive value')
    return decorated0

def decorator1(func):
    def decorated1(**kwargs):
        if kwargs['width']>0 and kwargs['height']>0:
            func(**kwargs)
        else:
            print("error")
    return decorated1

def deco(func):
    def decoted(**kwargs):
        if kwargs['user'].is_authenticated:
            return func(**kwargs)
        else:
            raise PermissionError('Login required')

    return decoted


class User():
    def __init__(self,auth):
        self.is_authenticated=auth

user=User(auth=False)

@decorator1
@deco
def rect(**kwargs):
    return print(kwargs['width']*kwargs['height'])

@decorator1
@deco
def triangle(**kwargs):
    return print((kwargs['width']*kwargs['height'])/2)

triangle(user=user,width=10,height=10)
rect(user=user,width=10,height=10)
