from django.db import models
from django.contrib.auth.models import User
# Create your models here.
        
class Tenant(models.Model):
    name = models.CharField(max_length=255)
    domain = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.domain
    
class TenantUser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='tenant_user')
    tenant = models.ForeignKey(Tenant,on_delete=models.CASCADE, related_name='users')
    is_tenant_admin = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'tenant')
        

class Organization(models.Model):
    name = models.CharField(max_length=255)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='organizations')

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=255)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='departments')

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='customers')

    def __str__(self):
        return self.name