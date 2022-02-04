from django.contrib import admin

from .models import *


admin.site.register(House)
admin.site.register(Flat)
admin.site.register(Notary)
admin.site.register(Announcement)
admin.site.register(UserFilter)
admin.site.register(Favorite)
admin.site.register(GalleryAnnouncement)

