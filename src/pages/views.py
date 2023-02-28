from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homepage_view(request, *args, **kwargs):
    print(request.user)
    # return HttpResponse("<hi>Hi Django<hi>")
    return render(request, "home.html", {})

def contacts_view(request, *args, **kwargs):
    # return HttpResponse("<hi>Hi contact<hi>")
    my_context = {
        "my_text": "this is about me",
        "my_number": 123,
        "my_list": [1,2,3, 123]
    }
    return render(request, "contant.html", my_context)
    