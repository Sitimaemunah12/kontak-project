from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
class kategori(models.TextChoices):
    PT = 'PT', ('PT')
    CV = 'CV', ('CV')
    Firma = 'Firma', ('Firma')
    Persero = 'Persero', ('Persero')
    Pemerintah = 'Pemerintah', ('Pemerintah')
    Koperasi = 'Koperasi', ('Koperasi')
    Perseorangan = 'Perseorangan', ('Perseorangan')
        
class Perusahaan(models.Model):
    nama_perusahaan = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, blank=True)
    hp = models.CharField(max_length=13, blank=True, null=True)
    alamat = models.TextField(blank=True, null=True)
    kategori = models.CharField(
        max_length=50,
        choices=kategori.choices,
    )
    bidang = models.CharField(max_length=50)
    daerah = models.TextField(blank=True, null=True)
    nama_pic = models.CharField(max_length=100)
    jabatan = models.CharField(max_length=50)
    hp = models.CharField(max_length=13, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True)
    create_by =models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name="perusahaan_created_by")
    create_at = models.DateTimeField (auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
        
    def __str__(self):
        return self.nama_perusahaan
    
    class meta :
        db_table = "perusahaan"
        ordering = ["-id"]
        verbose_name_plural = "perusahaan"
    
