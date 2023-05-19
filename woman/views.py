from django.shortcuts import render, redirect
from .forms import ArticlesForm
# Create your views here.
from .models import Articls


def index(request):
    return render(request, 'woman/index.html')


def index2(request):
    posts = Articls.objects.all()
    return render(request, 'woman/index2.html', {'posts': posts, })


def create(request):
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            erorr = 'форма была неверной'

    form = ArticlesForm
    data = {
        "form": form,
        "erorr": erorr
    }
    return render(request, 'woman/create.html', data)
