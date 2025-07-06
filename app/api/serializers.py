from app.users.models import UserProfile
from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterSerilizaer(serializers.ModelSerializer):
    phone=serializers.CharField()
    class Meta:
        model=User
        fields=['username','email','password','phone']
        extra_kwargs={'password':{'write_only':True}}

    def create(self, validated_data):
        phone=validated_data.pop('phone')
        user=User.objects.create_user(**validated_data)
        UserProfile.objects.create(user=user,phone=phone)
        return user
    
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields=['phone','address']

class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(source='userprofile', read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile']