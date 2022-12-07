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

    def all_user_pages(self):
        with connection.cursor() as cursor:
            cursor.execute("""select users.id_user, users.name, pages.id_page from users
                                left join pages on users.id_user = pages.id_owner""")
            data = cursor.fetchall()
        return data

class FollowersSerializer(serializers.Serializer):
    id_page = serializers.IntegerField()
    id_user = serializers.IntegerField()

    def create_follower(self):
        with connection.cursor() as cursor:
            cursor.execute('insert into followers(id_page, id_user) values (%s, %s)',
                           list(self.validated_data.values()))
        return self.validated_data

    def delete_follower(self):
        with connection.cursor() as cursor:
            cursor.execute("delete from followers where id_page = %s and id_user = %s",
                           list(self.validated_data.values()))
        return self.validated_data

    def list_followers(self, pk):
        with connection.cursor() as cursor:
            cursor.execute("""select id_user, name, last_name from users
                           where id_user in (select id_user from followers where id_page = %s)""", [pk])
            data = cursor.fetchall()
        return data

    def count_followers(self, pk):
        with connection.cursor() as cursor:
            cursor.execute("""select count(id_user) from followers where id_page = %s""", [pk])
            data = cursor.fetchall()
        return data

    def max_followers(self):
        with connection.cursor() as cursor:
            cursor.execute("""create temp table counts as select id_page, count(*) as followers from followers Group By id_page;
                                select * from counts
                                where followers = (select max(followers) from counts)""")
            data = cursor.fetchall()
        return data

    def min_followers(self):
        with connection.cursor() as cursor:
            cursor.execute("""create temp table counts as select id_page, count(*) as followers from followers Group By id_page;
                                select * from counts
                                where followers = (select min(followers) from counts)""")
            data = cursor.fetchall()
        return data

    def avg_followers(self):
        with connection.cursor() as cursor:
            cursor.execute("""create temp table counts as select id_page, count(*) as followers from followers Group By id_page;
                                select * from counts
                                where followers = (select avg(followers) from counts)""")
            data = cursor.fetchall()
        return data

class PostsSerializer(serializers.ModelSerializer):
    id_page = serializers.IntegerField()
    id_user = serializers.IntegerField()
    reply_post = serializers.IntegerField(required=False)

    class Meta:
        model = Posts
        fields = ("id_page", "id_user", "content", "reply_post", "created_at")
        extra_kwargs ={"created_at": {"required": False}}


    def create_post(self):
        if "reply_post" not in self.validated_data:
            self.validated_data["reply_post"] = None
        with connection.cursor() as cursor:
            cursor.execute("""insert into posts(id_page, id_user, content, reply_post_id) values (%s, %s, %s, %s)""",
                           list(self.validated_data.values()))
        return self.validated_data

    def delete_post(self, pk):
        with connection.cursor() as cursor:
            cursor.execute("""delete from posts where id_post = %s""", [pk])
        return pk

    def list_posts(self, pk):
        with connection.cursor() as cursor:
            cursor.execute("""select id_page, id_post, content, reply_post_id, created_at from posts
                           where id_page in (select id_page from pages where id_page = %s)""", [pk])
            data = cursor.fetchall()
        return data

    def all_pages_content(self):
        with connection.cursor() as cursor:
            cursor.execute("""select pages.id_page, pages.description, posts.content
                                from pages
                                join posts on pages.id_page = posts.id_page;""")
            data = cursor.fetchall()
        return data

    def post_and_reply_posts(self):
        with connection.cursor() as cursor:
            cursor.execute("""select p1.id_post as reply_id, p1.content as reply_content, p2.id_post, p2.content
                                    from posts p1 join posts p2 on p1.reply_post_id = p2.id_post;""")
            data = cursor.fetchall()
        return data


