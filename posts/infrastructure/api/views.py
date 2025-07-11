from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from posts.infrastructure.serializers.post_serializer import PostSerializer
from posts.usecases.create_post import create_post
from posts.usecases.approve_post import approve_post
from posts.usecases.update_post import update_post
from posts.usecases.delete_post import delete_post
from posts.usecases.list_pending_posts import get_pending_posts
from posts.usecases.get_approved_posts import get_approved_posts
from posts.usecases.get_post_summary import get_post_summary
from posts.infrastructure.persistence.get_repository import get_post_repository
from drf_spectacular.utils import extend_schema

@extend_schema(
    request=PostSerializer,
    responses=PostSerializer,
    description="Crea una nueva publicación pendiente de aprobación."
)
class PostCreateView(APIView):
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            repository = get_post_repository()
            post = create_post(serializer.validated_data, repository)
            return Response(PostSerializer(post).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(
    request=None,
    responses=PostSerializer,
    description="Aprueba una publicación existente.",
    methods=["PATCH"]
)
class ApprovePostView(APIView):
    def patch(self, request, post_id):
        repository = get_post_repository()
        post = approve_post(post_id, repository)

        if not post:
            return Response({"detail": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

        return Response(PostSerializer(post).data, status=status.HTTP_200_OK)

@extend_schema(
    request=PostSerializer,
    responses=PostSerializer,
    description="Actualiza parcialmente una publicación existente.",
    methods=["PATCH"]
)
class PostUpdateView(APIView):
    def patch(self, request, post_id):
        serializer = PostSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            repository = get_post_repository()
            updated_post = update_post(post_id, serializer.validated_data, repository)

            if not updated_post:
                return Response({"detail": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

            return Response(PostSerializer(updated_post).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@extend_schema(
    request=None,
    responses={204: None},
    description="Elimina una publicación existente.",
    methods=["DELETE"]
)
class PostDeleteView(APIView):
    def delete(self, request, post_id):
        repository = get_post_repository()
        success = delete_post(post_id, repository)

        if not success:
            return Response({"detail": "Post not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)

@extend_schema(
    responses=PostSerializer(many=True),
    description="Retorna todas las publicaciones pendientes por aprobación.",
    methods=["GET"]
)
class PostPendingListView(APIView):
    def get(self, request):
        repository = get_post_repository()
        posts = get_pending_posts(repository)
        return Response(PostSerializer(posts, many=True).data, status=status.HTTP_200_OK)

@extend_schema(
responses=PostSerializer(many=True),
description="Retorna todas las publicaciones aprobadas.",
)
class PostApprovedListView(APIView):
    def get(self, request):
        repository = get_post_repository()
        posts = get_approved_posts(repository)
        return Response(PostSerializer(posts, many=True).data, status=status.HTTP_200_OK)
    
@extend_schema(
    responses={
        200: {
            "type": "object",
            "properties": {
                "approved": {"type": "integer"},
                "pending": {"type": "integer"},
                "total": {"type": "integer"},
            },
            "example": {
                "approved": 15,
                "pending": 4,
                "total": 19
            }
        }
    },
    description="Devuelve un resumen con la cantidad de publicaciones aprobadas, pendientes y el total."
)
class PostSummaryView(APIView):
    def get(self, request):
        repository = get_post_repository()
        summary = get_post_summary(repository)
        return Response(summary, status=status.HTTP_200_OK)