from employees.models import Face, Attendance
from rest_framework import serializers


class FaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Face
        fields = '__all__'


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'