from django.shortcuts import render, HttpResponse
from .scrapper import scrapper, vox_scrapper
from .models import Article

# Create your views here.


def homepage(request):
    Article.objects.all().delete()
    scrapper()
    articles = Article.objects.all()
    count = Article.objects.count()

    context = {
        'articles': articles,
        'count': count
    }
    return render(request, "home.html", context)


def sort(request):
    articles = Article.objects.all()
    count = Article.objects.count()
    if request.method == 'POST':
        sortID = request.POST.get('sort', None)
        if sortID == 'author':
            articles = sorted(articles, key=lambda x: x.author)

        elif sortID == 'title':
            articles = sorted(articles, key=lambda x: x.title)

    context = {
        'articles': articles,
        'count': count
    }
    return render(request, "home.html", context)


