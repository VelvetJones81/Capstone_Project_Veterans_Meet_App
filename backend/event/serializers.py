from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Event
        fields = ["id", "event_date", "venue", "organizer", "organizer_id" ]
        depth = 1
