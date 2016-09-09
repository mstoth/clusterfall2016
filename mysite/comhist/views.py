from django.shortcuts import render

# Create your views here.

def all(request):
    print(request.path_info.split('/').pop())
    return render(request,request.path_info.split('/').pop())
