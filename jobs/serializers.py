from rest_framework import serializers

from .models import Job


class JobSerializer(serializers.ModelSerializer):
    employer_name = serializers.CharField(
        source="employer.name",
        read_only=True
    )

    class Meta:
        model = Job
        fields = [
            "id",
            "title",
            "company",
            "location",
            "salary",
            "description",
            "requirements",
            "job_type",
            "employer",
            "employer_name",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "employer",
            "employer_name",
            "created_at",
        ]

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError(
                "Job title cannot be empty."
            )

        return value.strip()

    def validate_salary(self, value):
        if value is not None and value < 0:
            raise serializers.ValidationError(
                "Salary cannot be negative."
            )

        return value