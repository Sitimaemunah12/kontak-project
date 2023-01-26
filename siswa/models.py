from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
class jenis_kelamin(models.TextChoices):
    LakiLaki = 'L', ('Laki-Laki')
    PEREMPUAN = 'P', ('Perempuan')
        
class siswa(models.Model):
    NAMA = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, blank=True)
    hp = models.CharField(max_length=13, blank=True, null=True)
    alamat = models.TextField(blank=True, null=True)
    jenis_kelamin = models.CharField(
        max_length=1,
        choices=jenis_kelamin.choices,
    )
    tempat_lahir = models.CharField(max_length=100)
    tanggal_lahir = models.DateField()
    nisn = models.CharField(max_length=20)
    sekolah = models.CharField(max_length=50)
    create_by =models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name="siswa_created_by")
    create_at = models.DateTimeField (auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    # sekolah
    
        
        
    # perusahaan
    
    # default
    # create_by = 
   
    
    def __str__(self): 
        return self.NAMA
    
    class meta :
        db_table = "siswa"
        ordering = ["-id"]
        verbose_name_plural = "siswa"
    
