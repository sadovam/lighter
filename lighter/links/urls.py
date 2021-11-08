from django.urls import path

from . import views

app_name = 'links'
urlpatterns = [
    path('', views.links_index, name='index'),
    path('<int:page_id>/', views.page, name='page'),

]