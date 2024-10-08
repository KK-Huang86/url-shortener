from django.shortcuts import render,redirect
from .form.url_form import UrlForm
from .models import Url
import string
import random
# Create your views here.

def index(request):
  form = UrlForm()
  return render(request,"index.html",{"form":form})

def shorten_url(request):
    if request.method == "POST":
        form = UrlForm(request.POST)
        if form.is_valid():
            original_url = form.cleaned_data["original_url"]
            print(f"Original URL: {original_url}") 

            existing_url = Url.objects.filter(original_url=original_url).first()
            if existing_url:
                short_url = request.build_absolute_uri('/') + existing_url.short_url
                return render(request, 'index.html', {'short_url': short_url, 'form': form})

            else:
                # 創建新的短網址
                short_code = generate_short_code()
                short_url = request.build_absolute_uri('/') + short_code
                print(f"short_url: {short_url} ")
                Url.objects.create(original_url=original_url, short_url=short_code)
                return render(request, 'index.html', {'short_url': short_url, 'form': form})

    else:
        # 如果表單無效，返回表單並顯示錯誤訊息
        form = UrlForm()
    return render(request, 'index.html', {'form': form})
  

def redirect_original_url(request, short_url):
    try:
        original_url = Url.objects.get(short_url=short_url).original_url
        return redirect(original_url)
    except Url.DoesNotExist:
        return render(request, '404.html', status=404)


def generate_short_code():
    characters = string.ascii_letters + string.digits
    short_code=''.join(random.choice(characters) for i in range(6))
    print(f"short_code:{short_code}")
    while Url.objects.filter(short_url=short_code).exists():
        short_code=''.join(random.choice(characters) for i in range(6))

    return short_code