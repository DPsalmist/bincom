from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(AGENT_NAME)
class AGENT_NAMEAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'last_name', 'phone', 'email', 'poll_unit_id']
	# prepopulated_fields = {'first_name': 'last_name' 'phone' 'email'}

@admin.register(POLLING_UNIT)
class POLLING_UNITAdmin(admin.ModelAdmin):
	list_display = ['polling_unit_name', 'poll_unit_id', 'polling_unit_description']
	search_fields = ['poll_unit_id', 'polling_unit_name']

admin.site.register(ANNOUNCED_LGA_RESULTS)

admin.site.register(ANNOUNCED_PU_RESULTS)

admin.site.register(ANNOUNCED_STATE_RESULTS)

admin.site.register(ANNOUNCED_WARD_RESULTS)

admin.site.register(PARTY)

admin.site.register(LGA)

admin.site.register(WARD)

admin.site.register(STATES)