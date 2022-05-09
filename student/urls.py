from django.urls import path
from . import views
# from django.conf import settings
# from django.conf.urls.static import static


app_name = 'student'


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_user, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('new-project/', views.newProject, name='new-project'),
    path('users/', views.usersView, name='users'),
    path('list/<int:profile_id>/', views.list, name='list'),
]


# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)