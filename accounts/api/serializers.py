from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.db.models import Q

from rest_framework.serializers import (
    CharField,
    EmailField,
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError,
)

User = get_user_model()

ask_user = HyperlinkedIdentityField(
    view_name='asks-api:questions',
    lookup_field='username',
)

class UserDetailSerializer(ModelSerializer):
    questions_url = ask_user
    group = SerializerMethodField()
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'questions_url',
            'group',
            # 'first_name',
            # 'last_name',
        ]

    def get_group(self,obj):
        if not obj.is_staff or not obj.is_superuser:
            return "normal"
        else:
            return "staff"

class UserCreateSerializer(ModelSerializer):
    email = EmailField(label='Email Address')
    email2 = EmailField(label='Confirm Email')
    group = CharField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password',
            'group',

        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                        }

    def validate(self, data):
        # email = data['email']
        # user_qs = User.objects.filter(email=email)
        # if user_qs.exists():
        #     raise ValidationError("This user has already registered.")
        return data

    def validate_email(self, value):
        data = self.get_initial()
        email1 = data.get("email2")
        email2 = value
        if email1 != email2:
            raise ValidationError("Emails must match.")

        user_qs = User.objects.filter(email=email2)
        if user_qs.exists():
            raise ValidationError("This user has already registered.")

        return value

    def validate_email2(self, value):
        data = self.get_initial()
        email1 = data.get("email")
        email2 = value
        if email1 != email2:
            raise ValidationError("Emails must match.")

        return value

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(
            username=username,
            email=email
        )
        user_obj.set_password(password)
        user_obj.save()
        validated_data['group'] = "Normal"
        return validated_data


class UserLoginSerializer(ModelSerializer):
    # token = CharField(allow_blank=True, read_only=True)
    username = CharField(required=False, allow_blank=True)
    email = EmailField(label='Email Address', required=False, allow_blank=True)
    group = CharField(required=False, allow_blank=True)
    # questions = ask_user
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'password',
            # 'token',
            'group',
        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                        }

    def validate(self, data):
        user_obj = None
        email = data.get("email", None)
        username = data.get("username", None)
        password = data.get("password", None)
        if not email and not username:
            raise ValidationError("A username or email is required to login")
        user = User.objects.filter(
            Q(email=email) |
            Q(username=username)
        ).distinct()
        user = user.exclude(email__isnull=True).exclude(email__iexact='')
        print user
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError("This username/email is not valid")
        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Incorrect credentials please try again")
        data['username'] = user_obj.username
        data['email'] = user_obj.email
        if not user_obj.is_staff or not user_obj.is_superuser:
            data['group'] = "normal"
        else:
            data['group'] = "staff"
        return data