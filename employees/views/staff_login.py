from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.contrib.auth.hashers import check_password
from employees.models import Staff, Face
from employees.serializers import StaffLoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes


class StaffLoginView(APIView):
    permission_classes = [AllowAny]

    @extend_schema(
        # Define the request body using the serializer
        request=StaffLoginSerializer,
        # Define possible responses
        responses={
            200: OpenApiTypes.OBJECT,  # We'll define the structure inline
            400: OpenApiTypes.OBJECT,
            401: OpenApiTypes.OBJECT,
            404: OpenApiTypes.OBJECT,
        },
        # Add a description for the endpoint
        description="Authenticates a staff member using either face_id or phone_number and returns JWT tokens.",
        # Add examples for the request and responses
        examples=[
            OpenApiExample(
                name="Login with face_id",
                value={"face_id": 1},
                request_only=True,  # This example is for the request body
            ),
            OpenApiExample(
                name="Login with phone_number",
                value={"phone_number": "1234567890"},
                request_only=True,
            ),
            OpenApiExample(
                name="Successful Response",
                value={
                    "refresh": "your_refresh_token",
                    "access": "your_access_token",
                    "staff": {
                        "id": 1,
                        "first_name": "John",
                        "last_name": "Doe",
                        "phone_number": "1234567890",
                    },
                },
                response_only=True,  # This example is for the response
                status_codes=["200"],
            ),
            OpenApiExample(
                name="Bad Request Response",
                value={"non_field_errors": ["Either face_id or phone_number must be provided"]},
                response_only=True,
                status_codes=["400"],
            ),
        ],
    )
    def post(self, request):
        serializer = StaffLoginSerializer(data=request.data)
        if serializer.is_valid():
            face_id = serializer.validated_data.get('face_id')
            phone_number = serializer.validated_data.get('phone_number')

            try:
                # Try to find staff by face_id or phone_number
                if face_id:
                    staff = Staff.objects.get(face_id__id=face_id)
                elif phone_number:
                    staff = Staff.objects.get(phone_number=phone_number)
                else:
                    return Response(
                        {"error": "Either face_id or phone_number is required"},
                        status=status.HTTP_400_BAD_REQUEST
                    )

                # Generate JWT tokens
                refresh = RefreshToken.for_user(staff)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'staff': {
                        'id': staff.id,
                        'first_name': staff.first_name,
                        'last_name': staff.last_name,
                        'phone_number': staff.phone_number,
                    }
                }, status=status.HTTP_200_OK)

            except Staff.DoesNotExist:
                return Response(
                    {"error": "Invalid credentials"},
                    status=status.HTTP_401_UNAUTHORIZED
                )
            except Face.DoesNotExist:
                return Response(
                    {"error": "Face ID not found"},
                    status=status.HTTP_404_NOT_FOUND
                )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)