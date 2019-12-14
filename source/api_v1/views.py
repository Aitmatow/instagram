from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api_v1.serializers import CommentSerializer
from webapp.models import Comment, Image


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        comment = Comment.objects.create(
            text=data['text'],
            image=Image.objects.get(pk=data['image']),
            author=User.objects.get(username=data['author'])
        )
        comment.save()
        print(comment.id)
        return Response({'comment_id': comment.id, 'created' : comment.created})

    # def get_queryset(self):
    #     if self.request.user.is_authenticated:
    #         return Comment.objects.all()
    #
    @action(methods=['post'], detail=True)
    def like(self, request, pk = None):
        comment = self.get_object()
        comment.image.likes += 1
        comment.image.save()
    #
    # @action(methods=['post'], detail=True)
    # def dislike(self, request, pk=None):
    #     comment = self.get_object()
    #     comment.image.likes -= 1
    #     comment.image.save()
