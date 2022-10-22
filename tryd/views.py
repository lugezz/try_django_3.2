from django.shortcuts import render
from articles.models import Article

def home_view(request):
    obj = Article.objects.get(id=3)
    article_qs = Article.objects.all()

    context = {'id': obj.id,
        'title': obj.title,
        'content': obj. content,
        'art_obj': obj,
        'obj_list': article_qs
    }

    return render(request, 'home-view.html', context)