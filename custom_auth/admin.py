from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from django.utils.safestring import mark_safe

User = get_user_model()

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['username', 'first_name', 'last_name', 'position', 'department', 'is_active']
    list_filter = ['is_active', 'is_staff', 'gender']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'birth_date', 'gender', 'phone_number', 'avatar', 'face_image')}),
        ('Work Info', {'fields': ('position', 'group_name', 'department', 'salary', 'start_work_at', 'end_work_at')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Face', {'fields': ('face',)}),  # Updated from face_id to face
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name', 'last_name', 'position', 'department'),
        }),
    )
    readonly_fields = ['created_at', 'updated_at', 'avatar_preview']
    search_fields = ['username', 'first_name', 'last_name']
    ordering = ['username']
    filter_horizontal = ('groups', 'user_permissions')

    def avatar_preview(self, obj):
        if obj.avatar:
            return mark_safe(f'<img src="{obj.avatar.url}" width="100" height="100" />')
        return 'No avatar'
    avatar_preview.short_description = 'Avatar Preview'

    def get_readonly_fields(self, request, obj=None):
        return self.readonly_fields

admin.site.register(User, CustomUserAdmin)