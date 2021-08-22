from django.contrib import admin
from .models import User, Gifters, Profile, ConfirmImage, Gifting, Receiving

# Register your models here.


admin.site.register(User)
admin.site.register(Gifters)
admin.site.register(Profile)
admin.site.register(ConfirmImage)
admin.site.register(Gifting)
admin.site.register(Receiving)