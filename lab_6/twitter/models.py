# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Chats(models.Model):
    id_chat = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    admin = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chats'


class ChatsUsers(models.Model):
    id_chat = models.OneToOneField(Chats, models.DO_NOTHING, db_column='id_chat', primary_key=True)
    id_user = models.ForeignKey('Users', models.DO_NOTHING, db_column='id_user')

    class Meta:
        managed = False
        db_table = 'chats_users'
        unique_together = (('id_chat', 'id_user'),)


class Followers(models.Model):
    id_page = models.OneToOneField('Pages', models.DO_NOTHING, db_column='id_page', primary_key=True)
    id_user = models.ForeignKey('Users', models.DO_NOTHING, db_column='id_user')

    class Meta:
        managed = False
        db_table = 'followers'
        unique_together = (('id_page', 'id_user'),)


class Logs(models.Model):
    date_time = models.DateTimeField(primary_key=True)
    action = models.CharField(max_length=128)
    id_user = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logs'
        unique_together = (('date_time', 'action', 'id_user'),)


class Messages(models.Model):
    id_chat = models.OneToOneField(Chats, models.DO_NOTHING, db_column='id_chat', primary_key=True)
    id_user = models.ForeignKey('Users', models.DO_NOTHING, db_column='id_user')
    content = models.CharField(max_length=512)
    date_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'messages'
        unique_together = (('id_chat', 'id_user', 'content', 'date_time'),)


class Pages(models.Model):
    id_page = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    description = models.CharField(max_length=512, blank=True, null=True)
    id_owner = models.ForeignKey('Users', models.DO_NOTHING, db_column='id_owner', blank=True, null=True)
    unblock_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pages'


class PagesTags(models.Model):
    id_page = models.OneToOneField(Pages, models.DO_NOTHING, db_column='id_page', primary_key=True)
    name = models.ForeignKey('Tags', models.DO_NOTHING, db_column='name')

    class Meta:
        managed = False
        db_table = 'pages_tags'
        unique_together = (('id_page', 'name'),)


class Posts(models.Model):
    id_post = models.AutoField(primary_key=True)
    id_page = models.ForeignKey(Pages, models.DO_NOTHING, db_column='id_page', blank=True, null=True)
    id_user = models.ForeignKey('Users', models.DO_NOTHING, db_column='id_user', blank=True, null=True)
    content = models.CharField(max_length=1024, blank=True, null=True)
    reply_post = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'posts'


class Reactions(models.Model):
    id_post = models.OneToOneField(Posts, models.DO_NOTHING, db_column='id_post', primary_key=True)
    id_user = models.ForeignKey('Users', models.DO_NOTHING, db_column='id_user')
    likes = models.BooleanField(blank=True, null=True)
    dislikes = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reactions'
        unique_together = (('id_post', 'id_user'),)


class Tags(models.Model):
    name = models.CharField(primary_key=True, max_length=128)

    class Meta:
        managed = False
        db_table = 'tags'


class Users(models.Model):
    id_user = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    last_name = models.CharField(max_length=128, blank=True, null=True)
    email = models.CharField(max_length=256, blank=True, null=True)
    password = models.CharField(max_length=64, blank=True, null=True)
    image_s3_path = models.CharField(max_length=256, blank=True, null=True)
    role = models.CharField(max_length=10, blank=True, null=True)
    is_blocked = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
        unique_together = (('id_user', 'email', 'password'),)
