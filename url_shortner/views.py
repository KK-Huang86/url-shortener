from django.shortcuts import render,redirect
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from .form.url_form import UrlForm
from .models import Url
import string
import random
# Create your views here.

def index(request):
  form = UrlForm()
  return render(request,"index.html",{"form":form})

@require_POST
def shorten_url(request):
        form = UrlForm(request.POST)
        if form.is_valid():
            original_url = form.cleaned_data["original_url"]
            is_active = form.cleaned_data.get("is_active", True)

            existing_url = Url.objects.filter(original_url=original_url).first()
            if existing_url:
                short_url = request.build_absolute_uri('/') + existing_url.short_url
                return render(request, 'index.html', {'short_url': short_url, 'form': form})

            else:
                short_code = generate_short_code()
                short_url = request.build_absolute_uri('/') + short_code
                Url.objects.create(original_url=original_url, short_url=short_code,is_active=is_active)
                return render(request, 'index.html', {'short_url': short_url, 'form': form})

        else:
            form = UrlForm()
        return render(request, 'index.html', {'form': form})

def redirect_original_url(request, short_url):
    try:
        url_instance = Url.objects.get(short_url=short_url)
        if url_instance.is_active:
            return redirect(url_instance.original_url)
        else:
            return render(request, '404.html', status=404)
    except Url.DoesNotExist:
        return render(request, '404.html', status=404)

def generate_short_code():
    characters = string.ascii_letters + string.digits
    short_code=''.join(random.choice(characters) for i in range(6))
    while Url.objects.filter(short_url=short_code).exists():
        short_code=''.join(random.choice(characters) for i in range(6))

    return short_code



def get_information(request):
    if request.method == "POST":
        url = request.POST.get('original_url')
    if url:
        print(url) 
        return HttpResponse(f"Original URL: {url}")
    else:
        return HttpResponse("No URL provided.")
    
    return HttpResponse("This view only handles POST requests.")