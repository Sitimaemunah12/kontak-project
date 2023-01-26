from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
class Status(models.TextChoices):
    SWASTA = 'Swasta', ('Swasta')
    NEGERI = 'Negeri', ('Negeri')
    
class sekolah(models.Model):
        npsn = models.CharField(max_length=20, blank=True)
        nama_smk = models.CharField(max_length=50)
        email = models.CharField(blank=True, null=True, max_length=50)
        Status = models.CharField(
            max_length=10,
            choices=Status.choices
        )
        alamat = models.TextField(blank=True, null=True)
        provinsi = models.CharField(blank=True, null=True, max_length=50)
        kabupaten_kota = models.CharField(blank=True, null=True, max_length=50)
        kecamatan = models.CharField(blank=True, null=True, max_length=50)
        telp = models.CharField(max_length=13, blank=True, null=True)
        create_by =models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name="sekolah_created_by")
        create_at = models.DateTimeField (auto_now_add=True)
        update_at = models.DateTimeField(auto_now=True)
        
        def __str__(self):
            return self.nama_smk
        
class meta :
        db_table = "sekolah"
        ordering = ["-id"]
        verbose_name_plural = "sekolah"