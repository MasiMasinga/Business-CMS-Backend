from django.urls import path
from .views import DepartmentViewSet, RoleViewSet, EmployeeViewSet

urlpatterns = [
    path('departments/', DepartmentViewSet.as_view(
        {'get': 'list', 'post': 'create'}), name='departments'),
    path('departments/<int:pk>/', DepartmentViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='department'),
    path('roles/',
         RoleViewSet.as_view({'get': 'list', 'post': 'create'}), name='roles'),
    path('roles/<int:pk>/', RoleViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='role'),
    path('employees/',
         EmployeeViewSet.as_view({'get': 'list', 'post': 'create'}), name='employees'),
    path('employees/<int:pk>/', EmployeeViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='employee'),
]
