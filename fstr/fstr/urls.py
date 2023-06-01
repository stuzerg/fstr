from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from passag import views

router = routers.DefaultRouter()
router.register(r'coords', views.CoordsViewset)
router.register(r'uzers', views.UzersViewset)

urlpatterns = [
    path('pereval/', views.PerevalList.as_view()),
    path('pereval/submitData/', views.PerevalAddedViewset.as_view()),
    path('pereval/submitData/<int:pk>', views.PerevalDetails.as_view()),
    path('admin/', admin.site.urls),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
