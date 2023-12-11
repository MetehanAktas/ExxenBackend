from django.db import models

# Create your models here.
class Movie(models.Model):
    isim = models.CharField(max_length=30)
    resim = models.FileField( upload_to="filmler",blank=True,null=True,verbose_name="Film ismi giriniz")
    aciklama = models.TextField(max_length=300,null=True,blank=True)
    def __str__(self):
        return self.isim