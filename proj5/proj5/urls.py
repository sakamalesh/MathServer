from django.contrib import admin
from django.urls import path
from app5 import views
urlpatterns=[
    path('admin/',admin.site.urls),
    path('areaofcylinder/',views.cyndarea,name="AreaofCylinder"),
    path('',views.cyndarea,name="AreaofCylinderroot")
]