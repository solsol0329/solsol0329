from django.shortcuts import render,redirect,get_object_or_404
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST,require_safe


def index(request):
    movies = Article.objects.all()
    context = {
        'movies':movies,
    }
    return render(request, 'movies/index.html', context)

@require_http_methods(["GET","POST"])
@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.Post)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail')
    else:
        form = ArticleForm()
    context = {
        'form':form,
    }
    return render(request, 'movies/create.html', context)


@require_safe
@login_required
def detail(request,pk):
    movie = get_object_or_404(Article,pk=pk)
    context = {
        'movie':movie,
    }
    return render(request, 'movies/detail.html',context)



@login_required
def update(request,pk):
    movie = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie:detail')
    else:
        form = ArticleForm(instance=movie)
        context = {
            'form':form,
            'movie':movie,
        }
    return render(request, 'movies/update.html', context)




@require_POST
def delete(request,pk):
    if request.method == 'POST':
        movie = Article.objects.get(pk=pk)
        movie.delete()
    return redirect('movies:index')
