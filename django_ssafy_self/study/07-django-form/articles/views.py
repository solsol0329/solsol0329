from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm


# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


# def new(request):
#     form = ArticleForm()
#     context = {
#         'form':form,
#     }
#     return render(request, 'articles/new.html', context)


def create(request):
    # 만약 요청의 메서드가 post라면(create)
    if request.method == 'POST':
        form = ArticleForm(request.POST)

        # 유효성 검사
        # 유효성 검사가 통과된 경우
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail',article.pk)
        

        # title = request.POST.get('title')
        # content = request.POST.get('content')
        # article = Article(title=title, content=content)
        # article.save()
        # return redirect('articles:index')
    # 만약 요청의 메서드가 post가 아니라면(new)
    else:
        form = ArticleForm()
    context = {
    'form':form,
    }
    return render(request, 'articles/create.html', context)



def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     form = ArticleForm(instance=article)
#     context = {
#         'article': article,
#         'form' : form,
#     }
#     return render(request, 'articles/edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method =='POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save() 
            # save는 이게 생성인지 수정인지 판단할 기준이 필요함. 따라서 form에서 받을 때 instance=article를 넣어야 함
            return redirect('articles:detail', article.pk)
        # article.title = request.POST.get('title')
        # article.content = request.POST.get('content')
        # article.save()
        # return redirect('articles:detail', article.pk)

    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form' : form,
    }
    return render(request, 'articles/update.html', context)