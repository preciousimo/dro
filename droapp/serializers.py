from rest_framework import serializers
from .models import LadyPCDetail

class LadyPCDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = LadyPCDetail
        fields = (
            'last_period_date', 'cycle_average', 'period_average', 'period_start_date', 'period_end_date'
        )