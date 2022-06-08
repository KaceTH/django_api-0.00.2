from django.contrib import admin

from  .models import StudentUser, CommunityWriting

# Register your models here.

admin.site.register(StudentUser)
admin.site.register(CommunityWriting)

