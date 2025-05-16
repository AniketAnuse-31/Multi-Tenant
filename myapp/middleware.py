from .models import Tenant
from django.http import HttpResponseBadRequest

from django.utils.deprecation import MiddlewareMixin
from .models import Tenant

class TenantMiddleware(MiddlewareMixin):
    def process_request(self, request):
        domain = request.META.get('HTTP_X_TENANT_DOMAIN')
        if domain:
            try:
                request.tenant = Tenant.objects.get(domain=domain)
            except Tenant.DoesNotExist:
                request.tenant = None
        else:
            request.tenant = None
