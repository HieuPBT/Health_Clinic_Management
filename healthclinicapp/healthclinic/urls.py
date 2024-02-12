from django.urls import path, include, re_path
from healthclinic.views import AppointmentConfirm, AppointmentListCreate, UserViewSet
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = routers.DefaultRouter()
router.register('user', UserViewSet)
#router.register('appointment', AppointmentListCreate.as_view(), basename='appointment')
#router.register('appointment', AppointmentConfirm.as_view(), basename='appointment')

schema_view = get_schema_view(
    openapi.Info(
        title="Health Clinic API",
        default_version='v1',
        description="APIs for Health Clinic ", contact=openapi.Contact(email=""),
        license=openapi.License(name="Hieu PBT"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', include(router.urls)),
    path('appointment', AppointmentListCreate.as_view()),
    path('appointment/<int:pk>', AppointmentConfirm.as_view()),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0),
            name='schema-json'),
    re_path(r'^swagger/$',
            schema_view.with_ui('swagger', cache_timeout=0),
            name = 'schema-swagger-ui'),
    re_path(r'^redoc/$',
            schema_view.with_ui('redoc', cache_timeout=0),
            name='schema-redoc')
]