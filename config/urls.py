from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static


def homeView(request):
    return redirect('swagger-ui')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('employees.urls')),
    path('auth/', include('custom_auth.urls')),
    path('', homeView),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




