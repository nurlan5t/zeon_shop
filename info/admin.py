from django.contrib import admin
from .models import News, AboutUs, HelpQA, OurAdvantages, SliderMainPage, \
    PublicOffer


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish')


class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title',)


class HelpQAAdmin(admin.ModelAdmin):
    list_display = ('question', )


admin.site.register(News, NewsAdmin)
admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(HelpQA, HelpQAAdmin)
admin.site.register(OurAdvantages)
admin.site.register(SliderMainPage)
admin.site.register(PublicOffer)
