from django.contrib import admin
from django.contrib import messages
from django.utils.html import format_html
from .models import login, user, staff, Products

# Register your models here.

@admin.register(login)
class LoginAdmin(admin.ModelAdmin):
    list_display = ('logid', 'username', 'role', 'get_user_info')
    list_filter = ('role',)
    search_fields = ('username', 'role')
    ordering = ('logid',)
    readonly_fields = ('logid',)
    
    def get_user_info(self, obj):
        if obj.role == 'customer':
            try:
                user_obj = user.objects.get(login=obj)
                return format_html('<span style="color: green;">Customer: {}</span>', user_obj.fullname)
            except user.DoesNotExist:
                return format_html('<span style="color: red;">No user profile</span>')
        elif obj.role == 'staff':
            try:
                staff_obj = staff.objects.get(login=obj)
                return format_html('<span style="color: blue;">Staff: {}</span>', staff_obj.fullname)
            except staff.DoesNotExist:
                return format_html('<span style="color: red;">No staff profile</span>')
        return format_html('<span style="color: orange;">Admin</span>')
    
    get_user_info.short_description = 'User Information'

@admin.register(user)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'fullname', 'mail', 'mobileno', 'status', 'login_username')
    list_filter = ('status',)
    search_fields = ('fullname', 'mail', 'mobileno')
    ordering = ('user_id',)
    readonly_fields = ('user_id',)
    actions = ['approve_users', 'reject_users']
    
    def login_username(self, obj):
        return obj.login.username if obj.login else 'No Login'
    login_username.short_description = 'Username'
    
    def approve_users(self, request, queryset):
        updated = queryset.update(status='approved')
        self.message_user(request, f'{updated} users have been approved.', messages.SUCCESS)
    approve_users.short_description = "Approve selected users"
    
    def reject_users(self, request, queryset):
        updated = queryset.update(status='rejected')
        self.message_user(request, f'{updated} users have been rejected.', messages.SUCCESS)
    reject_users.short_description = "Reject selected users"

@admin.register(staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'fullname', 'mail', 'mobileno', 'status', 'aadhar', 'login_username')
    list_filter = ('status',)
    search_fields = ('fullname', 'mail', 'mobileno', 'aadhar')
    ordering = ('user_id',)
    readonly_fields = ('user_id',)
    actions = ['approve_staff', 'reject_staff']
    
    def login_username(self, obj):
        return obj.login.username if obj.login else 'No Login'
    login_username.short_description = 'Username'
    
    def approve_staff(self, request, queryset):
        updated = queryset.update(status='approved')
        self.message_user(request, f'{updated} staff members have been approved.', messages.SUCCESS)
    approve_staff.short_description = "Approve selected staff"
    
    def reject_staff(self, request, queryset):
        updated = queryset.update(status='rejected')
        self.message_user(request, f'{updated} staff members have been rejected.', messages.SUCCESS)
    reject_staff.short_description = "Reject selected staff"

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'pn', 'pq', 'pp', 'pc', 'display_image')
    search_fields = ('pn', 'pc')
    ordering = ('id',)
    readonly_fields = ('id',)
    list_filter = ('pc',)
    
    def display_image(self, obj):
        if obj.pi:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover;" />', obj.pi.url)
        return "No Image"
    display_image.short_description = 'Product Image'
