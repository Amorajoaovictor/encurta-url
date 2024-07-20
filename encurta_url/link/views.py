from django.shortcuts import render
from rest_framework import viewsets

from link.models import Link
from link.serializers import LinkSerializer
# Create your views here.
class LinkViewSet(viewsets.ModelViewSet):
	queryset = Link.objects.all()
	serializer_class = LinkSerializer

