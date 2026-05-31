from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from core.models import GenreModel
from core.serializers import GenreListSerializer

@api_view(['GET'])
@permission_classes([AllowAny])
def genre_list(request):
    try:
        genres = GenreModel.objects.all().order_by('name')
        serializer = GenreListSerializer(genres, many=True)
        
        return Response({
            "success": True,
            "message": "Genre list retrieved successfully",
            "genres": serializer.data
        }, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response({
            "success": False,
            "message": f"Server error: {str(e)}"
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)