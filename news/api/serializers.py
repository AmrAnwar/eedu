from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
)
from news.models import Post

post_url = HyperlinkedIdentityField(
    view_name='news-api:detail',
    lookup_field='slug',
)
post_delete_url = HyperlinkedIdentityField(
    view_name='news-api:delete',
    lookup_field='slug',
)


class PostDetailSerializer(ModelSerializer):
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
        ]


class PostListSerializer(ModelSerializer):
    url = post_url
    delete_url = post_delete_url

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
        ]
