from rest_framework import serializers

from link.models import Link
class LinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Link
        fields = "__all__" 