from django.contrib import admin
from .models import Customer, RoomManagement, BookingManagement, RoomService
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

admin.site.register(Customer)
admin.site.register(RoomManagement)
admin.site.register(BookingManagement)
admin.site.register(RoomService)
admin.site.site_header = "Resort Management Admin"
admin.site.site_title = "Resort Management"
admin.site.index_title = "Welcome to the Resort Management Dashboard"
