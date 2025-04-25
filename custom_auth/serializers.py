from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from employees.models import Company, Schedule

User = get_user_model()

# Serializer for Company model
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"  # Adjust fields as needed

# Serializer for Schedule model
class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = "__all__"  # Adjust fields as needed

# Serializer for User model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__' # Explicitly list fields to avoid issues
        read_only_fields = ("id",)

class CustomTokenObtainPairSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError("Invalid credentials")

        refresh = RefreshToken.for_user(user)

        # Serialize QuerySets
        company_data = CompanySerializer(Company.objects.all(), many=True).data
        schedule_data = ScheduleSerializer(Schedule.objects.all(), many=True).data

        response_data = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "user_data": UserSerializer(user).data,
            "company_data": company_data,
            "schedule": schedule_data,
        }

        if user.is_staff:
            # Serialize non-staff users for all_staff
            all_staffs = UserSerializer(User.objects.filter(is_staff=False), many=True).data
            response_data["all_staffs"] = all_staffs

        return response_data