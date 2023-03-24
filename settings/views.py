from django.shortcuts import render

# Create your views here.
def changes(request):
    return render(request,'changes.html')