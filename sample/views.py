from django.shortcuts import render, get_object_or_404
from .models import Article, Like
from django.http import JsonResponse

def article(request):
    articles = Article.objects.all()
    liked_list =[]
    for article in articles:
        liked = article.like_set.filter(user=request.user)
        if liked.exists():
            liked_list.append(article.id)

    params = {
        'articles': articles,
        'liked_list': liked_list
    }
    return render(request, 'sample/articles.html', params)

def like(request):
    if request.method == 'POST':
        article = get_object_or_404(Article, pk=request.POST.get('article_id'))
        user = request.user
        liked = False
        like = Like.objects.filter(
            article = article,
            user = user,
        )
        if like.exists():
            like.delete()
        else:
            like.create(
                article = article,
                user = user,
            )
            liked=True

        #likedはいいねされているlike
        params={
            'article_id': article.id,
            'liked': liked,
            'count': article.like_set.count(),
        }
    
    if request.is_ajax():
        return JsonResponse(params)
