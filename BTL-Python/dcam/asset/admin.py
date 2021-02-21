from django.contrib import admin
from asset.models import *
import logging as log

# Register your models here.
admin.site.register(Device)
admin.site.register(Management)
admin.site.register(License)
admin.site.register(Product)
admin.site.register(Warranty)
admin.site.register(DjLogAdmin)
