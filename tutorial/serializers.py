from rest_framework import serializers
from tutorial.models import MyUser

from django.utils.translation import ugettext_lazy as _


class UserSerializer(serializers.HyperlinkedModelSerializer):

    username = serializers.CharField(
        help_text=_("Required. x characters or fewer.")

    )

    title = serializers.CharField(
        help_text=_("title")

    )

    class Meta:
        model = MyUser
        fields = ('username', 'title')

