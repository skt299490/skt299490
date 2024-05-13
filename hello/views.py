from django.http import HttpResponse

def index(request):
    return HttpResponse("勤怠管理システム")
