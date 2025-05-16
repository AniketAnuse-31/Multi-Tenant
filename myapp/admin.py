from django.contrib import admin
from .models import Tenant, Organization, Department, Customer, TenantUser
# Register your models here.
admin.site.register(Tenant)
admin.site.register(TenantUser)
admin.site.register(Organization)
admin.site.register(Department)
admin.site.register(Customer)
