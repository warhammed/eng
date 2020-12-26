from django.contrib import admin
from core import views as core
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core.index, name="home"),
    path('introducing/', core.introducing, name="introducing"),
]
urlpatterns += i18n_patterns(
    path('introducing/', core.introducing, name="introducing"),
    path('contact/', core.contact, name="contact"),
    path('managers/', core.managers, name="managers"),
    path('labs/', core.labs, name="labs"),
    path('group/', include('groups.urls')),
    path('fields/', include('fields.urls')),
    path('staff/', include('staff.urls')),
    path('album/', include('album.urls')),
    path('news/', include('news.urls')),
)


if settings.DEBUG:
   urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'core.views.error404'
handler500 = 'core.views.error500'