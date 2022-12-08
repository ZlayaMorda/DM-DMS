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
        "list_pages": PageSerializer,
        "list_user_pages": PageSerializer
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

    @action(detail=False, methods=('get',), url_path='user-pages')
    def list_user_pages(self, request):
        serializer = self.get_serializer_class()
        serialized_page = serializer()
        return Response(serialized_page.all_user_pages(), status=HTTP_200_OK)

class FollowersView(BaseViewSet):
    action_serializers = {
        "create_follower": FollowersSerializer,
        "count_followers": FollowersSerializer,
        "delete_follower": FollowersSerializer,
        "list_followers": FollowersSerializer,
        "max_followers": FollowersSerializer,
        "min_followers": FollowersSerializer,
        "avg_followers": FollowersSerializer
    }
    @action(detail=False, methods=('post',), url_path='create')
    def create_follower(self, request):
        serializer = self.get_serializer_class()
        serialized_follower = serializer(data=request.data)
        serialized_follower.is_valid(raise_exception=True)
        serialized_follower.create_follower()
        return Response(serialized_follower.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=('post',), url_path='delete')
    def delete_follower(self, request):
        serializer = self.get_serializer_class()
        serialized_follower = serializer(data=request.data)
        serialized_follower.is_valid(raise_exception=True)
        serialized_follower.delete_follower()
        return Response(serialized_follower.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=('get',), url_path='list')
    def list_followers(self, request, **kwargs):
        return Response(self.get_queryset(**kwargs), status=HTTP_200_OK)

    def get_queryset(self, **kwargs):
        serializer = self.get_serializer_class()
        serialized_follower = serializer()
        return serialized_follower.list_followers(self.kwargs.pop("pk", None))

    @action(detail=True, methods=('get',), url_path='count')
    def list_followers(self, request, **kwargs):
        serializer = self.get_serializer_class()
        serialized_follower = serializer()
        return Response(serialized_follower.count_followers(self.kwargs.pop("pk", None)), status=HTTP_200_OK)

    @action(detail=False, methods=('get',), url_path='max-count')
    def max_followers(self, request, **kwargs):
        serializer = self.get_serializer_class()
        serialized_follower = serializer()
        return Response(serialized_follower.max_followers(), status=HTTP_200_OK)

    @action(detail=False, methods=('get',), url_path='min-count')
    def min_followers(self, request, **kwargs):
        serializer = self.get_serializer_class()
        serialized_follower = serializer()
        return Response(serialized_follower.min_followers(), status=HTTP_200_OK)

    @action(detail=False, methods=('get',), url_path='avg-count')
    def avg_followers(self, request, **kwargs):
        serializer = self.get_serializer_class()
        serialized_follower = serializer()
        return Response(serialized_follower.avg_followers(), status=HTTP_200_OK)

class PostsViews(BaseViewSet):
    action_serializers = {
        "create_post": PostsSerializer,
        "delete_post": PostsSerializer,
        "list_posts": PostsSerializer,
        "reply_to_post": PostsSerializer,
        "get_all_post_page": PostsSerializer,
        "get_all_post_reply_posts": PostsSerializer
    }

    @action(detail=False, methods=('post',), url_path='create')
    def create_post(self, request):
        serializer = self.get_serializer_class()
        serialized_post = serializer(data=request.data)
        serialized_post.is_valid(raise_exception=True)
        serialized_post.create_post()
        return Response(serialized_post.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=('delete',), url_path='delete')
    def delete_post(self, request, **kwargs):
        serializer = self.get_serializer_class()
        serialized_post = serializer()
        serialized_post.delete_post(self.kwargs.pop("pk", None))
        return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=('get',), url_path='list')
    def list_posts(self, request, **kwargs):
        serializer = self.get_serializer_class()
        serializer_post = serializer()
        return Response(serializer_post.list_posts(self.kwargs.pop("pk", None)), status=HTTP_200_OK)

    def get_queryset(self):
        pass

    @action(detail=False, methods=('get',), url_path='all-post-page')
    def get_all_post_page(self, request, **kwargs):
        serializer = self.get_serializer_class()
        serializer_post = serializer()
        return Response(serializer_post.all_pages_content(), status=HTTP_200_OK)

    @action(detail=False, methods=('get',), url_path='all-post-reply-posts')
    def get_all_post_reply_posts(self, request, **kwargs):
        serializer = self.get_serializer_class()
        serializer_post = serializer()
        return Response(serializer_post.post_and_reply_posts(), status=HTTP_200_OK)
