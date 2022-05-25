from django.contrib import admin
from .models import News, AboutUs, HelpQA


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'publish')


class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


class HelpQAAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')


admin.site.register(News, NewsAdmin)
admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(HelpQA, HelpQAAdmin)

