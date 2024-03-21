from rest_framework import serializers
from .models import Department, Role, Employee

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
    
    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError("The name field is required.")
        return value


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

    def validate_department(self, value):
        if not value:
            raise serializers.ValidationError("The department field is required.")
        return value

    def validate_job_title(self, value):
        if not value:
            raise serializers.ValidationError("The job_title field is required.")
        return value

    def validate_salary(self, value):
        if not value:
            raise serializers.ValidationError("The salary field is required.")
        return value


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError("The name field is required.")
        return value

    def validate_role(self, value):
        if not value:
            raise serializers.ValidationError("The role field is required.")
        return value

    def validate_department(self, value):
        if not value:
            raise serializers.ValidationError("The department field is required.")
        return value
