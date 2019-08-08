
from django.contrib import admin
from .models import Customer
from .models import Empolyee
from .models import Service

admin.site.register(Empolyee)
admin.site.register(Customer)
admin.site.register(Service)