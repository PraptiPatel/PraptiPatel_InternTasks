from django.contrib import admin

from . models import company
from . models import product

admin.site.register(company)
admin.site.register(product)