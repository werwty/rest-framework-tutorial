from rest_framework import viewsets
from tutorial.serializers import UserSerializer
from tutorial.models import MyUser

from rest_framework import response, permissions
from drf_openapi.views import SchemaView
from drf_openapi.entities import OpenApiSchemaGenerator


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer



class DocView(SchemaView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, version):
        generator = OpenApiSchemaGenerator(
            version=version,
            url=self.url,
            title=self.title
        )
        return response.Response(generator.get_schema(request, public=True))
