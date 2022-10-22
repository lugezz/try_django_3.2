from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import ArticleForm
from .models import Article


def article_view(request, id_art):
    obj = Article.objects.get(id=id_art)

    context = {'id': obj.id,
               'title': obj.title,
               'content': obj. content,
               'art_obj': obj,
               }

    return render(request, 'articles/article.html', context)


def article_search_view(request):
    # print (dir(request))
    query_dict = request.GET
    try:
        query = int(query_dict.get('query'))
    except Exception:
        query = None

    article_obj = None
    if query is not None:
        article_obj = Article.objects.get(id=query)
    context = {'obj': article_obj}

    return render(request, 'articles/search.html', context)


@login_required
def article_create(request):
    form = ArticleForm(request.POST or None)

    context = {
        'form': form
    }

    if request.method == 'POST':
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')

            art_obj = Article.objects.create(title=title, content=content)
            context['obj'] = art_obj
            context['created'] = True

    return render(request, 'articles/create.html', context)
