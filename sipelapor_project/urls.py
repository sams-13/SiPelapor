from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from reports import views

urlpatterns = [
    path('admin-panel/', admin.site.urls),
    path('admin/', RedirectView.as_view(url='/admin-panel/', permanent=False)),
    
    path('laporan/', views.laporan_saya, name='laporan'),
    
    path('', include('reports.urls')),
    path('accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)