from employees.models import Face, Staff, Attendance
from rest_framework import serializers


class FaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Face
        fields = '__all__'


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'