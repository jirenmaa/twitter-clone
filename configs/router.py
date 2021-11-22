from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

urlpatterns = [
    path("auth/", include("modules.auth.routes")),
    path("tweets/", include("modules.tweets.routes")),
    path("<str:username>/", include("modules.users.routes")),
]

# allow static files to be served if in debug mode
# and if user does not using cloudinary storage as media storage
if not settings.USING_CLOUDINARY and settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
