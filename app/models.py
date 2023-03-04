from django.db import models


# Create your models here.


    
class Bolimlar(models.Model):
    nomi = models.CharField(max_length=150)
    def __str__(self):
        return f"{self.nomi}"
    class Meta:
        verbose_name = "Bolim"
        verbose_name_plural = "Bolimlar"
    

class Ish(models.Model):
    ism = models.CharField(max_length=100)
    bolim = models.ForeignKey(Bolimlar, on_delete=models.CASCADE)
    familiya = models.CharField(max_length=100)
    yosh = models.DateField(help_text='Kun | oy | yil')
    manzil = models.CharField(max_length=100)
    


    def __str__(self):
        return f"{self.ism} {self.familiya} {self.yosh} {self.manzil} "  
      

    class Meta:
        verbose_name = 'Ishchi'
        verbose_name_plural = 'Ishchilar' 
        
      


