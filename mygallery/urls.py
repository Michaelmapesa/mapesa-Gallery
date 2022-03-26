from django.urls import path, re_path
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns=[
    path(' ',views.index,name = 'index'),
    re_path(r'^search/', views.search_image, name='search_image'),
    re_path(r'^location/(?P<image_location>\d+)', views.location_filter, name='location_filter'),
    re_path(r'^image/(?P<category_name>\w+)/(?P<image_id>\d+)',views.single,name = 'single')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
