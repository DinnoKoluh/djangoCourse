from django.contrib import admin

from . import models
# Register your models here.
# No need to register models beacues we use Django's built-in models
class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember

admin.site.register(models.Group)
