from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
)
from answers.models import Answer
from accounts.api.serializers import UserDetailSerializer

answer_url = HyperlinkedIdentityField(
    view_name='answers-api:detail',
    lookup_field='slug',
)
answer_delete_url = HyperlinkedIdentityField(
    view_name='answers-api:delete',
    lookup_field='slug',
)
answer_edit_url = HyperlinkedIdentityField(
    view_name='answers-api:edit',
    lookup_field='slug',
)


class AnswerCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = [
            'title',
            'type',
            'wait',
            'file',
        ]



class AnswerDetailSerializer(ModelSerializer):
    user = UserDetailSerializer(read_only=True)
    type = SerializerMethodField()
    delete_url = answer_delete_url
    edit_url = answer_edit_url
    class Meta:
        model = Answer
        fields = [
            'id',
            'title',
            'user',
            'note',
            'timestamp',
            'type',
            'file',
            'wait',
            'delete_url',
            'edit_url',
        ]


    def get_type(self, obj):
        return obj.get_type_display()


class AnswerListSerializer(ModelSerializer):
    user = UserDetailSerializer(read_only=True)
    type = SerializerMethodField()
    # url = answer_url
    delete_url = answer_delete_url
    edit_url = answer_edit_url
    class Meta:
        model = Answer
        fields = [
            # 'url',
            'id',
            'title',
            'user',
            'note',
            'timestamp',
            'type',
            'file',
            'delete_url',
            'edit_url',
    ]
    def get_type(self, obj):
        return obj.get_type_display()
