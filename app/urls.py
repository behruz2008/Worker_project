
from django.urls import path


from app.views import IshView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', IshView.as_view(), name= 'Ish'),
]



if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


