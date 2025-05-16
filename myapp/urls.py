from django.urls import path
from .views import (
    TenantListCreateView, TenantDetailView,
    OrganizationListCreateView, OrganizationDetailView,
    DepartmentListCreateView, DepartmentDetailView,
    CustomerListCreateView, CustomerDetailView
)

urlpatterns = [
    path('api/tenants/', TenantListCreateView.as_view(), name='tenant-list-create'),
    path('api/tenants/<int:pk>/', TenantDetailView.as_view(), name='tenant-detail'),

    path('api/organizations/', OrganizationListCreateView.as_view(), name='organization-list-create'),
    path('api/organizations/<int:pk>/', OrganizationDetailView.as_view(), name='organization-detail'),

    path('api/departments/', DepartmentListCreateView.as_view(), name='department-list-create'),
    path('api/departments/<int:pk>/', DepartmentDetailView.as_view(), name='department-detail'),

    path('api/customers/', CustomerListCreateView.as_view(), name='customer-list-create'),
    path('api/customers/<int:pk>/', CustomerDetailView.as_view(), name='customer-detail'),
]
