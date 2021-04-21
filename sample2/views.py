from django.shortcuts import render, get_object_or_404
from.models import Content, Comment
from django.http import JsonResponse

def content(request):
    contents = Content.objects.all()
    params = {
        'contents': contents,
    }
    return render(request, 'sample2/content.html', params)

def detail(request, pk):
    content = get_object_or_404(Content, pk=pk)
    comments = Comment.objects.filter(content_id=content.pk)
    params ={
        'content': content,
        'comments': comments,
    }
    return render(request, 'sample2/detail.html', params )


def comment(request):
    if request.method == 'POST':
        content = get_object_or_404(Content, pk=request.POST.get('content_id'))
        user = request.user
        comment = request.POST.get('comment')
        new = Comment(
            user = user,
            content = content,
            comment = comment,
        )
        new.save()

        params ={
            'content_id': content.id,
            'comment': new.comment,
        }
    
    if request.is_ajax():
        return JsonResponse(params)

