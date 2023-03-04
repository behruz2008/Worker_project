from django.shortcuts import render
from .models import *


from django.views.generic import ListView
# Django views modelida ListView metodi orqali ish ko'rishi

from .models import Ish
class IshView(ListView):
    model = Ish
    # content_object_name = Ish degani bu - frontend html fayllar uchun beriladigan o'zgaruvchining nomidir
    context_object_name = "Ish"
    template_name = "blog/index.html"
    
    


