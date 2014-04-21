from django.contrib import admin
from .models import *


''' Register Admin layouts into django'''
# admin.site.register(__MODEL-NAME__)
admin.site.register(Item)
admin.site.register(ItemType)
admin.site.register(Supplier)
admin.site.register(Color)
admin.site.register(Material)
admin.site.register(Revision)
admin.site.register(AttributeType)
admin.site.register(Template)
