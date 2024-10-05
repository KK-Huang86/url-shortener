from django.shortcuts import render
from .form.url_form import UrlForm
from .models import Url
import string
import random
# Create your views here.

def index(request):
  form = UrlForm()
  return render(request,"index.html",{"form":form})

def shorten_url(request):
  if request.method=="POST":
      form = UrlForm(request.POST)
      if form.is_valid():
         original_url=UrlForm.clean_original_url["original_url"]

      existing_url=Url.objects.filter(original_url=original_url).first()
      if existing_url:
        short_url = request.build_absolute_uri('/') + existing_url.short_url
        return render(request, 'index.html', {'short_url': short_url, 'form': form})
      
      short_code = generate_short_code()



def generate_short_code(request):
    characters = string.ascii_letters + string.digits
    short_code=''.join(random.choice(characters) for i in range(6))


    return short_code