from rest_framework import serializers
from watchlist_app.models import Movie
class MovieSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    description=serializers.CharField()
    active=serializers.BooleanField()
    
    def create(self,validated_data):
     return Movie.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.name=validated_data.get('name',instance)
        instance.description=validated_data.get('description',instance)
        instance.active=validated_data.get('active',instance)
        instance.save()
        return instance
        