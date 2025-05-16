from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Tenant, Organization, Department, Customer
from .serializers import (
    TenantSerializer, OrganizationSerializer,
    DepartmentSerializer, CustomerSerializer
)


# ------------ Tenant Views --------------

class TenantListCreateView(ListCreateAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    permission_classes = [IsAuthenticated]


class TenantDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    permission_classes = [IsAuthenticated]


# -----------Organization Views ---------------

class OrganizationListCreateView(ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated]
    # Filter by tenant if using tenant isolation for data isolation
    def get_queryset(self):
        tenant = self.request.tenant
        return Organization.objects.filter(tenant=tenant)


class OrganizationDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        tenant = self.request.tenant
        return Organization.objects.filter(tenant=tenant)


# ---- Department Views -------------

class DepartmentListCreateView(ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        tenant = self.request.tenant
        return Department.objects.filter(organization__tenant=tenant)


class DepartmentDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        tenant = self.request.tenant
        return Department.objects.filter(organization__tenant=tenant)


# -------- Customer Views ------------

class CustomerListCreateView(ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        tenant = self.request.tenant
        return Customer.objects.filter(department__organization__tenant=tenant)


class CustomerDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        tenant = self.request.tenant
        return Customer.objects.filter(department__organization__tenant=tenant)
