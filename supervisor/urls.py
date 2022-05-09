from django.urls import path
from . import views
# from django.conf import settings
# from django.conf.urls.static import static


app_name = 'supervisor'


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('strict_register/', views.register_supervisor, name='register_supervisor'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('project-list/', views.usersView, name='project-list'),
    path('logout/', views.logout_view, name='logout'),
]


# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)