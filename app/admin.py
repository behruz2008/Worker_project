from django.contrib import admin
from .models import Ish 
from.models import Bolimlar



class BolimlarAdmin(admin.ModelAdmin):
    list_display = ['nomi']
    list_filter = ['nomi']
    list_per_page = 10
    # search_fields ['nomi']
    class Meta:
        model = Bolimlar
admin.site.register(Bolimlar, BolimlarAdmin)



class IshAdmin(admin.ModelAdmin):
    list_display = ['ism','bolim','familiya','yosh','manzil']
    list_filter = ['ism','yosh']
    list_per_page = 10
    search_fields = ['ism']
    class Meta:
        model = Ish
admin.site.register(Ish, IshAdmin)




        
    
    






