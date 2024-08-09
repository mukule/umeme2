from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500

handler404 = 'error_handling.views.custom_404'
handler500 = 'error_handling.views.custom_500'


urlpatterns = [
    path('', include('main.urls', namespace='main')),
    path('users/', include('users.urls', namespace='users')),
    path('vacancies/', include('vacancies.urls', namespace='vacancies')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
