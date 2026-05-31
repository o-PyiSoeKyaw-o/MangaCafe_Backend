from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from core.models import MangaModel
from core.serializers import MangaListSerializer

@api_view(['GET'])
@permission_classes([AllowAny])
def manga_list(request):
    try:
        mangas = MangaModel.objects.all().order_by('title')
        serializer = MangaListSerializer(mangas, many=True)
        
        return Response({
            "success": True,
            "message": "Mangalist retrieved successfully",
            "mangas": serializer.data
        }, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response({
            "success": False,
            "message": f"Server error: {str(e)}"
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)