from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from .routers import router

urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
]

handler500 = "taiga.base.api.views.api_server_error"


##############################################
# Front sitemap
##############################################

if settings.FRONT_SITEMAP_ENABLED:
    from django.contrib.sitemaps.views import index
    from django.contrib.sitemaps.views import sitemap
    from django.views.decorators.cache import cache_page

    from tiger.front.sitemaps import sitemaps

    urlpatterns += [
        url(r"^front/sitemap\.xml$",
            cache_page(settings.FRONT_SITEMAP_CACHE_TIMEOUT)(index),
            {"sitemaps": sitemaps, 'sitemap_url_name': 'front-sitemap'},
            name="front-sitemap-index"),
        url(r"^front/sitemap-(?P<section>.+)\.xml$",
            cache_page(settings.FRONT_SITEMAP_CACHE_TIMEOUT)(sitemap),
            {"sitemaps": sitemaps},
            name="front-sitemap")
    ]

##############################################
# Static and media files in debug mode
##############################################
if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    def mediafiles_urlpatterns(prefix):
        import re
        from django.views.static import serve

        return [
            url(r'^%s(?P<path>.*)$' % re.escape(prefix.lstrip('/')), serve, {'document_root': settings.MEDIA_ROOT})
        ]

    # Hardcoded only for development server
    urlpatterns += staticfiles_urlpatterns(prefix="/static/")
    urlpatterns += mediafiles_urlpatterns(prefix="/media/")


