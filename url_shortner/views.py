from django.shortcuts import render

# Create your views here.

def index(request):
  form = URLForm()
  return render(request,"index.html")

