from functools import update_wrapper
from django.urls import path
from django.contrib import admin
from django.views.generic import RedirectView
from .models import News, AboutUs, HelpQA, OurAdvantages, SliderMainPage, \
    PublicOffer, CallBack, SocialTypes, FooterHeaderObjects, ImageHelpQA


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish')


@admin.register(CallBack)
class CallBackAdmin(admin.ModelAdmin):
    list_display = ('type_of_treatment', 'called_status', 'published',)
    search_fields = ('user_name', 'user_phone',)
    list_filter = ('called_status',)


@admin.register(SocialTypes)
class SocialTypesAdmin(admin.ModelAdmin):
    list_display = ('contact_type', 'link_to')


@admin.register(HelpQA)
class HelpQAAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')


class RedirectToObject(admin.ModelAdmin):
    """Overriding a ModelAdmin class's methods.
     Specific implementations:
        1) limitation for add new objects
        2) redirecting to CRUD page on one existing object.
     """

    def has_add_permission(self, request):
        """limit for add 'About us'."""
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)

    def change_view(self, request, object_id=None, form_url='',
                    extra_context=None):
        try:
            object_id = self.model.objects.all().first().id
        except AttributeError:
            return self.changeform_view(request, None, form_url, extra_context)

        object_id = str(object_id)
        return self.changeform_view(request, object_id, form_url,
                                    extra_context)

    def get_urls(self):
        def wrap(view):
            def wrapper(*args, **kwargs):
                return self.admin_site.admin_view(view)(*args, **kwargs)

            wrapper.model_admin = self
            return update_wrapper(wrapper, view)

        info = self.model._meta.app_label, self.model._meta.model_name

        return [
            path('', wrap(self.change_view), name='%s_%s_changelist' % info),
            path('add/', wrap(self.add_view), name='%s_%s_add' % info),
            path('<path:object_id>/history/', wrap(self.history_view),
                 name='%s_%s_history' % info),
            path('<path:object_id>/delete/', wrap(self.delete_view),
                 name='%s_%s_delete' % info),
            path('<path:object_id>/change/', wrap(self.change_view),
                 name='%s_%s_change' % info),
            path('<path:object_id>/', wrap(RedirectView.as_view(
                pattern_name='%s:%s_%s_change' % ((self.admin_site.name,)
                                                  + info)
            ))),
        ]


@admin.register(ImageHelpQA)
class ImageHelpQAAdmin(RedirectToObject):
    pass


class SocialTypesInline(admin.StackedInline):
    """Allow to admin add contacts for footer (maximum 6)."""
    model = SocialTypes
    max_num = 6


@admin.register(FooterHeaderObjects)
class FooterHeaderObjectsAdmin(RedirectToObject):
    inlines = [SocialTypesInline]


@admin.register(PublicOffer)
class PublicOfferAdmin(RedirectToObject):
    pass


@admin.register(SliderMainPage)
class SliderMainPageAdmin(RedirectToObject):
    pass


@admin.register(AboutUs)
class AboutUsAdmin(RedirectToObject):
    pass


admin.site.register(OurAdvantages)
