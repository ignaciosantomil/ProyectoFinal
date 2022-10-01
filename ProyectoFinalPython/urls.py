from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from AppProyecto.views import *


urlpatterns = [
    path('', lambda req: redirect('AppProyectoInicio')),
    path('admin/', admin.site.urls),
    path('AppProyecto/', include('AppProyecto.urls')),
    path('UserProyecto/', include('UserProyecto.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)