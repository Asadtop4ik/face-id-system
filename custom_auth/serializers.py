from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from employees.models import Company, Schedule, Face

User = get_user_model()

# Serializer for Face model
class FaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Face
        fields = "__all__"  # Adjust to specific fields, e.g., ['id', 'image', 'encoding']

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
    face = FaceSerializer(read_only=True)  # Nest FaceSerializer for full object

    class Meta:
        model = User
        fields = [
            'id', 'username', 'first_name', 'last_name', 'birth_date', 'position',
            'group_name', 'department', 'gender', 'phone_number', 'start_work_at',
            'end_work_at', 'avatar', 'face_image', 'salary', 'created_at', 'updated_at',
            'is_active', 'is_staff', 'is_superuser', 'face', 'last_login', 'groups', 'user_permissions'
        ]
        read_only_fields = ('id', 'created_at', 'updated_at', 'last_login')

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
            all_staffs = UserSerializer(User.objects.filter(is_staff=False), many=True).data
            response_data["all_staffs"] = all_staffs

        return response_data