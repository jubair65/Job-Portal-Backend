from rest_framework import serializers

from .models import Application


class ApplicationSerializer(serializers.ModelSerializer):
    candidate_name = serializers.CharField(
        source="candidate.name",
        read_only=True
    )

    candidate_email = serializers.EmailField(
        source="candidate.email",
        read_only=True
    )

    job_title = serializers.CharField(
        source="job.title",
        read_only=True
    )

    company = serializers.CharField(
        source="job.company",
        read_only=True
    )

    class Meta:
        model = Application
        fields = [
            "id",
            "job",
            "job_title",
            "company",
            "candidate",
            "candidate_name",
            "candidate_email",
            "status",
            "applied_at",
        ]

        read_only_fields = [
            "id",
            "candidate",
            "candidate_name",
            "candidate_email",
            "job_title",
            "company",
            "status",
            "applied_at",
        ]


class ApplicationStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ["status"]

    def validate_status(self, value):
        allowed_statuses = {
            Application.Status.APPLIED,
            Application.Status.SHORTLISTED,
            Application.Status.REJECTED,
        }

        if value not in allowed_statuses:
            raise serializers.ValidationError(
                "Invalid application status."
            )

        return value