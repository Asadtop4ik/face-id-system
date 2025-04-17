from rest_framework import viewsets
from employees.models import Face, Attendance
from employees.serializers import FaceSerializer, AttendanceSerializer
from rest_framework.parsers import MultiPartParser, FormParser


class FaceViewSet(viewsets.ModelViewSet):
    queryset = Face.objects.all()
    serializer_class = FaceSerializer
    parser_classes = (MultiPartParser, FormParser)


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    parser_classes = (MultiPartParser, FormParser)



