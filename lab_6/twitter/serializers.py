from rest_framework import serializers
from .models import *
from django.db import connection

class EmptySerializer(serializers.Serializer):
    pass

def convert_to_null(values):
    for num in range(len(values)):
        if values[num] == '':
            values[num] = None
    return values

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ("name", "last_name", "email", "password", "image_s3_path", "role")

    def save(self):
        with connection.cursor() as cursor:
            cursor.execute('call create_user(%s, %s, %s, %s, %s, %s)', list(self.validated_data.values()))
        return self.validated_data

    def update_user(self, pk):
        self.validated_data['pk'] = pk
        with connection.cursor() as cursor:
             cursor.execute(
                 "UPDATE users SET name = COALESCE(%s, name)," +
                 " last_name = COALESCE(%s, last_name), email = COALESCE(%s, email)," +
                 " password = COALESCE(%s, password), image_s3_path = COALESCE(%s, image_s3_path)," +
                 " role = COALESCE(%s, role) where id_user = %s", convert_to_null(list(self.validated_data.values())))
        return self.validated_data

    def delete_user(self, pk):
        with connection.cursor() as cursor:
            cursor.execute("delete from users where id_user = %s", [pk])
        return pk

    def list_users(self):
        with connection.cursor() as cursor:
            cursor.execute("select * from users")
            data = cursor.fetchall()
        return data

class PageSerializer(serializers.ModelSerializer):
    id_owner = serializers.IntegerField(required=False)
    class Meta:
        model = Pages
        fields = ("name", "description", "id_owner")

    def save(self):
        with connection.cursor() as cursor:
            cursor.execute('insert into pages(name, description, id_owner) values (%s, %s, %s)', list(self.validated_data.values()))
        return self.validated_data

    def update_page(self, pk):
        if "id_owner" not in self.validated_data:
            self.validated_data["id_owner"] = None
        self.validated_data['pk'] = pk

        with connection.cursor() as cursor:
            cursor.execute(
                "UPDATE pages SET name = COALESCE(%s, name)," +
                " description = COALESCE(%s, description), id_owner = COALESCE(%s, id_owner)" +
                " where id_page = %s", convert_to_null(list(self.validated_data.values())))
        return self.validated_data

    def delete_page(self, pk):
        with connection.cursor() as cursor:
            cursor.execute("delete from pages where id_page = %s", [pk])
        return pk

    def list_pages(self):
        with connection.cursor() as cursor:
            cursor.execute("select * from pages")
            data = cursor.fetchall()
        return data
