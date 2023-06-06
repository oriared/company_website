from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from config import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('cart/', include('cart.urls', namespace='cart')),
    path('cooperation/', include('cooperation.urls', namespace='cooperation')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('', include('core.urls', namespace='core')),
]

if settings.DEBUG:

    urlpatterns = [
        path('__debug__/', include('debug_toolbar.urls'))
    ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
