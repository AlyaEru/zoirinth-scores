from django.shortcuts import render

from rest_framework import viewsets

from .serializers import ScoreSerializer
from .models import Score


class ScoreViewSet(viewsets.ModelViewSet):
    queryset = Score.objects.all().order_by('level')
    serializer_class = ScoreSerializer
