from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    #path('grappelli/', include('grappelli.urls')),
    path('', admin.site.urls),    
]
