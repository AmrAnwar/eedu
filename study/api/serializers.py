from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
)
from study.models import Unit, Part, Word, Test, WordBank, Exercise, Exam
from study import models



unit_url = HyperlinkedIdentityField(
    view_name='study-api:unit-detail',
    lookup_field='slug',
)
# words_url = HyperlinkedIdentityField(
#     view_name='study-api:part-detail',
#     lookup_field='slug',
# )
part_url = HyperlinkedIdentityField(
    view_name='study-api:part',
    lookup_field='id',
)

# answer_delete_url = HyperlinkedIdentityField(
#     view_name='answers-api:delete',
#     lookup_field='slug',
# )
# answer_edit_url = HyperlinkedIdentityField(
#     view_name='answers-api:edit',
#     lookup_field='slug',
# )


class DialogSerializer(ModelSerializer):
    class Meta:
        model = models.Dialog
        fields = [
            'description',
            'first_speaker',
            'second_speaker',
            'location',
        ]


class MistakeSerializer(ModelSerializer):
    class Meta:
        model = models.Mistake
        fields = [
            'description',
            'replace',
            'answer',
        ]


class CompleteSerializer(ModelSerializer):
    class Meta:
        model = models.Complete
        fields = [
            'description',
            'answer'
        ]


class ChoicesSerializer(ModelSerializer):
    answer = SerializerMethodField()
    class Meta:
        model = models.Choices
        fields = [
            'question',
            'choice_one',
            'choice_two',
            'choice_three',
            'answer',
        ]

    def get_answer(self, obj):
        return (getattr(obj, (obj.get_answer_display())))


class TestSerializer(ModelSerializer):
    choices = SerializerMethodField()
    complete = SerializerMethodField()
    mistake = SerializerMethodField()
    dialog = SerializerMethodField()

    class Meta:
        model = Test
        fields = [
            'title',
            'choices',
            'complete',
            'dialog',
            'mistake',
            # 'part',
        ]

    def get_choices(self, obj):
        choices = models.Choices.objects.filter(test=obj)
        return ChoicesSerializer(choices, many=True).data

    def get_complete(self, obj):
        complete = models.Complete.objects.filter(test=obj)
        return CompleteSerializer(complete, many=True).data

    def get_mistake(self, obj):
        mistake = models.Mistake.objects.filter(test=obj)
        return MistakeSerializer(mistake, many=True).data

    def get_dialog(self, obj):
        dialog = models.Dialog.objects.filter(test=obj)
        return DialogSerializer(dialog, many=True).data


class WordDetailSerializer(ModelSerializer):
    class Meta:
        model = Word
        fields = [
            'id',
            'name',
            'translation',
            'users',
        ]


class WordBankDetailSerializer(ModelSerializer):
    class Meta:
        model = WordBank
        fields = [
            'id',
            'user',
            'name',
            'translation',
        ]


class ExerciseSerializer(ModelSerializer):

    class Meta:
        model = Exercise
        fields = [
            'id',
            'question',
            'answer',
            'exam',
            'type',
            'users',
        ]


class ExamSerializer(ModelSerializer):

    class Meta:
        model = Exam
        fields = [
            'title',
            'id',
        ]


class PartDetailFullSerializer(ModelSerializer):
    words = SerializerMethodField()
    tests = SerializerMethodField()

    class Meta:
        model = Part
        fields = [
            'id',
            'title',
            'words',
            'tests',
        ]

    def get_words(self, obj):
        c_qs = Word.objects.filter(part=obj)
        words = WordDetailSerializer(c_qs, many=True).data
        return words

    def get_tests(self, obj):
        tests = Test.objects.filter(part=obj)
        tests_ser = TestSerializer(tests, many=True).data
        return tests_ser


class PartDetailTestSerializer(ModelSerializer):
    tests = SerializerMethodField()
    class Meta:
        model = Part
        fields = [
            'id',
            'title',
            'tests',
        ]

    def get_tests(self, obj):
        tests = Test.objects.filter(part=obj)
        tests_ser = TestSerializer(tests, many=True).data
        return tests_ser


class PartDetailWordSerializer(ModelSerializer):
    words = SerializerMethodField()
    class Meta:
        model = Part
        fields = [
            'id',
            'title',
            'words',
        ]

    def get_words(self, obj):
        c_qs = Word.objects.filter(part=obj)
        words = WordDetailSerializer(c_qs, many=True).data
        return words


class PartDetailSerializer(ModelSerializer):
    urlwords = SerializerMethodField()
    urltests = SerializerMethodField()
    class Meta:
        model = Part
        fields = [
            'id',
            'urlwords',
            'urltests',
            'title',
        ]

    def get_urlwords(self, obj):
        return obj.get_url_words()

    def get_urltests(self, obj):
        return obj.get_url_tests()

# class UnitDetailSerializer(ModelSerializer):
#     parts = SerializerMethodField()
#
#     class Meta:
#         model = Unit
#         fields = [
#             'id',
#             'title',
#             'note',
#             'parts',
#         ]
#
#     def get_parts(self, obj):
#         c_qs = Part.objects.filter(unit=obj)
#         parts = PartDetailSerializer(c_qs, many=True).data
#         return parts


class UnitListSerializer(ModelSerializer):
    parts = SerializerMethodField()

    class Meta:
        model = Unit
        fields = [
            'id',
            'title',
            'parts',
            'note',
            'timestamp',
        ]

    def get_parts(self, obj):
        c_qs = Part.objects.filter(unit=obj)
        parts = PartDetailSerializer(c_qs, many=True).data
        return parts


class UnitListV1Serializer(ModelSerializer):
    parts = SerializerMethodField()

    class Meta:
        model = Unit
        fields = [
            'id',
            'title',
            'parts',
            'note',
            'timestamp',
        ]

    def get_parts(self, obj):
        c_qs = Part.objects.filter(unit=obj)
        parts = PartDetailFullSerializer(c_qs, many=True).data
        return parts