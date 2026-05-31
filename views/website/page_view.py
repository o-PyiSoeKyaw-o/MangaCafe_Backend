from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import MangaModel, ChapterModel
from .serializers import MangaListSerializer, MangaDetailSerializer, ChapterDetailSerializer

@api_view(['GET', 'POST'])
def manga_list_create_view(request):
    if request.method == 'GET':
        mangas = MangaModel.objects.all()
        serializer = MangaListSerializer(mangas, many=True)
        return Response(serializer.data)
        
    elif request.method == 'POST':
        serializer = MangaListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)