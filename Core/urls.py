from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from .views import signin, signup, signout, profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout'),
    path('profile/', profile, name='profile'),

    path('', include('kinopoisk.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )