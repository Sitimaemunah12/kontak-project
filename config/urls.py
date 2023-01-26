from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('halaman/', include("sekolah.urls")),
    path('', include("sekolah.urls")),

]
