from django.contrib import admin
from django.urls import path

from . import views

app_name = "article"

urlpatterns = [
    path('', views.articles,name = "articles"),
    path('dashboard/', views.dashboard,name = "dashboard"),
    path('addarticle/', views.addarticle,name = "addarticle"),
    path('article/<int:id>', views.article,name = "article"),
    path('edit/<int:id>', views.edit,name = "edit"),
    path('delete/<int:id>', views.delete,name = "delete"),
    path('comment/<int:id>', views.addComment,name = "comment"),
    
]