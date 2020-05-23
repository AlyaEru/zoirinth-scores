from rest_framework import serializers

from .models import Score

class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Score
        fields = ('user', 'points', 'level')
