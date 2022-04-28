# from django.http import HttpResponse, HttpResponseRedirect
# from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def sign_up(request):
    context ={}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_check = request.POST.get('password_check')
        if (username and password and password == password_check):
            try:
                new_user = User.objects.create_user(username=username, password=password)
                auth.login(request, new_user)
                return redirect('blog_samples:home')
            except:
                context['error'] = '이미 존재하는 아이디입니다.'
        else:
            context['error'] ='아이디와 비밀번호를 잘못 입력하셨습니다.'
    return render(request, 'my_accounts/sign_up.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect("blog_samples:home")
    context={}
    # 요청이 post인지 확인
    if request.method =="POST":
    # 아이디 입력받은 것 있는지 확인
        username = request.POST.get('username')
    # 비밀번호 입력받은 것 있는지 확인
        password = request.POST.get('password')
        if (username and password):
            # 비밀번호 체크 ----추가적으로 필요한 함수
            user = auth.authenticate(   # 통과 못하면 none 반환(auth.athenticate)
                request,
                username=username,
                password=password
            )
            # 로그인
            if user:
                auth.login(request, user)
                # 리다이렉트
                return redirect('blog_samples:home')
            else:
                context['error']='아이디랑 비밀번호 틀렸습니다.'
        else:
            context['error'] = '아이디 혹은 비밀번호를 입력해주세요'
    #context에 에러메시지 담아주기
    return render(request, 'my_accounts/login.html', context)


def logout(request):
    # if request.method =="POST":
    auth.logout(request)
    return redirect('blog_samples:home')


def naver_test(request):
    return render(request, 'my_accounts/naver_test.html')