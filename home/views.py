from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import subscribers
from .forms import subsform

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = subsform(request.POST);
        if form.is_valid():
            your_email=form.cleaned_data['your_email']
            if subscribers.objects.filter(your_email__iexact=your_email).exists():
                pass
            else:
                p=subscribers(your_email=your_email)
                p.save()
    else:
        form = subsform()

    return render(request, "home/index.html", {'form': form})

def validate_your_email(request):
    your_email = request.GET.get('your_email', None)
    data = {
        'is_taken': subscribers.objects.filter(your_email__iexact=your_email).exists()
    }
    return JsonResponse(data)

def blog(request):
    return render(request, "home/blog.html")

def about(request):
    return render(request, "home/about.html")
