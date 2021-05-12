from .serializers import UserSerializer
from rest_framework import viewsets
from .models import User
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    # queryset = Product.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        user = User.objects.all()
        return user

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = UserSerializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        user = User.objects.create(
            name=request.data['name'],
            last_name=request.data['last_name'],
            mail=request.data['mail'],
            password=request.data['password']
        )
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        if request.data['name'] is not '':
            user.name = request.data['name']
        if request.data['last_name'] is not '':
            user.last_name = request.data['last_name']
        if request.data['mail'] is not '':
            user.mail = request.data['mail']
        if request.data['password'] is not '':
            user.password = request.data['password']
        user.save()
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        return Response('User removed')
