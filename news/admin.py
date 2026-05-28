from django.contrib import admin
from .models import News, Category
from django.db.models import Count
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = News
        fields = '__all__'

class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display=('id','title','category','created_at','updated_at','is_published')
    list_display_links=('id','title')
    search_fields=('title','content')
    list_editable=('is_published',)
    list_filter=('is_published','category')
    date_hierarchy = 'created_at'
    empty_value_display = '— нет данных —'

class CategoryAdmin(admin.ModelAdmin):
    list_display=('id','title','get_news_count')
    search_fields=('title',)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(news_count=Count('get_news'))
        return queryset

    def get_news_count(self, obj):
        return obj.news_count

    get_news_count.short_description = 'Количество новостей'
admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)