from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
)
from study.models import Unit,Part,Word
from accounts.api.serializers import UserDetailSerializer

unit_url = HyperlinkedIdentityField(
    view_name='study-api:unit-detail',
    lookup_field='slug',
)
words_url = HyperlinkedIdentityField(
    view_name='study-api:part-detail',
    lookup_field='slug',
)
# answer_delete_url = HyperlinkedIdentityField(
#     view_name='answers-api:delete',
#     lookup_field='slug',
# )
# answer_edit_url = HyperlinkedIdentityField(
#     view_name='answers-api:edit',
#     lookup_field='slug',
# )


class WordDetailSerializer(ModelSerializer):
    class Meta:
        model = Word
        fields = [
            'name',
            'translation',
        ]


class PartDetailSerializer(ModelSerializer):
    words = SerializerMethodField()
    class Meta:
        model = Part
        fields = [
            'id',
            'title',
            'words'
        ]
    def get_words(self, obj):
            c_qs = Word.objects.filter(part=obj)
            words =WordDetailSerializer(c_qs, many=True).data
            return words


class UnitDetailSerializer(ModelSerializer):
    parts = SerializerMethodField()
    class Meta:
        model = Unit
        fields = [
            'id',
            'title',
            'note',
            'parts',
        ]

    def get_parts(self, obj):
            c_qs = Part.objects.filter(unit = obj)
            parts =PartDetailSerializer(c_qs, many=True).data
            return parts


class UnitListSerializer(ModelSerializer):
    url = unit_url
    class Meta:
        model = Unit
        fields = [
            'id',
            'title',
            'url',
            'note',
            'timestamp',
    ]