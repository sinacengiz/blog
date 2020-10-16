from django.contrib import admin
from .models import Article,Comment
admin.site.register(Comment)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display=["title","author","created_date","content"]
    list_display_links=["title","author","created_date","content"]
    search_fields=["title"]
    list_filter=["created_date"]
    class Meta:
        model=Article

