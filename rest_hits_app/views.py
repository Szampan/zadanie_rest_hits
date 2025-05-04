from django.shortcuts import render
from rest_framework import viewsets
from .models import Hit
from .serializers import HitSerializer


class HitViewSet(viewsets.ModelViewSet):
    queryset = Hit.objects.all().order_by('-created_at')
    serializer_class = HitSerializer
    lookup_field = 'title_url'
