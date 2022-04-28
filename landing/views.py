from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.
def index(request):
    context = {
        "weather_data": {
            "weather": "아주 맑음",
            "temperature": "17"
        },
        "members": ['hooni', 'janny', 'jisu']
    }
    return render(request, "index.html", context)

def months(request, month):
    month_list = []
    try:
        for m in range(1, 13):
            month_list.append(f"{m}월")
        return HttpResponse(month_list[month - 1])
    except:
        return HttpResponse('다시 입력 해주세요')


def detail(request, name):
    users = [
        {"name": "hooni", "email": "hooni@naver.com", "hobby": "running"},
        {"name": "mina", "email": "mina@naver.com", "hobby": "dance"},
        {"name": "yami", "email": "yami@naver.com", "hobby": "reading"},
        {"name": "cool", "email": "cool@naver.com", "hobby": "surfing"},
        {"name": "jack", "email": "jack@naver.com", "hobby": "golf"},
    ]
    result =""
    a_user = None
    for user in users:
        if user["name"] == name:
            # result += f"{user['name']}, {user['email']}, {user['hobby']}"
            a_user = user
            break
    return render(request, 'landing/users.html', a_user)

# def test_index(request):
#     return render(request, 'index.html')