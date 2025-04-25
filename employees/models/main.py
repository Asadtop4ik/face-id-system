from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Face(models.Model):
    name = models.CharField(max_length=150, default="null")
    face_width = models.CharField(max_length=255, default="null")
    face_height = models.CharField(max_length=255, default="null")
    landmark = models.CharField(max_length=255, default="null")
    smilingProbability = models.CharField(max_length=255, default="null")
    LeftEyeOpenProbability = models.CharField(max_length=255, default="null")
    rightEyeOpenProbability = models.CharField(max_length=255, default="null")
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='face_images/', blank=True, null=True)
    face = models.TextField(default="null")

    def __str__(self):
        return self.name


class Attendance(models.Model):
    staff = models.ForeignKey(User, on_delete=models.CASCADE)
    came = models.DateTimeField()
    went = models.DateTimeField()
    went_lunch = models.DateTimeField()
    came_lunch = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.staff.first_name} {self.staff.last_name}"


class Company(models.Model):
    name = models.CharField(max_length=255)
    lat = models.CharField(max_length=255)
    long = models.CharField(max_length=255)
    radius = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Schedule(models.Model):
    staff = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.CharField(max_length=255)
    start_work = models.CharField(max_length=255)
    lunch_start = models.CharField(max_length=255)
    lunch_end = models.CharField(max_length=255)
    end_work = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.staff.first_name} {self.staff.last_name}"


