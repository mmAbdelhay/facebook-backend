from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from Users.models import Post,Comment,Like
from posts.api.serializers import *


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def index(request):
    posts = Post.objects.all()
    serializer = PostSerializer(instance=posts, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def index2(request):
    posts = Comment.objects.all()
    serializer = CommentsSerializer(instance=posts, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create(request):
    serializer = PostSerializer(data=request.data)
    # print(request.user.id);
    if serializer.is_valid():
        serializer.save(request.user.id)
        return Response(data={
            "success": True,
            "message": "post has been added successfully"
        }, status=status.HTTP_201_CREATED)

    return Response(data={
        "success": False,
        "errors": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def addComment(request):
    serializer = CommentsSerializer(many=False, data=request.data)

    if serializer.is_valid():
        serializer.save(request.user.id)
        return Response(data={
            'message': 'comment added',
            'success': True
        }, status=status.HTTP_201_CREATED)
    return Response(data={
        'Error': serializer.errors,
        'success': False
    }, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def like(request):
    serializer = LikesSerializer(many=False, data=request.data)
    if serializer.is_valid():
        serializer.save(request.user.id)
        return Response(data={
            'message': 'you liked the post successfully',
            'success': True
        }, status=status.HTTP_201_CREATED)
    return Response(data={
        'Error': serializer.errors,
        'success': False
    }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def unlike(request, id):
    like = Like.objects.get(PID=id)
    serializer = LikesSerializer(instance=like, many=False)
    if request.user.id == like.UID.id:
        serializer.unlike(like)
        return Response(data={
            'message': 'unliked',
            'success': True
        }, status=status.HTTP_200_OK)
    else :
        return Response(data={
            'Error': 'not owner',
            'success': False
        }, status=status.HTTP_400_BAD_REQUEST)




@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete(request, id):
    post = Post.objects.get(pk=id)
    serializer = PostSerializer(instance=post, many=False)
    if request.user.id == post.poster_ID.id:
        serializer.delete()
        return Response(data={
            'message': 'deleted',
            'success': True
        }, status=status.HTTP_200_OK)
    else :
        return Response(data={
            'Error': 'not owner',
            'success': False
        }, status=status.HTTP_400_BAD_REQUEST)



@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update(request, id):
    post = Post.objects.get(pk=id)
    serializer = PostSerializer(instance=post, many=False, data=request.data)
    if serializer.is_valid():
        if request.user.id == post.poster_ID.id:
            serializer.update(request.data['content'],post)
            return Response(data={
                'message': 'post updated',
                'success': True
            }, status=status.HTTP_201_CREATED)
        else :
            return Response(data={
                'Error': 'not owner',
                'success': False
            }, status=status.HTTP_400_BAD_REQUEST)
    return Response(data={
        'Error': serializer.errors,
        'success': False
    }, status=status.HTTP_400_BAD_REQUEST)
