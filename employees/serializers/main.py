from employees.models import Face, Staff, Attendance
from rest_framework import serializers


class FaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Face
        fields = '__all__'


class StaffLoginSerializer(serializers.Serializer):
    face_id = serializers.IntegerField(required=False)
    phone_number = serializers.CharField(max_length=50, required=False)

    def validate(self, data):
        face_id = data.get('face_id')
        phone_number = data.get('phone_number')

        if not face_id and not phone_number:
            raise serializers.ValidationError("Either face_id or phone_number must be provided.")

        return data


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'