from django.shortcuts import render, HttpResponse
from .scrapper import scrapper, vox_scrapper
from .models import Article


def homepage(request):
    """
    loads the homepage of the app and renders it

    deletes all existing articles in the database and calls the
    scrapper() function from scrapper.py to repopulate the database
    then using the context variable passes the database information
    to the template and renders it

    parameter request: the GET network request issued when the
        homepage is called
    returns: the rendered homepage
    """

    # resets the database and updates it by running the scrapper
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
    """
        displays the sorted data based off user input

        checks the POST request called from the form in home.html
        and depending on the input sorts the database and returns
        the rendered sorted articles

        parameter request: the POST network request issued by the user
        returns: the rendered sorted articles
        """

    # gets the articles from the data base
    articles = Article.objects.all()
    count = Article.objects.count()

    # sorts the list
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


def custom_filter(request):
    """
       displays the filtered data based off user input

       checks the POST request called from the form in home.html
       and depending on the input filters the database and returns
       the rendered filtered articles

       parameter request: the POST network request issued by the user
       returns: the rendered filtered articles
    """

    # gets the articles from the database
    articles = list(Article.objects.all())

    # filters the articles for the keywords
    if request.method == 'POST':
        sortID = request.POST.get('sort', None)
        filterStr = request.POST.get('filterField', None)

        if filterStr != "":
            if sortID == 'author':
                articles = list(filter(lambda x: filterStr.lower() in x.author.lower(), articles))

            elif sortID == 'title':
                articles = list(filter(lambda x: filterStr.lower() in x.title.lower(), articles))

    # passes in the articles to the template
    context = {
        'articles': articles,
        'count': len(articles)
    }

    # updates the database to the filtered version
    Article.objects.all().delete()
    for article in articles:
        Art = Article(title=article.title, author=article.author, source=article.source)
        Art.save()

    return render(request, "home.html", context)
