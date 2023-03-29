# from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.core.paginator import Paginator
from .filters import ArticleFilter
from .models import Article
from .forms import ArticleForm


class ArticleList(ListView):
    model = Article
    template_name = 'news.html'
    context_object_name = 'article'
    ordering = ['-id']
    paginate_by = 1


class ArticleSearch(ListView):
    model = Article
    template_name = 'search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ArticleFilter(self.request.GET, queryset=self.get_queryset())
        return context


class ArticleDetail(DetailView):
    template_name = 'newsdetail.html'
    queryset = Article.objects.all()
   

class AddArticle(CreateView):
    template_name = 'addnews.html'
    form_class = ArticleForm
    
    
class ArticleUpdateView(UpdateView):
    template_name = 'article_update.html'
    form_class = ArticleForm
 
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Article.objects.get(pk=id)
 

class ArticleDeleteView(DeleteView):
    template_name = 'article_delete.html'
    queryset = Article.objects.all()
    success_url = '/news/'
