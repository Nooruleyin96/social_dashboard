from django.urls import path
from django.http import HttpResponse

def dummy_view(request):
    return HttpResponse("Hello from dashboard!")

urlpatterns = [
    path('', dummy_view),
]
