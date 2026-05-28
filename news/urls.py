from django.urls import path
from django.views.decorators.cache import cache_page
from django.contrib.auth import views as auth_views
from news.forms import UserPasswordResetForm


from .views import *

urlpatterns = [
    path('contact/', contact, name='contact'),
    path(
        'password-reset/',
        auth_views.PasswordResetView.as_view(
            form_class=UserPasswordResetForm,
            template_name='registration/password_reset_form.html'
        ),
        name='password_reset'
    ),
    path(
        '',
        cache_page(60, key_prefix='home_page')(HomeNews.as_view()),
        name='home'
    ),
    #path('', cache_page(60)(HomeNews.as_view()), name='home'),
    #path('', index, name='home'),
    #path('', HomeNews.as_view(), name='home'),
    #path('category/<int:category_id>/', get_category, name='category'),
    path('category/<int:category_id>/', NewsByCategory.as_view(extra_context={'title': 'Какой-то заголовок'}), name='category'),
    #path('news/<int:news_id>/', view_news, name='view_news'),
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),
    #path('add-news', add_news, name='add_news'),
    path('add-news', CreateNews.as_view(), name='add_news'),
    
]   