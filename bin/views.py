from django.shortcuts import render

# Create your views here.
def index(request):
    context = {"message":'Welcome Dude ! in the Index page.'}
    return render(request,'bin/index.html', context)

def log_in(request):
    return render(request,'bin/sinup.html')
