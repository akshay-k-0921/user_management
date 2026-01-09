from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from . import frontend_views


schema_view = get_schema_view(
    openapi.Info(
        title="User Management API",
        default_version='v1',
        description="APIs for authentication, profile management and task CRUD",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="support@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # Root
    path("", frontend_views.root, name="root"),
    
    # frontend urls
    path("signup/", frontend_views.signup),
    path("login/", frontend_views.login_view),
    path("home/", frontend_views.home),
    path("task/<int:id>/", frontend_views.task_detail),
    path("task-detail/", frontend_views.task_detail),
    path("add-task/", frontend_views.add_task),
    path("edit-task/<int:id>/", frontend_views.edit_task),
    path("profile/", frontend_views.profile),
    path("reset-password/", frontend_views.reset_password),
    
    # backend urls
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.urls')),
    path('api/tasks/', include('tasks.urls')),

    # Swagger urls
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

