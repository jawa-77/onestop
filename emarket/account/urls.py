from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('userinfo/',views.current_user,name='user_info'),
    path('userinfo/update/',views.update_user,name='update_user'),
]


from django.urls import path
from .views import current_user, update_user

urlpatterns = [
    path('userinfo/', current_user, name='user-info'),
    path('userinfo/update/', update_user, name='user-update'),
]
