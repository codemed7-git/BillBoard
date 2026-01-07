from django.urls import path
from .views import index, by_rubric, detail, add_bb, my_ads

app_name = 'bboard'

urlpatterns = [
    path('', index, name='index'),
    path('rubric/<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('detail/<int:pk>/', detail, name='detail'),
    path('add/', add_bb, name='add_bb'),
    path('my_ads/', my_ads, name='my_ads'),
]