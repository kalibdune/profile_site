from django.urls import path
from .import views
urlpatterns = [
    path('', views.index, name='home'),
    path('work-organica', views.work_organica, name='work-organica'),
    path('work-apollo', views.work_apollo, name='work-apollo'),
    path('site-portfolio', views.site_portfolio, name='site-portfolio')
]
