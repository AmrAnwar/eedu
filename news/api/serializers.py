from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
)
from news.models import Post
from accounts.api.serializers import UserDetailSerializer

post_url = HyperlinkedIdentityField(
    view_name='news-api:detail',
    lookup_field='slug',
)
post_delete_url = HyperlinkedIdentityField(
    view_name='news-api:delete',
    lookup_field='slug',
)
post_edit_url = HyperlinkedIdentityField(
    view_name='news-api:edit',
    lookup_field='slug',
)


class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'type',
            'wait',
            'image',
            'file',
        ]



class PostDetailSerializer(ModelSerializer):
    user = UserDetailSerializer(read_only=True)
    delete_url = post_delete_url
    edit_url = post_edit_url
    type = SerializerMethodField()
    class Meta:
        model = Post
        fields = [
            'id',
            'user',
            'type',
            'image',
            'file',
            'timestamp',
            'content',
            'wait',
            'delete_url',
            'edit_url',

        ]

    def get_type(self, obj):
        return obj.get_type_display()


class PostListSerializer(ModelSerializer):
    user = UserDetailSerializer(read_only=True)
    type = SerializerMethodField()
    url = post_url
    delete_url = post_delete_url
    edit_url = post_edit_url

    class Meta:
        model = Post
        fields = [
            'url',
            'id',
            'user',
            'type',
            'image',
            'timestamp',
            'delete_url',
            'edit_url',
        ]

    def get_type(self, obj):
        return obj.get_type_display()
