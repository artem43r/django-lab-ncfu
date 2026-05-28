from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import News, Category
from .forms import NewsForm, ContactForm
from .utils import MetaTagsMixin, MyMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from .forms import NewsForm, ContactForm, UserPasswordResetForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = ContactForm()

    return render(request,
                  'news/contact.html',
                  {'form': form})
    
    
class HomeNews(MetaTagsMixin, MyMixin, ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    #extra_context = {'title': 'Главная'}
    mixin_prop = 'hello world'
    paginate_by = 10
    meta_description = 'Главная страница новостей'
    meta_keywords = 'новости, django, сайт' 
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper('Главная страница')  
        context['mixin_prop'] = self.get_prop()
        return context
    
    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category', 'author')
class NewsByCategory(MetaTagsMixin, MyMixin, ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    allow_empty = False
    paginate_by = 2
    meta_description = 'Новости по категории'
    meta_keywords = 'новости, категория, django'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        context['title'] = self.get_upper(Category.objects.get(pk=self.kwargs['category_id']))
        return context
    
    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')
class ViewNews(DetailView):
    model = News
    context_object_name = 'news_item'
class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    #success_url = reverse_lazy('home')
    login_url = '/admin/'
    #raise_exception = True
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

