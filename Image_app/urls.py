from django.urls import path
from .views import home,Select_image
urlpatterns = [
    path('', home,name='home'),
    path('category/<int:cid>/',Select_image ,name='home'),
]
