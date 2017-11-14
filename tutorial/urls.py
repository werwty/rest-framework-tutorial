
from django.conf.urls import url, include
from rest_framework import routers
from tutorial.views import UserViewSet, DocView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^schema/(?P<version>(v1))/', DocView.as_view(title='API Docs'), name='api_schema'),

]


