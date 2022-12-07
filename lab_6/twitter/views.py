from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import GenericViewSet
from twitter.serializers import *


class BaseViewSet(GenericViewSet):
    """
    GenericViewSet with permissions and serializers by action
    action_serializers = {
        'list': DefaultListSerializer,
    }
    """

    serializer_class = EmptySerializer
    action_serializers = {}

    def get_serializer_class(self):
        return self.action_serializers.get(self.action, self.serializer_class)


class UserView(BaseViewSet):
    action_serializers = {
        "create_user": UserSerializer,
        "update_user": UserSerializer,
        "delete_user": UserSerializer,
        "list_users": UserSerializer
    }

    @action(detail=False, methods=('post',), url_path='create')
    def create_user(self, request):
        serializer = self.get_serializer_class()
        serialized_user = serializer(data=request.data)
        serialized_user.is_valid(raise_exception=True)
        serialized_user.save()
        return Response(serialized_user.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=('post',), url_path='update')
    def update_user(self, request, **kwargs):
        serializer = self.get_serializer_class()
        serialized_user = serializer(data=request.data)
        serialized_user.is_valid(raise_exception=True)
        serialized_user.update_user(self.kwargs.pop("pk", None))
        return Response(status=HTTP_200_OK)

    @action(detail=True, methods=('delete',), url_path='delete')
    def delete_user(self, request, **kwargs):
        serializer = self.get_serializer_class()
        serialized_user = serializer()
        serialized_user.delete_user(self.kwargs.pop("pk", None))
        return Response(status=HTTP_200_OK)

    @action(detail=False, methods=('get',), url_path='list')
    def list_users(self, request):
        return Response(self.get_queryset(), status=HTTP_200_OK)

    def get_queryset(self):
        serializer = self.get_serializer_class()
        serialized_user = serializer()
        return serialized_user.list_users()


class PageView(BaseViewSet):
    action_serializers = {
        "create_page": PageSerializer,
        "update_page": PageSerializer,
        "delete_page": PageSerializer,
        "list_pages": PageSerializer
    }

    @action(detail=False, methods=('post',), url_path='create')
    def create_page(self, request):
        serializer = self.get_serializer_class()
        serialized_page = serializer(data=request.data)
        serialized_page.is_valid(raise_exception=True)
        serialized_page.save()
        return Response(serialized_page.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=('post',), url_path='update')
    def update_page(self, request, **kwargs):
        serializer = self.get_serializer_class()
        serialized_page = serializer(data=request.data)
        serialized_page.is_valid(raise_exception=True)
        serialized_page.update_page(self.kwargs.pop("pk", None))
        return Response(status=HTTP_200_OK)

    @action(detail=True, methods=('delete',), url_path='delete')
    def delete_page(self, request, **kwargs):
        serializer = self.get_serializer_class()
        serialized_page = serializer()
        serialized_page.delete_page(self.kwargs.pop("pk", None))
        return Response(status=HTTP_200_OK)

    @action(detail=False, methods=('get',), url_path='list')
    def list_pages(self, request):
        return Response(self.get_queryset(), status=HTTP_200_OK)

    def get_queryset(self):
        serializer = self.get_serializer_class()
        serialized_page = serializer()
        return serialized_page.list_pages()
