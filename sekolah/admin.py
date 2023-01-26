from django.contrib import admin
from .models import sekolah
class SekolahAdmin(admin.ModelAdmin):
    list_display = ['nama_smk', 'email', 'alamat',]
admin.site.register(sekolah, SekolahAdmin)
