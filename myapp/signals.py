from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from .models import TenantUser, Tenant

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        # Only create TenantUser if we can assign a tenant
        # You'll need to implement your tenant assignment logic here
        # For testing, you might want to skip this or assign a default tenant
        try:
            TenantUser.objects.create(user=instance, tenant=Tenant.objects.first())
        except Exception as e:
            print(f"Couldn't create TenantUser: {e}")