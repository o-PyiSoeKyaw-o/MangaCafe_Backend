from rest_framework import serializers
from core.models import GenreModel, MangaModel

class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenreModel
        fields = ['id', 'name', 'slug']

class MangaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MangaModel
        fields = ['id', 'title', 'summary', 'cover_image', 'status', 'type', 'genres', 'is_premium']