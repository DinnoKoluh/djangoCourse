from django.contrib import admin

# Register your models here.

from first_app.models import AccessRecord, Topic, Webpage, User

admin.site.register(AccessRecord)
admin.site.register(Webpage)
admin.site.register(Topic)
admin.site.register(User)

