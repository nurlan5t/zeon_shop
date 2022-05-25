from django.contrib import admin
from .models import News, AboutUs


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'publish')


class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


admin.site.register(News, NewsAdmin)
admin.site.register(AboutUs, AboutUsAdmin)
