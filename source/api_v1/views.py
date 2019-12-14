from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from api_v1.serializers import CommentSerializer
from webapp.models import Comment, Image


class CommentViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

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
        return Response({'comment_id': comment.id, 'created' : comment.created})

class likesView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        image = Image.objects.get(pk = kwargs['pk'])
        oper = request.data['oper']
        print(image)
        if oper == 'like':
            image.likes += 1
            image.users_like.add(User.objects.get(username=request.data['user']))
        elif oper == 'dislike':
            image.likes -= 1
            image.users_like.remove(User.objects.get(username=request.data['user']))
        image.save()
        return JsonResponse({'like': image.likes})


