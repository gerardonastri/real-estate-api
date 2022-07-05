from rest_framework.serializers import ModelSerializer
from .models import Property
from .models import User


class PropertySerializer(ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'


# class UserSerializer(ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'
