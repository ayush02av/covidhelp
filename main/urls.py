from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomePage, name='HomePage'),
    path('about/', views.AboutPage, name='AboutPage'),
    path('blog/', views.BlogPage, name='BlogPage'),
    path('vaccine/', views.VaccinePage, name='VaccinePage'),
    path('article/', views.ArticlePage)
]