from django.db import models

class Face(models.Model):
    name = models.CharField(max_length=150)
    face_width = models.CharField(max_length=255)
    face_height = models.CharField(max_length=255)
    landmark = models.CharField(max_length=255)
    smilingProbability = models.CharField(max_length=255)
    LeftEyeOpenProbability = models.CharField(max_length=255)
    rightEyeOpenProbability = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='face_images/')
    face = models.TextField()

    def __str__(self):
        return self.name


class Staff(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )

    face_id = models.ForeignKey(Face, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    birth_date = models.DateTimeField(blank=True, null=True)
    position = models.CharField(max_length=50)
    group_name = models.CharField(max_length=50, blank=True, null=True)
    department = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=50)
    start_word_at = models.DateTimeField(blank=True, null=True)
    end_word_at = models.DateTimeField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    face_image = models.ImageField(upload_to='face_images/', blank=True, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Attendance(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    came = models.DateTimeField()
    went = models.DateTimeField()
    went_lunch = models.DateTimeField()
    came_lunch = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.staff.first_name} {self.staff.last_name} - {self.came.strftime('%Y-%m-%d')}"
