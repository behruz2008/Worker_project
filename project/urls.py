
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin', admin.site.urls),
    # include - app loyihaning ichida urls fayliga yo'naltiramiz
    path('',include('app.urls')),
    
]
