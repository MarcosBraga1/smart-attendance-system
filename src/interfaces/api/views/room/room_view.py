from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from src.interfaces.api.permissions.is_admin import IsAdmin
from src.interfaces.api.serializers.room.create_room_serializer import CreateRoomSerializer
from src.interfaces.api.serializers.room.room_response_serializer import RoomResponseSerializer
from src.interfaces.api.serializers.room.update_room_serializer import UpdateRoomSerializer
from src.application.use_cases.room.create_room import CreateRoomUseCase
from src.application.use_cases.room.delete_room import DeleteRoomUseCase
from src.application.use_cases.room.get_room import GetRoomUseCase
from src.application.use_cases.room.list_room import ListRoomUseCase
from src.application.use_cases.room.update_room import UpdateRoomUseCase
from src.application.exceptions import NotFoundException, PermissionDeniedException
from src.infrastructure.db.repositories.room_repository_impl import DjangoRoomRepository

class RoomViewSet(ViewSet):
    
    permission_classes = [IsAuthenticated, IsAdmin]
    
    def create(self, request):
        serializer = CreateRoomSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        use_case = CreateRoomUseCase(
            room_repo=DjangoRoomRepository()
        )
        
        try:
            
            result = use_case.execute(data=serializer.validated_data)
            
            serializer = RoomResponseSerializer(result)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        except:
            return Response(
                {
                    "error": {
                        "code": "500_internal_server_error",
                        "message": "Error when creating room"
                    }
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def list(self, request):
        use_case = ListRoomUseCase(
            room_repo=DjangoRoomRepository()
        )
        
        rooms = use_case.execute()
        
        serializer = RoomResponseSerializer(rooms, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        use_case = GetRoomUseCase(
            room_repo=DjangoRoomRepository()
        )
        
        try:
            
            room = use_case.execute(room_id=pk, user=request.user)
            
            serializer = RoomResponseSerializer(room)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except NotFoundException:
            return Response(
                {
                    "error": {
                        "code": "404_not_found",
                        "message": "Room not found"
                    }
                }, status=status.HTTP_404_NOT_FOUND
            )
    
    def update(self, request, pk=None):
        serializer = UpdateRoomSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        
        use_case = UpdateRoomUseCase(
            room_repo=DjangoRoomRepository()
        )
        
        try:
            
            room = use_case.execute(room_id=pk, data=serializer.validated_data, user=request.user)
            
            serializer = RoomResponseSerializer(room)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except NotFoundException:
            return Response(
                {
                    "error": {
                        "code": "404_not_found",
                        "message": "Room not found"
                    }
                }, status=status.HTTP_404_NOT_FOUND
            )
            
        except PermissionDeniedException:
            return Response(
                {
                    "error": {
                        "code": "403_forbidden",
                        "message": "Not allowed"
                    }
                }, status=status.HTTP_403_FORBIDDEN
            )
    
    def destroy(self, request, pk=None):
        use_case = DeleteRoomUseCase(
            room_repo=DjangoRoomRepository()
        )
        
        try:
            
            use_case.execute(room_id=pk, user=request.user)
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        except NotFoundException:
            return Response(
                {
                    "error": {
                        "code": "404_not_found",
                        "message": "Room not found"
                    }
                }, status=status.HTTP_404_NOT_FOUND
            )
            
        except PermissionDeniedException:
            return Response(
                {
                    "error": {
                        "code": "403_forbidden",
                        "message": "Not allowed"
                    }
                }, status=status.HTTP_403_FORBIDDEN
            )