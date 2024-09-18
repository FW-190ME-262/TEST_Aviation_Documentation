from .views import index, search_objects, set_cookie, del_cookie, \
    otziv, home
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', home, name='home'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('index', index, name='index'),
    path('set_cookie/', set_cookie, name='set_cookie'),
    path('del_cookie/', del_cookie, name='del_cookie'),
    path('otziv', otziv, name='otziv'),
    path('aircraft', views.aircraft_details, name='aircraft_details'),
    path('search/', search_objects, name='search_objects'),
    path('role_redirect/', views.role_redirect, name='role_redirect'),
    path('register', views.register, name='register'),
    path('search/', views.search_aircraft, name='search_aircraft'),
    path('aircraft', views.aircraft_poisk, name='aircraft_poisk'),
    path('aircraft/<int:id>/', views.aircraft_detail, name='aircraft_detail'),
    path('play/', views.play_game, name='play_game'),
    path('game-over/', views.game_over, name='game_over'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
